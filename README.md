# Nepal: law history in git

The Constitution of Nepal as a git repository: one file per article (`art-001.md` to `art-308.md`), the preamble and the nine schedules, one paragraph per line, so `git blame` and `git diff` work line by line.

**Language: English.** The text is the Law Commission's official English version. The Commission's Nepali PDF on the same page has a legacy-font text layer that extracts as wrong characters, so it was not used.

**What this repository is not, yet: a history.** The Law Commission publishes one consolidated English text, "as amended" by the Constitution of Nepal (First Amendment), 2016 (28 February 2016) and the Second Amendment, 2020 (18 June 2020). Nothing earlier can be rebuilt from that source: the 2015 text as promulgated on 20 September 2015 is not published separately. So the repository holds one version, dated 18 June 2020 (the latest amendment the text incorporates) and credited to the publisher as the oldest version available, with the three laws named as earlier laws. Later amendments will be added as they are sourced. The Commission's Nepali text runs to a later amendment (2081 B.S., 2024); it is not in this repository.

## What it holds

| Folder | Text | Versions |
| --- | --- | ---: |
| `constitution/` | The Constitution of Nepal, preamble, Articles 1 to 308 and Schedules 1 to 9 | 1 |

Part headings (Part-1 to Part-35) and the cover list of amendments are not kept as separate files; each article keeps its number and heading. Page headers, page numbers and line wraps from the PDF were removed. Schedule 1 (the flag) and Schedule 3 (the coat of arms) describe drawings; the drawings themselves are not in the text.

## Dates

Each commit is dated at noon, Asia/Kathmandu, on the day the change took effect. The in-force day is in the `In-force:` trailer. The Constitution and its amendments take effect on publication in the Nepal Gazette, the dates the Law Commission prints on the cover of its text.

## Source and licence

Source: Nepal Law Commission, [lawcommission.gov.np](https://lawcommission.gov.np/content/13437/), English PDF, retrieved 2026-10-30. See [`LICENSE`](LICENSE).
