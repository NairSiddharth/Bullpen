let index;
let store;
let currentCategory;

// Get category from page title or data attribute
function getCurrentCategory() {
  const banner = document.querySelector('.holo-title');
  if (banner) {
    return banner.textContent.trim().toLowerCase();
  }
  return null;
}

fetch(window.SITE_CONFIG.searchJsonPath)
  .then(res => res.json())
  .then(data => {
    store = {};
    currentCategory = getCurrentCategory();
    
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

const input = document.getElementById('category-search-input');
const results = document.getElementById('category-search-results');

if (input && results) {
  input.addEventListener('input', () => {
    const query = input.value.trim();

    if (!query || !index) {
      results.style.display = 'none';
      return;
    }

    const matches = index.search(query);
    
    // Filter by current category
    const categoryMatches = matches.filter(match => {
      const item = store[match.ref];
      if (!item.categories) return false;
      
      const itemCategories = Array.isArray(item.categories) 
        ? item.categories 
        : [item.categories];
      
      return itemCategories.some(cat => 
        cat.toLowerCase().includes(currentCategory)
      );
    }).slice(0, 5);

    if (!categoryMatches.length) {
      results.innerHTML = '<div class="search-result">No results in this category</div>';
      results.style.display = 'block';
      return;
    }

    results.innerHTML = categoryMatches.map(match => {
      const item = store[match.ref];
      return `
        <a href="${item.url}" class="search-result">
          <strong>${item.title}</strong>
        </a>
      `;
    }).join('');

    results.style.display = 'block';
  });

  // Close on click outside
  document.addEventListener('click', e => {
    if (!e.target.closest('.category-search')) {
      results.style.display = 'none';
    }
  });

  // Close on escape key
  input.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      results.style.display = 'none';
      input.blur();
    }
  });
}