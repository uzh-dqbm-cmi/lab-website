---
title: Liquid Biopsy
summary: 
tags:
- Translational Bioinformatics
date: "2026-01-01T00:00:00Z"
authors: 
- zsoltbalazs
- todorgitchev
- ivnaivankovic

# Optional external URL for project (replaces project detail page).
# external_link: ""

# image:
#   caption: ECCB 2018 poster.
#   focal_point: Smart

links:
# - icon: github
#   icon_pack: fab
#   name: View Code
#   url: https://github.com/uzh-dqbm-cmi/hcup_research
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Our lab develops computational solutions to improve liquid biopsies. We are especially interested in cfDNA-sequencing, as we believe that cfDNA is a very potent biomarker not only in cancer but also in non-malignant diseases.

**Monitoring radiotherapy patients through liquid biopsy**
In a collaborative effort with the Department of Radiation Oncology, we collected liquid biopsies from a heterogeneous cohort of cancer patients undergoing radiotherapy. Our approach utilizes whole genome sequencing (WGS) to maximize insights from circulating cell free tumor DNA (ctDNA). By leveraging multimodal information discerned from cfDNA WGS, we show that high-tumor fractions are associated with poor prognosis and can indicate a systemic progression (polymetastasic disease). We also demonstrate the power of cfDNA WGS to capture additional modalities, such as viral sequences (HPV) in head-and-neck cancer, which can drastically increase the sensitivity of tumor detection. (read more here: https://www.sciencedirect.com/science/article/pii/S0167814024006340)

**Facilitating data-reuse in liquid biopsy**
We developed a light-weigth pre-analytic workflow called Fragmentstein, to allow for the conversion of non-sensitive (does not contain mutational information) cfDNA fragment information files into complete alignment mapping files which can be processed by any downstream bioinformatics tool. The tool facilitates the widespread re-use of non-sensitive cfDNA fragmentation data. (read more here: https://academic.oup.com/bioinformatics/article/40/1/btae017/7550024)

**How should you process cfDNA-sequencing data?**
Numerous bioinformatics are used routinely in the analysis of cfDNA-sequencing data. But many of the practices that are routinely applied (e.g. trimming, downsampling) have been benchmarked for other applications. We investigated the effects of common pre-processing choices on the downstream analysis of cfDNA fragment data. Overall, most common practices have little effect on the downstream analysis. However, some preprocessing steps can have synergistic effects for specific analyses (e.g. in-silico size selection and strict alignment filtering on end motif analysis). (read more here: https://academic.oup.com/gigascience/advance-article/doi/10.1093/gigascience/giaf139/8306867)
