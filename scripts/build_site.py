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
    output = []
    for en_group, fr_group, keys in GROUPS:
        group = fr_group if language == "fr" else en_group
        links = []
        for key in keys:
            label = LABELS[language][SLUGS.index(key)]
            is_active = key == selected
            current = ' aria-current="page"' if is_active else ""
            active_class = ' class="active"' if is_active else ""
            links.append(f'<a href="{key}.html"{active_class}{current}><span class="nav-dot" aria-hidden="true"></span>{escape(label)}</a>')
        output.append(f'<section class="side-group"><div class="side-group-title">{escape(group)}</div>{"".join(links)}</section>')
    return "".join(output)

def page_html(language: str, page: str, body: str, headings: list[tuple[int,str,str]]) -> str:
    is_fr = language == "fr"
    base = "../" if is_fr else ""
    switch = f'../{page}.html' if is_fr else f'fr-FR/{page}.html'
    switch_label = "English" if is_fr else "Français"
    label = LABELS[language][SLUGS.index(page)]
    index = SLUGS.index(page)
    previous = SLUGS[index - 1] if index else None
    next_page = SLUGS[index + 1] if index + 1 < len(SLUGS) else None
    back = "Précédent" if is_fr else "Previous"
    forward = "Suivant" if is_fr else "Next"
    search_label = "Rechercher dans le wiki…" if is_fr else "Search the wiki…"
    toc_label = "Sur cette page" if is_fr else "On this page"
    issue_label = "Signaler un problème ↗" if is_fr else "Report an issue ↗"
    nav = nav_html(language, page)
    toc = "".join(
        f'<a class="toc-depth-{level}" href="#{escape(anchor)}">{escape(title)}</a>'
        for level, title, anchor in headings
    )
    prev_link = f'<a href="{previous}.html"><small>{back}</small>{escape(LABELS[language][index-1])}</a>' if previous else "<span></span>"
    next_link = f'<a href="{next_page}.html"><small>{forward}</small>{escape(LABELS[language][index+1])}</a>' if next_page else "<span></span>"
    return f"""<!doctype html>
<html lang="{language}" data-theme="dark">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="OS Weather public mod and API v1 documentation">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#191919">
<title>{escape(label)} | OS Weather Wiki</title>
<link rel="icon" type="image/svg+xml" href="{base}assets/weather.svg">
<link rel="manifest" href="{base}site.webmanifest">
<link rel="stylesheet" href="{base}assets/wiki.css">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('osweather-wiki-theme')==='light'?'light':'dark'}}catch(e){{}}</script>
<script defer src="{base}assets/wiki.js"></script>
</head>
<body data-root="{base}" data-language="{language}">
<header class="topbar">
<button id="menu-button" class="menu-button" type="button" aria-label="Toggle navigation">☰</button>
<a class="brand" href="index.html"><img src="{base}assets/weather.svg" alt="" width="35" height="35"><span><strong>OS WEATHER</strong><small>Official Wiki · API v1</small></span></a>
<div class="search-wrap"><span class="search-icon" aria-hidden="true">⌕</span><input id="search" type="search" placeholder="{search_label}" aria-label="{search_label}" autocomplete="off" aria-expanded="false"><kbd>Ctrl K</kbd><div class="search-results" id="search-results" hidden></div></div>
<div class="top-actions"><a class="issues-top" href="https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose" rel="noopener noreferrer">Issues ↗</a><a class="language" href="{switch}">{switch_label}</a><button type="button" id="theme-toggle" aria-label="Toggle dark and light mode">◐</button></div>
</header>
<div class="overlay" id="overlay"></div>
<div class="layout">
<aside id="sidebar" class="sidebar"><p class="sidebar-subtitle">DOCUMENTATION · 0.9 BETA</p>{nav}
<footer class="sidebar-footer"><strong>LevelsFR</strong><div>OS Weather · All Rights Reserved</div><div>Private source code</div><a href="https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose">{issue_label}</a></footer>
</aside>
<main class="main"><div class="article">
<nav class="breadcrumbs"><a href="index.html">OS Weather Wiki</a><span>›</span><span>{escape(label)}</span></nav>
<div class="meta"><span class="tag beta">BETA 0.9.0</span><span class="tag api">API v1</span><span class="tag loader">Fabric · NeoForge</span></div>
<article class="markdown-body">{body}</article>
<div class="page-navigation">{prev_link}{next_link}</div>
<footer class="page-footer"><span>© 2026 LevelsFR · All Rights Reserved</span><span>Public documentation · Proprietary source</span></footer>
</div></main>
<aside class="toc"><div class="toc-title">{toc_label}</div><nav>{toc}</nav></aside>
</div>
</body></html>"""

def build() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    (OUTPUT / "assets").mkdir(parents=True)
    (OUTPUT / "fr-FR").mkdir()
    shutil.copyfile(ROOT / "web" / "wiki.css", OUTPUT / "assets" / "wiki.css")
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
