# Tools

The scripts behind this Nepal-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/nepal-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only nepal-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py` and `late_ext_rebut.py` sit two folders above the scripts, next to
`config.json`.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to the folders since the move (`map_moved.py`), adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `map_moved.py` | Rewrites the paths in the history table to each Act's folder since the move of 10 November 2026 (`data/paths.json`, for example `drugs-act-2035-1978/` to `drugs-act/1978/2035/`), so that an Act's history is not split in two at the move; `run.sh` runs it after the history is indexed |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods (there were none here) |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (there were none here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the README, in English, light and dark |
| `config.json` | The repository, its language (English), the category names, the paths that are not law, and the chart's labels |
| `apply_patches.py` | Applies the patches below to a copy of the scripts, each once, in a fixed order, and records them in `.kit_patches.json` (`python -X utf8 apply_patches.py <scripts dir>`); later patches edit text earlier ones inserted, so a patch is never run twice on the same copy |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_de.py`, `patch_co.py`, `patch_sv.py`, `patch_pt.py`, `patch_ru.py`, `patch_r18.py`, `patch_xk.py`, `patch_mo.py`, `patch_lu.py`, `patch_li.py`, `patch_mx.py`, `patch_mn.py`, `patch_mt.py` | The same for the dates, references and currency names of other languages and jurisdictions (Vietnamese, Spanish, Catalan, German, Colombian, Salvadoran, Portuguese, Russian, Albanian, Macanese, Luxembourgish, Liechtenstein, Mexican, Mongolian, Maltese); they change nothing here (`patch_mt.py` also stops "Cabernet Franc" and "Dinaric" being read as currencies in every language; dead currencies stayed at 0) |
| `patch_en.py`, `patch_en_et.py` | English fixes to `detectors/placeholder_ref.py` made for bhutan-law and ethiopia-law ("vacation", "null and void", "Section … is repealed", "Proclamation No. … is hereby repealed", "shall be deleted") |
| `patch_np.py` | The English fix made for this repository, in the same form (`python -X utf8 patch_np.py <scripts dir>`; see below); it is last in `apply_patches.py`'s order |
| `patch_build_r7.py` | Brings a country's `build_vulns.py` up to date: lapsed-limit reviews matched on 400 characters of context, not 80, and a file deleted before a folder move linked under its old folder (already applied to the `build_vulns.py` here) |
| `redo.py` | Runs `apply_patches.py`, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--full` runs every step again through `run.sh`, `map_moved.py` among them, sends every category to the model and keeps every review already made; `EMBED_FONTS` names the script that embeds the chart's fonts); not needed here, as the fixes were in place before the review |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(data|tools|vulnerabilities)/'`.

Changes made for this repository:

- `pins.json` names the corpus language as `en`, the language of the texts, so the detectors use the English month names
  and the English currency exceptions. `add_root.py` is unchanged: the 190 commits that make a version credited to an Act
  carry `Kind: law`, the 34 credited to the Law Commission (the Constitution and the Acts dated by the archive's capture)
  `Kind: publisher`, which it also counts as law, and the 16 that change only documentation, tables, tools or the folder
  layout carry `Kind: documentation` or no `Kind` and are left out.
- `detectors/placeholder_ref.py` (`patch_np.py`) no longer reads "expired" right after "date" or "date-" as the mark of a
  repealed section: section 30 of the Drugs Act, 2035 (1978), "No person shall sell or distribute any drug which is date
  expired.", was read as repealed, and section 34(2), which punishes a sale "contrary to section 30", as a reference to it
  and a penalty with no offence. References to repealed placeholders and dead fines, which use the same test, went from 1
  each to 0. Both detectors were run again after the fix, before the model review.
- `config.json` counts as not law `data/`, `tools/`, `vulnerabilities/`, the root files and every `README.md` (each Act's
  list of its sections).
- Dates in the Bikram Sambat calendar are not converted: the detectors read Gregorian dates only, and 15 "until", "till"
  or "upto" phrases before a Bikram Sambat date with no Gregorian date beside it go unread (see EDGE-CASES.md). A
  conversion would need a table of month lengths for each Bikram Sambat year, which this repository's text cannot check.
