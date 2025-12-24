let index;
let store;

fetch(window.SITE_CONFIG.searchJsonPath)
  .then(res => res.json())
  .then(data => {
    store = {};
    index = lunr(function () {
      this.ref('id');
      this.field('title', { boost: 10 });
      this.field('content');
      this.field('categories');

      data.forEach((doc, i) => {
        doc.id = i;
        this.add(doc);
        store[i] = doc;
      });
    });
  });

const input = document.getElementById('header-search-input');
const results = document.getElementById('header-search-results');

if (input && results) {
  input.addEventListener('input', () => {
    const query = input.value.trim();

    if (!query || !index) {
      results.classList.remove('show');
      return;
    }

    const matches = index.search(query).slice(0, 6);

    if (!matches.length) {
      results.innerHTML = '<div class="search-no-results">No results found</div>';
      results.classList.add('show');
      return;
    }

    results.innerHTML = matches.map(match => {
      const item = store[match.ref];
      return `
        <a href="${item.url}" class="search-result">
          <strong>${item.title}</strong>
        </a>
      `;
    }).join('');

    results.classList.add('show');
  });

  // Close on click outside
  document.addEventListener('click', e => {
    if (!e.target.closest('.header-search')) {
      results.classList.remove('show');
    }
  });

  // Close on escape key
  input.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      results.classList.remove('show');
      input.blur();
    }
  });
}