# Deploying 11woodward.co.nz

The site is plain static files. Any static host works (GitHub Pages, Netlify,
Cloudflare Pages, S3+CloudFront). The repo is already set up for **GitHub Pages**,
which is how the source site was hosted.

---

## Option A — GitHub Pages (recommended, matches the source setup)

### 1. Push the repository

```bash
cd path/to/11woodward.co.nz
git add -A
git commit -m "Migrate pokiesrealmoney.co.com build to 11woodward.co.nz"
git push origin main
```

Set the remote to your GitHub repo, e.g. `git remote set-url origin git@github.com:<account>/11woodward.co.nz.git`.

### 2. Enable Pages

GitHub repo → **Settings → Pages**:

- **Source:** Deploy from a branch
- **Branch:** `main` / `/ (root)`
- Save.

The `CNAME` file (already in the repo, contains `11woodward.co.nz`) tells Pages the
custom domain. The `.nojekyll` file disables Jekyll processing so the site is served
exactly as-is.

### 3. DNS

At your domain registrar / DNS provider for `11woodward.co.nz`, create:

| Type  | Host / Name | Value |
|-------|-------------|-------|
| A     | `@`         | `185.199.108.153` |
| A     | `@`         | `185.199.109.153` |
| A     | `@`         | `185.199.110.153` |
| A     | `@`         | `185.199.111.153` |
| AAAA  | `@`         | `2606:50c0:8000::153` |
| AAAA  | `@`         | `2606:50c0:8001::153` |
| AAAA  | `@`         | `2606:50c0:8002::153` |
| AAAA  | `@`         | `2606:50c0:8003::153` |
| CNAME | `www`       | `<account>.github.io.` |

(If your DNS provider does not allow A records on the apex, use its ALIAS/ANAME
feature pointing to `<account>.github.io`, or move DNS to Cloudflare.)

### 4. HTTPS

Back in **Settings → Pages**, once DNS resolves, tick **Enforce HTTPS**. GitHub
provisions the Let's Encrypt certificate automatically (can take up to ~1 hour).

### 5. Verify

- <https://11woodward.co.nz/> loads
- <https://11woodward.co.nz/online-pokies/> and the other 15 routes load
- <https://11woodward.co.nz/sitemap.xml> and `/robots.txt` load
- `http://` and `www.` both redirect to `https://11woodward.co.nz`

---

## Option B — Netlify / Cloudflare Pages

1. Connect the GitHub repo.
2. Build command: **none**. Publish directory: **`.`** (repo root).
3. Add custom domain `11woodward.co.nz` in the host's dashboard and follow its DNS
   instructions. Delete the `CNAME` file if you use Netlify (it uses its own domain
   config and the file can confuse it); keep it for Cloudflare Pages.

---

## Post-deploy checklist

- [ ] Submit `https://11woodward.co.nz/sitemap.xml` in Google Search Console (add the
      property first, verify by DNS TXT).
- [ ] Set up the `hello@11woodward.co.nz` mailbox or a forwarder — it is printed on
      the contact page and in the Organization JSON-LD but does not exist yet.
- [ ] Decide what the contact form should do (see "Known gaps" in the migration
      report) — it currently posts to `#` and does nothing.
- [ ] Replace placeholder operator rows / logos / affiliate links before promoting.
- [ ] If the old domain `pokiesrealmoney.co.com` stays live, add 301 redirects from
      it to the matching paths on `11woodward.co.nz` to preserve any SEO equity, and
      set a cross-domain canonical. If it is being retired, leave it to lapse.

---

## Making a site-wide change later

There is no template layer — the nav/hero/footer HTML is duplicated in all 17
pages. To change something everywhere:

```bash
# preview which files contain the string
grep -rl 'OLD STRING' --include='*.html' .

# apply
find . -name '*.html' -not -path './.git/*' -print0 \
  | while IFS= read -r -d '' f; do perl -0777 -pi -e 's/OLD STRING/NEW STRING/g' "$f"; done
```
