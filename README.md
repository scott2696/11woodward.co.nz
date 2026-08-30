# 11woodward.co.nz

Independent New Zealand guide to real money online pokies and casinos.
Static HTML site, migrated 1:1 from the `pokiesrealmoney.co.com` build.

## Stack

- **Static HTML** — one `index.html` per route, clean URLs (`/about/`, `/online-pokies/`, …). No build step, no server, no database.
- **[Tailwind CSS](https://tailwindcss.com/) via Play CDN** (`cdn.tailwindcss.com?plugins=forms,container-queries`) with an inline `tailwind.config` (Material Design 3 colour tokens, "Work Sans" type scale) in the `<head>` of every page.
- **Google Fonts** — Work Sans + Material Symbols Outlined.
- **JavaScript** — none, except one inline `onclick` that toggles the mobile nav.
- **Hosting** — GitHub Pages, custom domain via `CNAME`.

## Local preview

No tooling required. Serve the folder with any static server:

```bash
python3 -m http.server 8000
# or: npx serve .
```

Then open <http://localhost:8000>. (Opening the files directly with `file://` also works, but the root-absolute links like `/about/` will not resolve — use a server.)

## Structure

```
.
├── index.html                     # Home — Best Online Pokies NZ
├── online-pokies/index.html       # Pillar: online pokies
├── online-casinos/index.html      # Pillar: online casinos
│   └── bonuses/index.html         # Casino bonuses
├── sports-betting/index.html
├── crypto-casinos/index.html
├── high-payout-casinos/index.html
├── fast-payout-casinos/index.html
├── live-casinos/index.html
├── no-deposit-casinos/index.html
├── about/index.html
├── contact/index.html             # Contact form is a placeholder (action="#")
├── authors/index.html
├── responsible-gambling/index.html
├── terms/index.html
├── privacy/index.html
├── cookies/index.html
├── favicon.svg · favicon.ico · favicon-16x16.png · favicon-32x32.png · apple-touch-icon.png
├── robots.txt
├── sitemap.xml                    # 17 URLs
├── feed.xml                       # RSS 2.0
├── CNAME                          # 11woodward.co.nz
├── CONTENT-BRIEFS.md              # internal editorial briefs (not published)
└── SEO-COMPETITOR-ANALYSIS.md     # internal notes (not published)
```

## Editing content

Every page is self-contained. The shared chrome (top nav, hero band, footer) is copy-pasted into each file — if you change a nav link, change it in all 17 files. A `grep -rl 'old text' --include='*.html' .` then a `perl -pi -e` sweep is the practical way to make a site-wide edit.

The affiliate tables and "Editor's Choice" cards are **neutral placeholders** ("Operator 01", "Bonus placeholder"). Swap in real operator data, logos and affiliate links before any promotion.

## Deploy

See [DEPLOY.md](DEPLOY.md).
