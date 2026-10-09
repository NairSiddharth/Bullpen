#!/usr/bin/env python3
"""Refresh career stat lines in _data/players.yml for the Hall of Fame Tracker.

Only stat lines whose label this script knows (Hits, HR, Sacks, Points, ...)
are rewritten, and only for players that have an `ids:` block. Everything else
-- fWAR, JAWS, Pro Bowls, All-Pro, hof_pace, summaries, commented-out players --
is left exactly as written.

Sources (all free, no API keys):
  MLB  statsapi.mlb.com             career hitting/pitching totals  ids.mlb
  NFL  nflverse stats_player files  sacks, tackles, interceptions   ids.nfl (GSIS id)
       nflverse PFR advanced def    pressures, cmp% when targeted   ids.pfr (2018+ only)
  NBA  ESPN athlete stats           points, rebounds, assists       ids.espn_nba

Usage:  python scripts/update_hof_stats.py [--dry-run] [--file _data/players.yml]
"""
import argparse
import csv
import datetime as dt
import io
import json
import re
import sys
import urllib.error
import urllib.request

import yaml

UA = {"User-Agent": "Mozilla/5.0 (FullCount HOF tracker; github.com/NairSiddharth)"}
NFLVERSE = "https://github.com/nflverse/nflverse-data/releases/download"
NFL_FIRST_SEASON = 2010  # earliest season summed; lower it if you add an older NFL player


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_csv(url):
    return list(csv.DictReader(io.StringIO(fetch(url).decode("utf-8"))))


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def fmt_int(x):
    return f"{int(round(x)):,}"


def fmt_half(x):  # sacks: 116.5, 34.5, 12
    return f"{x:,.1f}" if x % 1 else fmt_int(x)


# ---------------------------------------------------------------- MLB
def mlb_stats(ids):
    if not ids:
        return {}
    url = ("https://statsapi.mlb.com/api/v1/people?personIds=" + ",".join(map(str, ids))
           + "&hydrate=stats(group=[hitting,pitching],type=[career])")
    out = {}
    for p in json.loads(fetch(url))["people"]:
        vals = {}
        for block in p.get("stats", []):
            if not block.get("splits"):
                continue
            s = block["splits"][0]["stat"]
            if block["group"]["displayName"] == "hitting":
                vals.update({"Hits": fmt_int(s["hits"]), "HR": fmt_int(s["homeRuns"]),
                             "SB": fmt_int(s["stolenBases"]), "RBI": fmt_int(s["rbi"])})
            else:  # pitching
                vals.update({"Wins": fmt_int(s["wins"]), "K": fmt_int(s["strikeOuts"]),
                             "ERA": s["era"]})
        out[p["id"]] = vals
    return out


# ---------------------------------------------------------------- NFL
def nfl_stats(gsis_ids, pfr_ids):
    out = {}
    this_year = dt.date.today().year
    if gsis_ids:
        tot = {g: {"sacks": 0.0, "tkl": 0.0, "int": 0.0} for g in gsis_ids}
        for season in range(NFL_FIRST_SEASON, this_year + 1):
            try:
                rows = fetch_csv(f"{NFLVERSE}/stats_player/stats_player_reg_{season}.csv")
            except urllib.error.HTTPError as e:
                if e.code == 404:  # season file not published yet
                    continue
                raise
            for r in rows:
                t = tot.get(r["player_id"])
                if t is None:
                    continue
                t["sacks"] += num(r["def_sacks"])
                t["tkl"] += num(r["def_tackles_solo"]) + num(r["def_tackle_assists"])
                t["int"] += num(r["def_interceptions"])
        for g, t in tot.items():
            out[g] = {"Sacks": fmt_half(t["sacks"]), "Tackles": fmt_int(t["tkl"]),
                      "Int": fmt_int(t["int"])}
    if pfr_ids:
        adv = {p: {"prss": 0.0, "cmp": 0.0, "tgt": 0.0} for p in pfr_ids}
        for r in fetch_csv(f"{NFLVERSE}/pfr_advstats/advstats_season_def.csv"):
            a = adv.get(r["pfr_id"])
            if a is not None:
                a["prss"] += num(r["prss"])
                a["cmp"] += num(r["cmp"])
                a["tgt"] += num(r["tgt"])
        for p, a in adv.items():
            vals = {"Pressures": fmt_int(a["prss"])}
            if a["tgt"]:
                vals["Cmp% When Targeted"] = f"{100 * a['cmp'] / a['tgt']:.1f}%"
            out[p] = vals
    return out


# ---------------------------------------------------------------- NBA
def nba_stats(espn_ids):
    out = {}
    for i in espn_ids:
        d = json.loads(fetch(
            f"https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{i}/stats"))
        cat = next(c for c in d["categories"] if c["name"] == "totals")
        t = dict(zip(cat["names"], cat["totals"]))
        out[i] = {"Points": fmt_int(num(t["points"])),
                  "Rebounds": fmt_int(num(t["totalRebounds"])),
                  "Assists": fmt_int(num(t["assists"]))}
    return out


# ---------------------------------------------------------------- main
def collect(players):
    """Return {player name: {label: new value}}; a failing source is skipped, not fatal."""
    ids = {k: [p["ids"][k] for p in players if k in p.get("ids", {})]
           for k in ("mlb", "nfl", "pfr", "espn_nba")}
    results, failures = {}, []
    for name, fn, args in (("MLB", mlb_stats, (ids["mlb"],)),
                           ("NFL", nfl_stats, (ids["nfl"], ids["pfr"])),
                           ("NBA", nba_stats, (ids["espn_nba"],))):
        try:
            results.update(fn(*args))
        except Exception as e:  # keep the old numbers for this sport
            failures.append(name)
            print(f"WARNING: {name} source failed, keeping existing values: {e}", file=sys.stderr)

    updates = {}
    for p in players:
        merged = {}
        for key in ("mlb", "nfl", "pfr", "espn_nba"):
            v = p.get("ids", {}).get(key)
            if v is not None:
                merged.update(results.get(v, {}))
        if merged:
            updates[p["name"]] = merged
    return updates, failures


NAME_RE = re.compile(r'^- name:\s*["\']?(.+?)["\']?\s*$')
SECTION_RE = re.compile(r"^  (\w+):")
STAT_RE = re.compile(r'^(\s+-\s*")([^":]+):\s*([^"]*)(".*)$')


def apply(text, updates):
    """Rewrite matching stat lines in place, preserving comments and layout."""
    out, changes = [], []
    player = section = None
    for line in text.splitlines(keepends=True):
        if m := NAME_RE.match(line):
            player, section = m.group(1), None
        elif m := SECTION_RE.match(line):
            section = m.group(1)
        elif section == "stats" and player in updates and (m := STAT_RE.match(line)):
            label, old = m.group(2).strip(), m.group(3).strip()
            new = updates[player].get(label)
            if new is not None and new != old:
                line = f"{m.group(1)}{m.group(2)}: {new}{m.group(4)}"
                line += "" if line.endswith("\n") else "\n"
                changes.append(f"{player}: {label} {old} -> {new}")
        out.append(line)
    return "".join(out), changes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="_data/players.yml")
    ap.add_argument("--meta", default="_data/hof_meta.yml")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    text = open(a.file, encoding="utf-8").read()
    players = yaml.safe_load(text) or []
    updates, failures = collect(players)
    new_text, changes = apply(text, updates)

    print("\n".join(changes) if changes else "No stat changes.")
    if len(failures) == 3:
        sys.exit("All sources failed.")
    if changes and not a.dry_run:
        open(a.file, "w", encoding="utf-8").write(new_text)
        with open(a.meta, "w", encoding="utf-8") as f:
            f.write(f"stats_updated: {dt.date.today().isoformat()}\n")


if __name__ == "__main__":
    main()
