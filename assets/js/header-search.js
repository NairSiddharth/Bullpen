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

      data.forEach((doc, i) => {
        doc.id = i;
        this.add(doc);
        store[i] = doc;
      });
    });
  });

const input = document.getElementById('header-search-input');
const results = document.getElementById('header-search-results');

input.addEventListener('input', () => {
  const query = input.value.trim();

  if (!query || !index) {
    results.style.display = 'none';
    return;
  }

  const matches = index.search(query).slice(0, 5);

  if (!matches.length) {
    results.innerHTML = '<li>No results</li>';
    results.style.display = 'block';
    return;
  }

  results.innerHTML = matches.map(match => {
    const item = store[match.ref];
    return `
      <li>
        <a href="${item.url}">
          <strong>${item.title}</strong>
        </a>
      </li>
    `;
  }).join('');

  results.style.display = 'block';
});

// Close on click outside
document.addEventListener('click', e => {
  if (!e.target.closest('.header-search')) {
    results.style.display = 'none';
  }
});
