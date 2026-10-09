# Full Count

Full Count is a Houston sports blog covering the Astros, Rockets, and Texans, built with Jekyll and hosted on GitHub Pages.

The writing sits between fandom and analysis. Instead of game recaps or breaking news, each post tries to work out why something is happening and what it means going forward, usually backed by projections, models, or visualizations rather than opinion alone. Topics range from trade analysis and prospect scouting to award tracking and playoff outlooks across all three teams.

## Features

- Ongoing analysis posts organized by team and category
- A Hall of Fame tracker for quantifying player careers over time
- Custom Jekyll layouts and includes for post archives, category pages, and search

## Stack

- Jekyll (minima theme, dark skin)
- GitHub Pages for hosting and deployment
- jekyll-seo-tag, jekyll-sitemap, jekyll-feed, and jekyll-redirect-from plugins

## Running locally

There's no Gemfile in this repo, so `bundle install` won't work. The site has no custom deploy workflow either, it's built directly by GitHub Pages from source. To run it locally, install Ruby and Jekyll, then:

```bash
gem install jekyll
jekyll serve
```

Site will be available at `http://localhost:4000/Bullpen/`.

## Site

Live at [nairsiddharth.github.io/Bullpen](https://nairsiddharth.github.io/Bullpen/).

## License

MIT, see [LICENSE](LICENSE).
