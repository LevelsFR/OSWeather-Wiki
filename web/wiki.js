(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const body = document.body;
  const root = body.dataset.root || '';
  const lang = body.dataset.language || 'en';
  const menu = $('menu-button');
  const overlay = $('overlay');
  const theme = $('theme-toggle');
  menu?.addEventListener('click', () => body.classList.toggle('menu-open'));
  overlay?.addEventListener('click', () => body.classList.remove('menu-open'));
  document.querySelectorAll('.sidebar a').forEach(a => a.addEventListener('click', () => body.classList.remove('menu-open')));
  theme?.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('osweather-wiki-theme', next); } catch {}
  });
  document.querySelectorAll('pre').forEach(pre => {
    const button = document.createElement('button');
    button.className = 'copy-code';
    button.type = 'button';
    button.textContent = lang === 'fr' ? 'Copier' : 'Copy';
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(pre.querySelector('code')?.textContent || pre.textContent);
        button.textContent = lang === 'fr' ? 'Copié !' : 'Copied!';
        button.setAttribute('aria-label', 'Copied');
      } catch {
        button.textContent = lang === 'fr' ? 'Sélectionner le code' : 'Select text';
      }
    });
    pre.append(button);
  });
  const search = $('search');
  const results = $('search-results');
  let index = [];
  fetch(root + 'search-index.json')
    .then(response => {
      if (!response.ok) throw new Error('Search unavailable');
      return response.json();
    })
    .then(data => { index = Array.isArray(data) ? data : []; })
    .catch(() => {});
  const close = () => {
    if (!results) return;
    results.hidden = true;
    results.replaceChildren();
    search?.setAttribute('aria-expanded', 'false');
  };
  function draw() {
    if (!search || !results) return;
    const term = search.value.trim().toLocaleLowerCase(lang);
    results.replaceChildren();
    if (term.length < 2) { close(); return; }
    const scored = index
      .filter(entry => entry.lang === lang)
      .map(entry => ({entry, weight:
        (entry.title.toLocaleLowerCase(lang).includes(term) ? 20 : 0) +
        (entry.text.toLocaleLowerCase(lang).includes(term) ? 2 : 0)}))
      .filter(item => item.weight > 0)
      .sort((a,b) => b.weight-a.weight)
      .slice(0, 9);
    if (!scored.length) {
      const empty = document.createElement('div');
      empty.className = 'search-empty';
      empty.textContent = lang === 'fr' ? 'Aucun résultat' : 'No results';
      results.append(empty);
    }
    scored.forEach(({entry}) => {
      const a = document.createElement('a');
      a.href = root + entry.url;
      a.textContent = entry.title;
      const sub = document.createElement('small');
      sub.textContent = entry.text.replace(/[#*|_`]/g, ' ').slice(0,110);
      a.append(sub);
      results.append(a);
    });
    results.hidden = false;
    search.setAttribute('aria-expanded','true');
  }
  search?.addEventListener('input', draw);
  search?.addEventListener('keydown', e => {
    if (e.key === 'Escape') { close(); search.blur(); }
    if (e.key === 'Enter') {
      const first = results?.querySelector('a');
      if (first) location.href = first.href;
    }
  });
  document.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault(); search?.focus(); search?.select();
    }
    if (e.key === 'Escape') body.classList.remove('menu-open');
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('.search-wrap')) close();
  });

  // Match the reference wiki's reading progress and back-to-top interactions.
  const progress = document.querySelector('#reading-progress span');
  const toTop = $('back-to-top');
  function updateScrollUI() {
    const height = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const ratio = Math.max(0, Math.min(1, window.scrollY / height));
    if (progress) progress.style.width = String(Math.round(ratio * 10000) / 100) + '%';
    document.body.classList.toggle('long-article', height > 450);
    toTop?.classList.toggle('is-visible', window.scrollY > 400);
  }
  addEventListener('scroll', updateScrollUI, {passive:true});
  addEventListener('resize', updateScrollUI);
  updateScrollUI();
  toTop?.addEventListener('click', () => scrollTo({top:0,behavior:'smooth'}));
  const asideToc = $('page-toc');
  if (asideToc && !asideToc.querySelector('a')) asideToc.hidden = true;
  // Preserve the reference wiki's nav position between documentation pages.
  const sidebar = $('sidebar');
  const sidebarKey = 'osweather-sidebar-scroll:' + lang;
  try {if (sidebar) sidebar.scrollTop=Number(sessionStorage.getItem(sidebarKey)||0);}catch{}
  sidebar?.addEventListener('scroll',()=>{try{sessionStorage.setItem(sidebarKey,String(sidebar.scrollTop))}catch{}},{passive:true});

})();
