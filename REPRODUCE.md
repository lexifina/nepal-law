# How this repository was made (Nepal)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Nepal Law Commission, The Constitution of Nepal (English, incorporating the First and Second Amendments) | <https://lawcommission.gov.np/content/13437/> | 2026-10-30 | No reuse terms stated by the publisher; official government publication |
| Nepal Law Commission, The Labour Act, 2017 (2074) (official English text) | <https://lawcommission.gov.np/en/wp-content/uploads/2021/03/The-Labor-Act-2017-2074.pdf> | 2021-04-05 | No reuse terms stated by the publisher; official government publication |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | The Constitution of Nepal (consolidated English text, as amended to 18 June 2020) | 1 | 2020-06-18 to 2020-06-18 |
| `labour-act` | The Labour Act, 2017 (2074) | 1 | 2017-09-04 to 2017-09-04 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4 laws in the record.
- 3 tags.

## Dates

Each commit is dated at noon (Asia/Kathmandu) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Constitution of Nepal and each amendment come into force on the date of its publication in the Nepal Gazette, the date the Law Commission prints on the cover of its consolidated English text. https://lawcommission.gov.np/content/13437/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `8154d69f5d64a23aeeed48ade189cf3727300f034cb8d41e9716d2d9a712cc01` (564137 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

2 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 2 history commits and 3 tags (history tip `c42766141c0e4d96d9ba7c82c3591dbbc2d31127`).

## Decisions made by hand

- English is built: the Law Commission publishes an official English text of the Constitution with a sound text layer, so the legacy-font Nepali PDF (which would need a Preeti-to-Unicode mapping) was not used.
- The Commission publishes only the consolidated text as amended to the Second Amendment (18 June 2020); the First Amendment (28 February 2016) and the Second are listed as earlier laws, not reconstructed. The version is dated by the Second Amendment, the latest state the document gives.
- Part headings (Part-1 to Part-35) and the cover list of amendments are not kept as files; each article keeps its number and heading. Page headers and page numbers were dropped and wrapped lines were joined; clauses start new lines.
- The Constitution of Nepal was promulgated on 20 September 2015 (Gazette); that date is recorded in the laws list.
- Labour Act, 2017: one version, the text as authenticated on 4 September 2017 (19 Bhadra 2074), the day it commenced ("This Act shall commence forthwith", s. 1(2)). The Law Commission English text shows no later amendments; any later amendments are not in this record.
- Chapter headings are not kept as files; each section keeps its number and heading. Page headers and page numbers were dropped and wrapped lines were joined; sub-sections and clauses start new lines.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the parser and chose the source; it did not write or alter any legal text. Text comes straight from the PDF text layer.
- Claude Code wrote the parser; it did not write or alter any legal text. Text comes straight from the PDF text layer.
