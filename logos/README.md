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
