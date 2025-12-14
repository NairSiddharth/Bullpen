(function () {
  function getQueryParam(param) {
    const params = new URLSearchParams(window.location.search);
    return params.get(param);
  }

  function renderResults(results, store) {
    const container = document.getElementById('search-results');

    if (!results.length) {
      container.innerHTML = '<li>No results found</li>';
      return;
    }

    container.innerHTML = results.map(result => {
      const item = store[result.ref];
      return `
        <li class="post-card neon-card">
          <h3 class="post-card-title">
            <a href="${item.url}">${item.title}</a>
          </h3>
          <p class="post-card-excerpt">${item.excerpt}</p>
        </li>
      `;
    }).join('');
  }

  const query = getQueryParam('query');
  if (!query) return;

  fetch('/search.json')
    .then(res => res.json())
    .then(data => {
      const store = {};
      const idx = lunr(function () {
        this.ref('id');
        this.field('title', { boost: 10 });
        this.field('content');
        this.field('tags');
        this.field('categories');

        data.forEach((doc, i) => {
          doc.id = i;
          this.add(doc);
          store[i] = doc;
        });
      });

      const results = idx.search(query);
      renderResults(results, store);
    });
})();
