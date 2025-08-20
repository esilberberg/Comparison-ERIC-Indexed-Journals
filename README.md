# Analysis of ERIC's 2025 Revised Indexing Policy: Impact on Educators’ Access to the Scholarly Record 
This study aims to answer the question, how do ERIC’s budget cuts and the subsequent deselection of journals affect education practitioners’ ability to access scholarly research? To address this, we systematically compared ERIC’s November 2024 and June 2025 journal lists and uncovered a significant drop in the number of indexed titles, the introduction of a new “inactive” indexing status, and unexplained missing journals. We investigated the characteristics of the deselected journals, including their scope, Open Access (OA) status, and country of origin to understand how the deselection changes the framing of the educational scholarly record. Finally, in the absence of a comprehensive official explanation from ERIC, we propose explanations for the deselection and underscore its broader impact on education practitioners’ access to the scholarly record. 

## Files Overview

See `5-analysis.xlsx` under the `data` directory for complete set of research data. Data collected on August 1, 2025.

The `journal-lists` directory contains the 2024 and 2025 ERIC Journal Lists downloaded from eric.ed.gov.

The `data` directory contains the excel files used in the analysis.

`Webster-journals.xlsx` is derived from [Webster, E. (2025). Journals no longer being indexed by ERIC. Accessed August 1, 2025](https://docs.google.com/document/d/1H5qSJQE2N-wh6FxnWxBHE9r5Oq9mW-kI5Q_LDf4pKs4/edit?tab=t.0#heading=h.amc5r0s78jxx.).

| Script     | Description | Input     | Output |
| ----------- | ----------- | ----------- | ----------- |
|`1_build_dataset.py` | Combines the two ERIC journal lists (2024 and 2025) and into single list of all unique journal titles. It identifies which journals appear only on the 2024 or 2025 list and and records their indexing status (active vs. inactive) via the ERIC documentation. | `1-journals-2024-2025-ERIC-indexing-policy.xlsx` | `2-master-journal-list.xlsx` |
| `2_get_issn.py` | Retrieves each journal's ISSN-L by searching the journal name in the [OpenAlex API](https://docs.openalex.org/how-to-use-the-api/api-overview). | `2-master-journal-list.xlsx` | `3-journals-and-issn.xlsx` |
| `3_get_openalex_data.py` | Retrieves each journal's homepage, country of origin, status in [DOAJ](https://doaj.org/), and OA status by using its ISSN-L to query the OpenAlex API. | `3-journals-and-issn.xlsx` | `4-journals-with-openalex-data.xlsx` |
| `4_general_tallies.py` | Analyzes six categories of journals. It calculates the total count for each and determines the percentage that are OA, included in DOAJ, and from various countries. The categories are: <ul><li>All journals on the 2024 list</li><li>All journals on the 2025 list</li><li>Journals unique to the 2024 list</li><li>Journals unique to the 2025 list</li><li>Journals with active indexing status on 2025 list</li><li>Journals with inactive indexing status on 2025 list</li></ul> | `4-journals-with-openalex-data.xlsx` | `5-analysis.xlsx` |
| `5_cross_check_webster_list.py` | Compares which journals from Webster's (2025) crowdsourced listed of deselected journals actually appeared on ERIC's inactive journals list. | `Webster-journals.xlsx` <br> `5-analysis.xlsx` | |
| `6_country_comparison.py` | Calculates absolute change and percent change for the number of journals deselected by country. | `5-analysis.xlsx` | |
| `7_inactive_journals.py` | Analyzes the inactive journals to determine the percentage that are still actively publishing, the percentage that were indexed by ERIC up to 2025, and the average length of time they were indexed by ERIC. | `5-analysis.xlsx`| |
| `8_anomalous_journals.py` | Analyzes journals that were either unique to the 2024 or 2025 list to determine the percentage that are still actively publishing, the percentage that were indexed by ERIC up to 2025, and the year of earliest publication indexed by ERIC. | `5-analysis.xlsx`| |
