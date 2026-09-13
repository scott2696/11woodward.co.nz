# Brand logos

Master logo set for all sites under `MY_SITES/`. Copy this folder into a site as
`<site>/logos/` and reference images as `/logos/<file>`.

| Brand        | File                     | Notes                          |
|--------------|--------------------------|--------------------------------|
| Spinjo       | `spinjo.png`             |                                |
| Lucky Circus | `lucky-circus.jpg`       |                                |
| Lucky7even   | `lucky7even.jpg`         |                                |
| Lucky Vibe   | `lucky-vibe.jpg`         |                                |
| Roby Casino  | `roby-casino.jpg`        |                                |
| Spino        | `spino.jpg`              |                                |
| Ivibet       | `ivibet.png`             | casino logo                    |
| Ivibet       | `ivibet-sportsbook.jpg`  | use on sportsbook pages        |
| Hellspin     | `hellspin.jpg`           |                                |
| Slotgem      | `slotgem.jpg`            |                                |
| Bet&Play     | `betandplay.png`         |                                |

Wired into every `data-logo-slot` on `11woodward.co.nz` (see
`scratchpad/wire_logos.py` pattern: replaces the slot's fallback text with an
`<img>` keyed on the brand name).

## Added September 2026 (11woodward lineup expansion)

Copied from the master set under `MY_SITES/teachinnewzealand.co.nz/logos/`, except
CrownSlots which came from `keno-results.co.nz/assets/img/partners/`.

| Brand        | File                     | Notes                            |
|--------------|--------------------------|----------------------------------|
| CrownSlots   | `crownslots.jpg`         |                                  |
| MadCasino    | `madcasino.png`          | EN variant                       |
| Kingdom      | `kingdom.png`            |                                  |
| Smash        | `smash.png`              |                                  |
| Rivo         | `rivo.png`               |                                  |
| Rooster Bet  | `rooster-bet.png`        |                                  |
| Fortune Play | `fortune-play.png`       |                                  |
| Slotgem      | `slotgem.png`            | replaces `slotgem.jpg` in markup |

`slotgem.jpg` encoded its rounded-corner cutouts as solid black, which showed as
four dark blobs on the white logo tile; `slotgem.png` has them transparent, so
pages now reference the PNG. The JPEG is kept as the untouched original.

Vector originals for Kingdom, MadCasino, Rivo and Smash are in `svg/`.

### Still missing

- **Gunsbet** — no artwork supplied. Its `data-logo-slot` renders the brand name
  as a styled wordmark instead; drop in `gunsbet.png` and wire it to replace that.

## `norm/` — display set used by the site

The toplist tiles size artwork with `object-fit:contain`, so a square badge ends
up height-limited and renders far smaller than a wide wordmark that fills the
tile. Several logos also ship with large transparent margins baked in (Kingdom,
MadCasino and Smash were each a 300x300 canvas holding a ~300x110 wordmark),
which made the problem worse.

`norm/` holds a display set generated from the files above: each logo is trimmed
of its transparent/near-white margin, scaled to a common *area* so a wordmark and
a badge carry similar visual weight, then centred on one shared 480x144 canvas
(3.33:1, matching the 160x48 toplist tile). Because every output shares an aspect
ratio, each renders at an identical size in a given tile — 96x28 in the review
headers, full-width in the toplist — with no change to the tiles themselves.

All `<img src>` on this site point at `/logos/norm/*.png`. The originals are the
files above and are left untouched, so re-copying the master set does not undo
this; regenerate with `normalise_logos.py` after adding a brand.

Near-square marks (Lucky Circus, Lucky Vibe, Fortune Play, Bet&Play) still read
narrower than the wide wordmarks — they fill the tile's full height, which is as
close to equal as it gets without cropping the artwork.
