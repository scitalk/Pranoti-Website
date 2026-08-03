(function () {
  var input = document.getElementById('search-input');
  var resultsEl = document.getElementById('search-results');
  var statusEl = document.getElementById('search-status');
  var suggestionsEl = document.getElementById('search-suggestions');
  if (!input || !resultsEl) return;

  var MAX_SUGGESTIONS = 12;

  var SECTION_LABELS = {
    'ai-guides': 'AI Guide',
    'perspectives': 'Perspectives',
    'case-studies': 'Case Study',
    'portfolio': 'Portfolio'
  };

  var index = null;

  function loadIndex() {
    return fetch('/index.json')
      .then(function (res) { return res.json(); })
      .then(function (data) {
        index = data;
        renderSuggestions();
      });
  }

  function renderSuggestions() {
    if (!suggestionsEl || !index) return;

    var counts = {};
    index.forEach(function (item) {
      (item.tags || []).forEach(function (tag) {
        counts[tag] = (counts[tag] || 0) + 1;
      });
    });

    var topTags = Object.keys(counts)
      .sort(function (a, b) { return counts[b] - counts[a]; })
      .slice(0, MAX_SUGGESTIONS);

    if (!topTags.length) return;

    suggestionsEl.innerHTML = '';

    var label = document.createElement('span');
    label.className = 'search-suggestions-label';
    label.textContent = 'Try:';
    suggestionsEl.appendChild(label);

    topTags.forEach(function (tag) {
      var chip = document.createElement('button');
      chip.type = 'button';
      chip.className = 'search-chip';
      chip.textContent = tag;
      chip.addEventListener('click', function () {
        input.value = tag;
        input.focus();
        statusEl.textContent = 'Loading search index...';
        loadIndex().then(function () { render(tag); });
      });
      suggestionsEl.appendChild(chip);
    });
  }

  function score(item, terms) {
    var haystacks = [
      { text: (item.title || '').toLowerCase(), weight: 3 },
      { text: (item.keywords || []).join(' ').toLowerCase(), weight: 2 },
      { text: (item.tags || []).join(' ').toLowerCase(), weight: 2 },
      { text: (item.description || '').toLowerCase(), weight: 1 }
    ];
    var total = 0;
    terms.forEach(function (term) {
      haystacks.forEach(function (h) {
        if (h.text.indexOf(term) !== -1) total += h.weight;
      });
    });
    return total;
  }

  function render(query) {
    var q = query.trim().toLowerCase();
    resultsEl.innerHTML = '';

    if (suggestionsEl) suggestionsEl.style.display = q ? 'none' : '';

    if (!q) {
      statusEl.textContent = '';
      return;
    }

    var terms = q.split(/\s+/).filter(Boolean);
    var matches = index
      .map(function (item) { return { item: item, score: score(item, terms) }; })
      .filter(function (m) { return m.score > 0; })
      .sort(function (a, b) { return b.score - a.score; });

    statusEl.textContent = matches.length
      ? matches.length + ' result' + (matches.length === 1 ? '' : 's') + ' for "' + query + '"'
      : 'No results for "' + query + '"';

    matches.forEach(function (m) {
      var item = m.item;
      var card = document.createElement('article');
      card.className = 'post-card';

      var link = document.createElement('a');
      link.href = item.url;

      var label = document.createElement('span');
      label.className = 'search-result-tag';
      label.textContent = SECTION_LABELS[item.section] || item.section;

      var h2 = document.createElement('h2');
      h2.textContent = item.title;

      var excerpt = document.createElement('p');
      excerpt.className = 'excerpt';
      excerpt.textContent = item.description;

      link.appendChild(label);
      link.appendChild(h2);
      link.appendChild(excerpt);
      card.appendChild(link);
      resultsEl.appendChild(card);
    });
  }

  var debounceTimer;
  input.addEventListener('input', function () {
    clearTimeout(debounceTimer);
    var value = input.value;
    debounceTimer = setTimeout(function () {
      if (!index) {
        statusEl.textContent = 'Loading search index...';
        loadIndex().then(function () { render(value); });
      } else {
        render(value);
      }
    }, 150);
  });

  var params = new URLSearchParams(window.location.search);
  var initialQuery = params.get('q');
  if (initialQuery) {
    input.value = initialQuery;
    statusEl.textContent = 'Loading search index...';
    loadIndex().then(function () { render(initialQuery); });
  } else {
    loadIndex();
  }
})();
