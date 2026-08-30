# SERP Competitor & Content-Gap Analysis — 11woodward.co.nz

**Market:** New Zealand (en-NZ) · **Date:** 27 August 2026
**Scope:** All 10 money pages, analysed against live NZ SERP competitors with AU/UK/US/CA benchmarking.
**Method:** WebSearch (NZ primary + one mature-market comparative per page) + WebFetch of top-ranking pages. WebSearch is US-endpointed, so positions are approximate organic order, not rank-tracker verified. Fetch failures (HTTP 403) are logged inline and never fabricated.

---

## Executive summary — the 8 cross-cutting findings

1. **The NZ Online Casino Gambling Act 2026 is an open moat.** Only casino.org covers the new licensing regime, and shallowly. No competitor leads with penalties (up to NZD 5m body corporate / NZD 300k individual), the EOI fee (~NZD 19,000 + GST), the September 2026 auction, licences early 2027, or the offshore transition cut-off. **⚠ Date to verify before publish:** our site states a **1 Dec 2026** application deadline; some competitor sources imply an offshore-access wind-down into **mid-2027**. Confirm the exact statutory dates against DIA before this goes live.
2. **NZD-native banking + payout timing in NZ business days is universally weak.** The two strongest pages (casino.org, gambling.com) omit local banking rails entirely; everyone quotes vague "1–3 days." **Note:** POLi was discontinued in 2022 — several competitors still cite it incorrectly. Lead with NZD bank transfer, e-wallets, Paysafecard, crypto, and measured NZ-business-day payout ranges.
3. **Schema is under-deployed across the whole SERP.** Review/AggregateRating/ItemList/FAQPage JSON-LD is largely absent even on #1 pages. We already ship FAQPage + Breadcrumb + Organization; adding Review/AggregateRating on operator rows (post-affiliate) is an uncontested rich-result win.
4. **Wagering math is the bonus-page wedge.** Top rankers show zero (gambling.com) or one (casino.org) worked example. Per-offer NZD wagering math (deposit → ×WR → total-to-wager → realistic clear time) beats them on their weakest axis.
5. **Nobody publishes measured payout times or verifiable RTP.** Audit bodies (eCOGRA/iTech/GLI) are name-dropped but never evidenced with a certificate ID; payout speeds are ranges, never measured. A page with reproducible numbers out-E-E-A-Ts the entire first page.
6. **"Honesty about the catch" converts.** No-deposit max-cashout caps in NZD and live-table bonus-contribution % are buried everywhere except casino.org. Our pages already lean honest — reinforce with concrete NZD figures.
7. **Named-expert E-E-A-T + a hard update date beats the parasites.** Multiple ranking "competitors" are parasite/expired-domain content mills (nzhistory.net.nz, carbonklean.com, torontoguardian.com, glmshows.com) renting authority. Credentialed bylines + visible dates + genuine testing beat them structurally.
8. **Spoke expansion is wide open.** Min-deposit ($1/$5/$10) pokie pages, no-KYC + per-coin crypto pages, and per-sport racing/rugby/NRL pages are absent or thin across NZ competitors and map cleanly to our pillar structure.

---

## Master opportunity roadmap (scored, consistent T×E×R ÷ 10)

Scoring = Traffic Potential × Ranking Ease × Affiliate Revenue (each 0–10), product normalised to /100.

### Quick wins (0–30 days) — meta, schema, depth on existing pages

| Opportunity | Page | T | E | R | Score | Action |
|---|---|---|---|---|---|---|
| Per-offer NZD wagering-math column | /online-casinos/bonuses/ | 9 | 8 | 9 | **65** | Add deposit→×WR→total→clear-time into the money table, not a separate explainer |
| Measured payout table in NZ business days | /fast-payout-casinos/ | 9 | 7 | 9 | **57** | Add tested submit→approve→land columns per operator |
| Max-cashout caps stated in NZD | /no-deposit-casinos/ | 9 | 8 | 7 | **50** | Add "Max cashout (NZD)" + "Wagering on winnings" columns |
| Verifiable RTP table w/ audit cert ID | /high-payout-casinos/ | 8 | 7 | 9 | **50** | Operator, avg RTP %, test lab, cert reference, NZD support |
| Honest TAB-vs-offshore margin comparison | /sports-betting/ | 8 | 7 | 9 | **50** | Side-by-side odds-margin data; everyone else just dismisses TAB |
| NZD banking + payout-in-business-days matrix | / , /online-casinos/ | 7 | 8 | 8 | **45** | Filterable method table; two strongest pages miss it entirely |
| Honest live-bonus wagering explainer | /live-casinos/ | 7 | 9 | 7 | **44** | 10–20% contribution + NZD worked example; unique in NZ SERP |
| Ship Review/AggregateRating schema on rows | all money pages | 6 | 9 | 7 | **38** | Post-affiliate; uncontested rich-result real estate |
| Deepen Gambling Act 2026 module | /online-casinos/, homepage | 8 | 8 | 6 | **38** | Add penalties, EOI fee, auction mechanics, dated + DIA-sourced |

### Medium wins (30–90 days) — new spoke pages

| Opportunity | New URL | T | E | R | Score | Action |
|---|---|---|---|---|---|---|
| No-KYC crypto casinos | /crypto-casinos/no-kyc/ | 8 | 7 | 9 | **50** | High-intent, revenue-rich, competitors avoid it |
| Min-deposit pokies ($1/$5/$10) | /online-pokies/min-deposit/ (+ sub) | 6 | 9 | 8 | **43** | Untapped in both NZ and AU; budget-player capture |
| Per-coin crypto spokes | /crypto-casinos/bitcoin/ etc. | 7 | 7 | 8 | **39** | BTC/USDT/ETH/DOGE coin-level intent → internal-link to hub |
| NZ racing hub | /sports-betting/racing/ | 7 | 7 | 8 | **39** | Horse/harness/greyhound depth rivals ignore |
| Interactive NZD wagering calculator | /online-casinos/bonuses/ asset | 8 | 7 | 8 | **45** | No native-NZD calculator exists; dwell-time + linkable asset |
| Provably-fair explainer + rankings | /crypto-casinos/ | 6 | 8 | 7 | **34** | Explain verification; rank Originals-heavy books |
| "Best new / newest betting sites NZ" | /sports-betting/new/ | 6 | 7 | 7 | **29** | Distinct sub-intent NZ pages don't isolate (UK pattern) |

### Long-term (90–180 days) — authority & original data

| Opportunity | T | E | R | Score | Action |
|---|---|---|---|---|---|
| Per-sport spokes (rugby/NRL/cricket/Black Caps) internal-linked to sports hub | 7 | 6 | 7 | **29** | Funnel topical authority to the money page |
| Hands-on "we tested & withdrew" playtest module w/ named NZ testers | 6 | 6 | 6 | **22** | Experiential E-E-A-T parasites can't fake |
| "Which of the 15 licensed operators" live tracker | 6 | 7 | 5 | **21** | Forward-looking evergreen hook nobody has |
| Crypto-gambling tax NZ explainer (untaxed winnings vs IR disposal on NZD conversion) | 7 | 8 | 6 | **34** | Featured-snippet bait; only one competitor grazes it |

---

## Phase 1 & 2 — per-page competitor breakdown + gaps

_Below: the full competitor tables, gap analysis (a = table-stakes missing, b = weakly covered, c = untapped), and per-page scored opportunities, page by page._

---

### Homepage — "best online pokies real money NZ"

| Domain | Geo | Pos | Intent | Format | ~Words | Affiliate Placement | E-E-A-T | Schema | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|---|---|---|
| casino.org/new-zealand | NZ | 1–2 | Comm+info | Ranked hub + reviews | 8.5–9k | 15-casino table above fold | Named author + fact-checker, dated 22 Aug 2026, 3 RG partners | FAQ, Review, ItemList, Breadcrumb, Org | Best regulatory timeline; named-expert E-E-A-T; "avoid" list | No local banking; payout not in business days; wagering not itemised |
| gambling.com/nz/…/pokies | NZ | 1–3 | Comm+info | Guide + hub | 3.5–4.5k | Table above fold | Dean Ryan, fact-checker, dated Aug 3 | ItemList, Breadcrumb, Review | Brand authority; tournaments angle | Thinnest; NO Gambling Act 2026; no per-game RTP; thin RG |
| casino.guru/new-zealand | Intl/NZ | 3–4 | Comm (DB) | 800+ casino database | n/a | Filter/DB list | Complaint-resolution rep | ItemList, Review, Breadcrumb | Massive DB + complaint service | Generic/global; light NZ banking + law |
| top-online-pokies-nz.co.nz | NZ | 4–6 | Info+trans | Long affiliate guide | 7.5–8.5k | 10-casino table above fold | Author mismatch, **no update date**, strong RG | FAQ, Review, ItemList, Breadcrumb | POLi; realistic withdrawal table; land vs online | No date; references old 2003 Act; NZD/USD mixing |

_Parasite/exploitable: nzhistory.net.nz, thesunpapers.com/nz, carbonklean.com, best-online-pokies-for-nz.com._

**Gaps:** (a) above-fold ranked table w/ logos+bonus+payout+CTA; named author+fact-checker+date; wagering depth; RG section; "how we rate". (b) payout in NZ business days; NZD banking rails; per-game RTP; per-casino wagering. (c) Gambling Act 2026 trust band leading the page; NZD-native banking comparison; RTP-transparency methodology; "which of 15 operators" tracker.

**Top opportunities:** above-fold table w/ min-deposit+wagering columns (63); NZD banking + business-day payout module (49); named-expert E-E-A-T + hard date (34); Act 2026 licensing band (30); per-game high-RTP table (30).

---

### /online-pokies/ — "online pokies NZ"

| Domain | Geo | Pos | Format | ~Words | E-E-A-T | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|
| casino.org/new-zealand/online-pokies | NZ | 1 | Hybrid guide (19 H2s) | 8.5–9.5k | Adam Volz + fact-checker, dated 3 Aug | Best depth; per-game RTPs; providers + free-play + mechanics | No Act 2026; no local banking; payout days unlabelled |
| gambling.com/nz/…/pokies | NZ | 2 | Guide + hub | 3.5–4.5k | Dean Ryan + fact-checker | Brand authority; tournaments | Half the depth; no Act 2026; no per-game RTP |
| top-online-pokies-nz.co.nz | NZ | 3–4 | Long affiliate guide | 7.5–8.5k | No date; author mismatch | POLi + withdrawal business-day table | Stale-signal; leans on 2003 Act |
| esportsinsider.com/nz/…/online-pokies | NZ | 4–6 | Guide | — | **FETCH 403 — not verified** | — | — |
| best-online-pokies-for-nz.com | Intl→NZ | 5–7 | Thin listicle | thin | Anonymous | Exact-match domain | Thin, low-E-E-A-T |

**Gaps:** (a) pokie-type taxonomy; "how pokies work" RNG + volatility; providers; free-play; per-game RTP; FAQ+author+date. (b) named high-RTP pokie table; payout in business days; $1/$5/$10 min-deposit angle; volatility-to-playstyle matching. (c) Act 2026 for pokie players; NZD banking tied to payout timing; certified-RNG methodology; NZD jackpot tracker.

**Top opportunities:** match casino.org depth (43); highest-RTP named-game table (45); min-deposit sub-angle (43); NZD banking + business-day table (49); Act 2026 / which-of-15 module (30).

---

### /online-casinos/ — "best online casino NZ real money"

| Domain | Geo | Pos | Format | ~Words | E-E-A-T | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|
| gambling.com/nz | NZ | ~1 | Category listicle | 3.5–4.5k | Tim Williams, dated, methodology | Strong E-E-A-T; category segmentation; fast-payout emphasis | No Act 2026; no NZD banking; wagering listed not analysed |
| casino.org/new-zealand | NZ | ~2 | Mega-pillar | 12–14k | Head of Casino.org + fact-checker, 25-step method | Best breadth; full legal timeline; playtest; fund-protection | POLi absent; bonuses not value-standardised; "apps rare" stale |
| bettingtop10.co.nz | NZ | ~3–4 | Testing-led listicle | 8.5–9.2k | Named author + fact-checker, dated 24/08 | Local TLD; hands-on testing; flags ANZ/Westpac card declines; tax analysis | No schema; POLi missing; thin promo coverage |
| gamblinginsider.com/nz | NZ | ~2–3 | Listicle | — | **FETCH 403 — not analysed** | — | — |

**Gaps:** (a) POLi/local-rail coverage (most miss it); Product/AggregateRating/ItemList schema; sortable comparison matrix. (b) NZD banking specifics; ANZ/Westpac/BNZ card-decline reality; payout in NZ business days; game-level RTP/volatility; complaint-resolution timeframes; fund protection. (c) full Act 2026 detail (penalties, EOI fee, auction, 1 Dec cut-off, "Registered NZ Operator" badge).

**Top opportunities:** Act 2026 explainer + operator tracker (84 per agent normalisation); ItemList/Product/AggregateRating/FAQ schema (82); sortable NZD banking + business-day matrix (82); category sub-pages (74); hands-on playtest module (68).

---

### /online-casinos/bonuses/ — "casino bonuses NZ"

| Domain | Geo | Pos | Format | ~Words | Wagering math? | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|
| gambling.com/nz/…/bonus | NZ | ~1 | Offer listicle | 0.8–1.2k | **None** | Strong author; POLi; fresh | No math; no max-bet/contribution/expiry/cap; $ ambiguous |
| casino.org/…/bonuses | NZ | ~1–2 | Mega-guide | 8.5–9.5k | **One line** | Breadth; 1-Dec section; RG depth; "avoid" list | Only one wagering example; max-bet buried; POLi missing |
| casinos.com/nz/bonus | NZ | ~2–3 | Guide + cards | 6.5–7k | One example | Clean worked example; cashout caps in FAQ; POLi/Paysafecard | Single-deposit math only; no free-spin value math; no 1-Dec |
| casinoalpha.com/nz/bonuses | NZ | ~2–3 | Analytical guide | 8.5–9.5k | **Best in SERP** | Multiple NZD examples; contribution table; max-bet void rule; cap coverage | No 1-Dec; table buried below 30 cards; UK-flavoured RG (GamStop) |

**Verdict:** Most competitors list headline offers with no math. Only casinos.com (one basic) and CasinoAlpha (deep) show real math; gambling.com shows zero, casino.org one line — the exploitable weakness at the top of the SERP.

**Gaps:** (a) per-offer wagering worked-example column; 1 Dec 2026 context; AggregateOffer/FAQPage schema. (b) max-bet-while-wagering rule; game-contribution % table; free-spin value math; multi-deposit/stacked-package math; cap×wagering interaction. (c) bonuses under the licensed regime; NZD-denominated clarity; bonus-winnings payout in business days; native NZD wagering calculator.

**Top opportunities:** per-offer NZD wagering column (90); native NZD calculator (82); "bonuses under the 1 Dec regime" section (80); free-spin value + cap×wagering examples (78); AggregateOffer/FAQPage schema (78).

---

### /sports-betting/ — "best sports betting sites NZ"

**SERP verdict:** Offshore books dominate organic entirely. TAB NZ (licensed domestic monopoly, exclusive since July 2025 with Betcha) ranks #1 on no affiliate page — everyone frames TAB as the inferior incumbent. Biggest structural fact of the vertical.

| Domain | Geo | Pos | Format | ~Words | Strengths | Weaknesses |
|---|---|---|---|---|---|---|
| bettingtop10.co.nz | NZ | ~1–3 | Ranked list + guide | ~4,500 | NZ TLD; strong author E-E-A-T; explicit "why over TAB" section; fresh | No schema; light justification for offshore #1; shallow racing |
| ofb.nz | NZ | ~4 | Mega-guide (table at bottom) | ~11,500 | Deepest NZ-sport coverage; real-money testing; offshore-legality clarity | **Table buried at bottom** (kills conversion); bloat risk; older date |
| footitalia.com/betting-sites/nz | Intl (NZ subfolder) | ~3–5 | Ranked list + guide | ~8,500 | Good table placement; apps + tips | Non-NZ domain; racing barely covered |
| bookies.com/nz | US-intl | ~4 | Ranked list | — | **FETCH 403** | — |
| oddschecker.com/nz | UK-intl | ~1–2 | Odds-compare tool + list | — | **FETCH 403** (odds-comparison format NZ affiliates lack) | — |

**Gaps:** (a) Review/AggregateRating/FAQ schema (universal miss); odds-comparison functionality. (b) horse/harness/greyhound racing (thin except ofb.nz); NZD banking (POLi dead post-2022); generic apps coverage. (c) honest TAB-vs-offshore margin comparison; per-market spokes (rugby/NRL/cricket/racing); NZD payout speed/withheld-tax clarity; July 2025 TAB+Betcha exclusivity explained.

**Top opportunities:** schema rollout (82); table above fold + honest TAB comparison (80); NZ racing hub (76); per-sport spokes (68); "best new betting sites NZ" (67).

---

### /crypto-casinos/ — "best crypto casino NZ"

| Domain | Geo | Pos | Format | ~Words | Strengths | Weaknesses |
|---|---|---|---|---|---|---|
| casino.org/new-zealand/crypto | Intl authority | ~1–2 | Top-10 + deep guide | 4.5–5k | Strongest E-E-A-T; coin/deposit/withdrawal depth; NZ-specific RG | No crypto-tax section; no 2026 bill |
| torontoguardian.com/…crypto-nz | Intl (parasite) | ~1–3 | Sponsored listicle | — | **FETCH 403** — borrowed news-domain authority | Parasite; crackdown-vulnerable |
| kiwikasino.com/crypto-casinos | NZ | ~3–5 | Table + guide | 3.1–3.4k | NZ TLD; touches tax + NZD payout-to-bank; reduced-KYC | No byline; no schema; no 2026 bill |
| gameshub.com/nz/…/crypto | Intl | ~2–4 | List + guide | — | **FETCH 403** | — |
| slotozilla.com/nz/crypto-casinos | Intl | ~5–6 | Card listings | 0.8–1k | Fresh monthly date | **Very thin**; zero NZ specifics; beatable outright |

**Gaps:** (a) Review/FAQ schema; explicit no-KYC angle. (b) provably-fair (one-liner or absent); per-coin intent; withdrawal-speed proof. (c) NZ tax on crypto gambling + converting to NZD (recreational untaxed vs IR disposal rules); NZ 2026 licensing for crypto players; provably-fair explainer; no-KYC as owned category.

**Top opportunities:** no-KYC sub-page (84); crypto-tax NZ section (78); per-coin spokes (76); provably-fair explainer (74); schema + named author (73); 2026 bill explainer (68).

---

### /high-payout-casinos/ — "high payout casino NZ"

| Domain | Geo | Pos | Format | ~Words | Strengths | Weaknesses |
|---|---|---|---|---|---|---|
| casino.org/new-zealand/best-payouts | NZ | 1–2 | Guide + ranked cards | ~5,500 | Per-game RTP cards; live-dealer payout table; cites eCOGRA/iTech/MGA; flags 1-Dec rule | Thin operator-level audited RTP; RTP-vs-jackpot glancing |
| highestpayoutcasinogames.co.nz | NZ | 1 (EMD) | Encyclopedic guide | 8.5–9k | **Best RTP-vs-jackpot explainer**; "games to avoid"; audit-source transparency | **No byline, no date**; no NZD-license angle |
| casinonz10.com/best-payout | NZ | 2–3 | Listicle | ~4k | Clear NZD framing | Repetitive; no per-game RTP; no audit sources |
| bonus.net.nz/…/best-payout | NZ | 3–4 | Listicle | ~4k | Local .nz authority | Shallow RTP depth |
| next.io/…/best-payout (UK ref) | UK | 1–2 | Guide | — | **FETCH 403** | — |

**Gaps:** (a) operator-level avg RTP % in table; RTP + house-edge explainer; highest-RTP pokies table. (b) RTP-vs-progressive-jackpot explainer (only 1 does it); audit bodies name-dropped but **never evidenced with a cert ID**; live-dealer payout tables; "games to avoid". (c) verifiable RTP table w/ audit body + cert ID per operator; Act 2026 + NZD angle; NZD worked payout example; variance explainer; per-provider RTP-config disclosure (94% vs 96% builds).

**Top opportunities:** verifiable operator RTP table w/ cert ID (86); RTP-vs-jackpot explainer (80); Act 2026 + NZD angle (77); highest-RTP pokies table (76); "low-payout games to avoid" + variance (64).

---

### /fast-payout-casinos/ — "fast payout casino NZ"

| Domain | Geo | Pos | Format | ~Words | Strengths | Weaknesses |
|---|---|---|---|---|---|---|
| casino.org/…/fast-payouts | NZ | 1–2 | Guide + cards | ~7,500 | Method-speed table; explicit KYC-first; caps; "casinos to avoid"; real testing | Speeds as ranges not measured business days; caps glancing |
| casinobeats.com/nz/…/fast-payout | NZ | 1 | Guide | — | **FETCH 403** | — |
| gambling.com/nz/…/fastest-payout | NZ | 2 | Guide | — | **FETCH 403** | — |
| casinos.com/nz/fast-payout | NZ | 2–3 | Listicle | 0.8–1k | Clean cards; disclosure | **Thinnest** — no method table, no KYC, no caps, no NZ-license angle |
| casinobeats.com/uk/…/fast-withdrawal (UK ref) | UK | 1 | Deep guide + FAQ | 7.5–8k | **Gold-standard method table (fees + caps + delay-risk columns)**; per-casino caps | UK/UKGC/GamStop-specific |

**Gaps:** (a) withdrawal-speed-by-method table + KYC advice (thin competitors lack both). (b) measured NZ-business-day times w/ fees + delay-risk columns; per-operator daily/weekly cashout caps; crypto vs bank vs e-wallet true comparison. (c) per-operator **measured** withdrawal table (submit→approve→land in NZ business days); KYC-before-withdrawal standalone section; method table w/ fees+delay-risk+NZD caps; Act 2026 → payout-reliability angle.

**Top opportunities:** per-operator measured withdrawal table (88); method-speed table w/ fees+delay-risk+caps (83); KYC-before-withdrawal section (81); NZD cashout caps per operator (74); Act 2026 → reliability angle (72).

---

### /live-casinos/ — "live casino NZ"

| Domain | Geo | Pos | Format | ~Words | Strengths | Weaknesses |
|---|---|---|---|---|---|---|
| casino.guru/new-zealand/live-dealer | NZ | ~1 | Ranked list + guide | ~6,500 | Provider overview; house-edge transparency; clear methodology | Promo tone; bonus contribution buried; no NZ-timezone angle |
| junipercollective.co.nz/live-casinos | NZ | ~2 | Ranked list + reviews | ~2,400–2,600 | NZ-native (SkyCity comparison, NZD/tax); RG well-integrated | **Vague table limits**; shallow differentiation |
| whollysmoked.co.nz/live-casinos | NZ | ~3 | Deep ranked guide | 8.5–9k | **Best depth**: per-studio min bets, latency atlas, BJ strategy chart | All 11 = Evolution (concentration unflagged); crypto claims unverified |
| casino.org/new-zealand/live | NZ | ~4 | Guide + list | — | Brand authority; broad coverage | Global template lightly NZ-skinned |
| casinoblacks.com/live-casino | Global | ~5 | List guide | — | Ranks in NZ despite non-NZ TLD | **US-centric, thin NZ localisation — beatable** |

**Gaps:** (a) concrete NZD table-limit bands; Evolution vs Pragmatic split; house-edge table; game-show roster; mobile-browser note; RG in header. (b) **live-table bonus-contribution % with worked examples** (biggest shared weakness); concrete NZD min/max; latency/stream quality; studio-concentration honesty. (c) Act 2026 for live casino; NZ-timezone dealer availability; NZD-native vs USD-converted stakes; Pasifika/Asian-language tables (Andar Bahar/Teen Patti); lowest-latency-to-NZ hook.

**Top opportunities:** NZD limit bands + house-edge table above fold (82); honest live-bonus wagering explainer (80); Act 2026 live-casino section (74); studio-split page (70); NZ-timezone/latency angle (62).

---

### /no-deposit-casinos/ — "no deposit casino NZ"

| Domain | Geo | Pos | Format | ~Words | Strengths | Weaknesses |
|---|---|---|---|---|---|---|
| casino.guru/…/no-deposit | NZ | ~1 | Verified-offer list | — | **FETCH 403** (known for honest per-offer T&Cs + complaint data) | Could not read live |
| casino.org/…/no-deposit | NZ | ~2 | Comprehensive guide | ~8,500 | **Best honesty**: NZD caps stated; explains 50x on FS winnings; strong 2026 licensing section; code-freshness timestamps | Compare table below fold; per-spin FS value buried |
| bonus.net.nz/casino-bonus/codes | NZ | ~3 | Codes list + guide | 2.5–3k | NZ TLD; POLi/Neosurf; acknowledges limited value | **Vague max-cashout**; thin returning-player section |
| gambling.com/nz/…/no-deposit-bonus | NZ | ~4 | Short list | 0.8–1k | Strong author + affiliate transparency | **Thin**; no caps; FS-winnings mechanics unexplained; no 2026 angle |
| casinos.com/nz/bonus/no-deposit | NZ | ~5 | List guide | — | Clean ranked format | Generic global template |

**Gaps:** (a) real max-cashout caps in NZD (NZ$50–100) upfront per offer; FS-winnings wagering worked example; per-spin FS value; code-freshness timestamps. (b) honest "why headline no-deposit is low-value" framing; cap math; cash-chip vs free-spins vs combo distinction. (c) Act 2026 + "will these codes survive the transition?" angle; NZD-native vs USD-converted; realistic-expectations calculator; maintained "verified this week" freshness block.

**Top opportunities:** max-cashout caps + FS-winnings wagering in NZD (84); "what NZ$50 really pays" worked example (82); Act 2026 + code-longevity angle (78); per-offer freshness block (76); cash-chip vs FS vs combo explainer (68).

---

## Fetch-failure log (not fabricated)

HTTP 403 / unreadable, excluded from content analysis, positions inferred from SERP order only:
esportsinsider.com/nz, gamblinginsider.com/nz, bookies.com/nz, oddschecker.com/nz, torontoguardian.com (crypto), gameshub.com/nz (crypto & fast-payout), casinobeats.com/nz (fast-payout), gambling.com/nz (fast-payout), next.io (high-payout), casino.guru (no-deposit), whollysmoked.co.nz (live, on re-fetch).

## Accuracy checkpoints before publish

1. **Confirm the Gambling Act 2026 dates** — application deadline (we use 1 Dec 2026) vs offshore wind-down (some sources imply mid-2027). Verify against DIA primary sources.
2. **Drop POLi** from any page copy — discontinued 2022. Use NZD bank transfer, e-wallets, Paysafecard, crypto.
3. **Verify penalty figures** (NZD 5m / NZD 300k) and EOI fee (~NZD 19,000 + GST) before stating them.
