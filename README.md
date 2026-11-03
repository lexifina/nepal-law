# Nepal: law history in git

The law of Nepal as a git repository: the Constitution and the Acts of Parliament in force, one file per article or section, one paragraph per line, so `git blame` and `git diff` work line by line.

**Language: English.** The text is the Nepal Law Commission's official English version. The Commission's Nepali PDFs use legacy fonts whose text layers extract as wrong characters, so they were not used.

**What this repository is, so far: mostly current text, not yet a full history.** For most Acts the Law Commission published one consolidated English text, "as amended" by the amendments listed on its cover. Each such Act is here as one version:

- an Act whose cover lists no amendments is dated by its date of authentication;
- an amended Act is dated by the date of the latest amendment its cover lists, and that version is credited to that amendment, with the Act and its earlier amendments named;
- where the cover's amendment dates could not be read reliably, the version is dated by the day the text was retrieved from the Commission and credited to the publisher.

So a version's date is the day from which that wording applied, never earlier. Earlier wordings are not rebuilt yet; they can be added later as separate, labelled commits.

## What it holds

| Folder | Text | Versions |
| --- | --- | ---: |
| `constitution/` | The Constitution of Nepal, preamble, Articles 1 to 308 and Schedules 1 to 9, as amended to 18 June 2020 | 1 |
| `labour-act/` | The Labour Act, 2017 (2074), as enacted | 1 |
| one folder per Act | The Acts in force that the Law Commission published in English (see `data/versions.json` for the list) | 1 each |

The Acts were chosen from the Law Commission's current index of Acts in force: an Act is included when the Commission also published an official English text of it. Some English texts are older than the latest Nepali text; each version's commit says which amendment its wording reflects. An Act that has no English text, or whose English text could not be split into sections reliably, is not here yet.

Part and chapter headings and the cover list of amendments are not kept as separate files; each article or section keeps its number and heading, and the schedules of an Act are kept together in one file. Footnotes, page headers and page numbers were removed, and so were the symbols that mark amended text; wrapped lines were joined.

## Dates

Each commit is dated at noon, Asia/Kathmandu, on the day the change took effect. The in-force day is in the `In-force:` trailer. Dates are the Gregorian dates the Law Commission prints beside the Bikram Sambat dates on each Act's cover (converted from Bikram Sambat where only that is printed).

## Source and licence

Source: Nepal Law Commission, [lawcommission.gov.np](https://lawcommission.gov.np/), official English texts of the Constitution and the Acts. See [`LICENSE`](LICENSE).
