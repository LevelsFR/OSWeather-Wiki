#!/usr/bin/env python3
"""Build a static bilingual wiki from THIS PUBLIC REPOSITORY's Markdown only."""
from __future__ import annotations
import html
import json
import re
import shutil
import unicodedata
from pathlib import Path
import mistune

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
SLUGS = [
    "index", "installation", "compatibility", "features", "commands",
    "configuration", "release-status", "api-v1", "api-overrides",
    "api-dimensions", "api-examples", "faq", "support", "rights",
]
LABELS = {
    "en": [
        "Overview", "Installation", "Compatibility", "Weather system",
        "Commands", "Configuration", "Release status", "Public API v1",
        "Weather overrides", "Dimension providers", "Integration examples",
        "FAQ", "Report a bug", "License and permissions"
    ],
    "fr": [
        "Accueil", "Installation", "Compatibilité", "Système météo",
        "Commandes", "Configuration", "Statut de sortie", "API publique v1",
        "Overrides météo", "Providers de dimensions", "Exemples d’intégration",
        "FAQ", "Signaler un bug", "Licence et autorisations"
    ],
}
GROUPS = [
    ("Information", "Informations", SLUGS[0:7]),
    ("Public API v1", "API publique v1", SLUGS[7:11]),
    ("Help & legal", "Assistance et droits", SLUGS[11:14]),
]

def slugify(raw: str) -> str:
    text = unicodedata.normalize("NFKD", raw)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "section"

class WikiRenderer(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__(escape=True)
        self.headings: list[tuple[int,str,str]] = []
        self.used_ids: dict[str,int] = {}

    def heading(self, text: str, level: int, **attrs: object) -> str:
        label = html.unescape(re.sub(r"<[^>]*>", "", text))
        anchor = slugify(label)
        n = self.used_ids.get(anchor, 0)
        self.used_ids[anchor] = n + 1
        if n:
            anchor += "-" + str(n)
        if level in (2,3):
            self.headings.append((level, label, anchor))
        return f'<h{level} id="{anchor}">{text}</h{level}>\n'

    def link(self, text: str, url: str, title: str | None = None) -> str:
        # Relative Markdown links become public static HTML page links.
        if not (url.startswith("https://") or url.startswith("http://") or url.startswith("#")):
            url = re.sub(r"\.md(?=#|$)", ".html", url)
        return super().link(text, url, title)

def escape(value: str) -> str:
    return html.escape(value, quote=True)


def nav_html(language: str, selected: str) -> str:
    """Render the same collapsible <details> navigation structure as Cobblemon Realms Wiki."""
    output: list[str] = []
    for group_index, (en_group, fr_group, keys) in enumerate(GROUPS):
        group = fr_group if language == "fr" else en_group
        links: list[str] = []
        for key in keys:
            label = LABELS[language][SLUGS.index(key)]
            is_active = key == selected
            current = ' class="active" aria-current="page"' if is_active else ""
            links.append(f'<li style="--depth:0"><a href="{key}.html"{current}>{escape(label)}</a></li>')
        open_attr = " open" if selected in keys or group_index < 3 else ""
        output.append(
            f'<details class="nav-group"{open_attr}>'
            f'<summary><span>{escape(group)}</span><span class="nav-chevron" aria-hidden="true"></span></summary>'
            f'<ul>{"".join(links)}</ul></details>'
        )
    return "\n".join(output)

def page_html(language: str, page: str, body: str, headings: list[tuple[int,str,str]]) -> str:
    french = language == "fr"
    assetbase = "../" if french else ""
    switch = f'../{page}.html' if french else f'fr-FR/{page}.html'
    switch_label = "EN" if french else "FR"
    label = LABELS[language][SLUGS.index(page)]
    heading_links = "".join(
        f'<a class="toc-depth-{level}" href="#{escape(anchor)}">{escape(title)}</a>'
        for level, title, anchor in headings
    )
    toc_label = "Sur cette page" if french else "On this page"
    search_placeholder = "Rechercher dans le wiki…" if french else "Search the wiki…"
    menu_label = "Ouvrir le menu" if french else "Open menu"
    issue_label = "Signaler un bug" if french else "Report a bug"
    footer_label = "Dépôt source privé · Tous droits réservés" if french else "Private source · All Rights Reserved"
    theme_label = "Changer le thème" if french else "Change theme"
    return f"""<!doctype html>
<html lang="{language}" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#191919">
<meta name="description" content="Official OS Weather public documentation, installation and API v1 reference.">
<title>{escape(label)} | OS Weather Wiki</title>
<link rel="icon" type="image/svg+xml" href="{assetbase}assets/weather.svg">
<link rel="manifest" href="{assetbase}site.webmanifest">
<link rel="stylesheet" href="{assetbase}assets/wiki.css">
<link rel="stylesheet" href="{assetbase}assets/wiki-enhancements.css">
<link rel="stylesheet" href="{assetbase}assets/osweather-custom.css">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem("osweather-wiki-theme")==="light"?"light":"dark"}}catch(e){{}}</script>
<script defer src="{assetbase}assets/wiki.js"></script>
</head>
<body data-root="{assetbase}" data-language="{language}">
<div id="reading-progress" class="reading-progress" aria-hidden="true"><span></span></div>
<header class="topbar">
    <button id="menu-button" class="menu-button" type="button" aria-label="{menu_label}">☰</button>
    <a class="brand" href="index.html" aria-label="OS Weather Wiki">
      <span class="brand-copy"><strong>OS Weather <span class="brand-version">v0.9</span></strong><small>Wiki</small></span>
    </a>
    <div class="search-wrap">
      <span class="search-icon" aria-hidden="true"></span>
      <input id="search" type="search" autocomplete="off" spellcheck="false" placeholder="{search_placeholder}" aria-label="{search_placeholder}" aria-controls="search-results" aria-expanded="false">
      <kbd>Ctrl K</kbd>
      <div id="search-results" class="search-results" role="listbox" hidden></div>
    </div>
    <div class="header-tools">
      <a class="issues-link" href="https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose" target="_blank" rel="noopener noreferrer">{issue_label}</a>
      <a class="language" href="{switch}" aria-label="Change language">{switch_label}</a>
      <button type="button" id="theme-toggle" class="theme-toggle" aria-label="{theme_label}" title="{theme_label}">
        <span class="theme-icon theme-icon-sun" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"></path></svg></span>
        <span class="theme-icon theme-icon-moon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.5 14.2A8.5 8.5 0 0 1 9.8 3.5 8.5 8.5 0 1 0 20.5 14.2Z"></path></svg></span>
      </button>
    </div>
</header>
<div id="overlay" class="os-overlay"></div>
<div class="layout">
  <nav id="sidebar" class="sidebar" aria-label="Wiki navigation">
    <div class="sidebar-navigation">{nav_html(language, page)}</div>
    <footer class="sidebar-credits" aria-label="Wiki credits">
      <div class="sidebar-credits-title"><span class="sidebar-credits-mark">O</span><span>OS Weather Wiki</span></div>
      <div class="sidebar-credit-person"><strong>LevelsFR</strong><small>OS Weather</small></div>
      <div class="sidebar-credit-person"><small>{footer_label}</small></div>
      <div class="sidebar-credit-person"><a href="https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose">{issue_label} ↗</a></div>
    </footer>
  </nav>
  <main>
    <article>
      {body}
      <footer class="article-meta">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="8.5"></circle><path d="M12 7v5l3 2"></path></svg>
        <span>OS Weather 0.9.0-beta.10.5 · API v1 · {footer_label}</span>
      </footer>
    </article>
  </main>
  <aside id="page-toc" class="page-toc" aria-label="{toc_label}">
    <strong class="page-toc-title">{toc_label}</strong>
    <nav>{heading_links}</nav>
  </aside>
</div>
<button id="back-to-top" class="back-to-top" type="button" aria-label="Back to top" title="Back to top">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 14 6-6 6 6"></path></svg>
</button>
</body>
</html>"""

def build() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    (OUTPUT / "assets").mkdir(parents=True)
    (OUTPUT / "fr-FR").mkdir()
    shutil.copyfile(ROOT / "web" / "wiki.css", OUTPUT / "assets" / "wiki.css")
    shutil.copyfile(ROOT / "web" / "wiki-enhancements.css", OUTPUT / "assets" / "wiki-enhancements.css")
    shutil.copyfile(ROOT / "web" / "osweather-custom.css", OUTPUT / "assets" / "osweather-custom.css")
    shutil.copyfile(ROOT / "web" / "wiki.js", OUTPUT / "assets" / "wiki.js")
    shutil.copyfile(ROOT / "web" / "weather.svg", OUTPUT / "assets" / "weather.svg")
    index: list[dict[str,str]] = []
    for language in ("en", "fr"):
        out_folder = OUTPUT if language == "en" else OUTPUT / "fr-FR"
        for slug in SLUGS:
            source = ROOT / "content" / language / f"{slug}.md"
            raw = source.read_text(encoding="utf-8")
            renderer = WikiRenderer()
            md = mistune.create_markdown(renderer=renderer, plugins=["table", "strikethrough", "url"])
            article = md(raw)
            # Only authored, approved Markdown from this public repository is rendered.
            document = page_html(language, slug, article, renderer.headings)
            (out_folder / f"{slug}.html").write_text(document, encoding="utf-8")
            index.append({
                "title": LABELS[language][SLUGS.index(slug)],
                "lang": language,
                "url": ("fr-FR/" if language == "fr" else "") + slug + ".html",
                "text": re.sub(r"\\s+", " ", raw)[:6500],
            })
    (OUTPUT / "search-index.json").write_text(
        json.dumps(index, ensure_ascii=False, separators=(",",":")), encoding="utf-8"
    )
    (OUTPUT / "index.html").exists() or (_ for _ in ()).throw(RuntimeError("No home page"))
    (OUTPUT / "404.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>404 | OS Weather Wiki</title><link rel="stylesheet" href="assets/wiki.css">'
        '<main style="max-width:700px;margin:15vh auto;padding:30px">'
        '<h1>Page not found</h1><p>This documentation page does not exist.</p>'
        '<a href="index.html">Back to the OS Weather Wiki</a></main></html>',
        encoding="utf-8"
    )
    (OUTPUT / "site.webmanifest").write_text(
        json.dumps({
            "name": "OS Weather Wiki", "short_name": "OS Weather",
            "start_url": "./", "scope": "./", "display": "standalone",
            "background_color": "#191919", "theme_color": "#191919",
            "icons": [{"src":"assets/weather.svg","sizes":"any","type":"image/svg+xml"}]
        }, indent=2), encoding="utf-8"
    )
    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUTPUT / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print(f"Generated {len(index)} multilingual pages and {len(list(OUTPUT.rglob('*')))} outputs")

if __name__ == "__main__":
    build()
