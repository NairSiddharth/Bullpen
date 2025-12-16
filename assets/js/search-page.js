fetch('/search.json')
  .then(res => res.json())
  .then(data => {
    const params = new URLSearchParams(window.location.search);
    const query = params.get('query');

    if (!query) return;

    const index = lunr(function () {
      this.ref('id');
      this.field('title', { boost: 10 });
      this.field('content');

      data.forEach((doc, i) => {
        doc.id = i;
        this.add(doc);
      });
    });

    const results = index.search(query);
    const list = document.getElementById('search-results');

    if (!results.length) {
      list.innerHTML = '<li>No results found</li>';
      return;
    }

    list.innerHTML = results.map(r => {
      const item = data[r.ref];
      return `
        <li>
          <a href="${item.url}">
            <strong>${item.title}</strong>
          </a>
          <p>${item.excerpt}</p>
        </li>
      `;
    }).join('');
  });
