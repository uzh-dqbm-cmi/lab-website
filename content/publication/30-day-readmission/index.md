---
title: "Neural networks versus Logistic regression for 30 days all-cause readmission prediction"
authors:
- ahmedallam
- michaelkrauthammer
date: "2019-09-01T00:00:00Z"
doi: "10.1038/s41598-019-45685-z"

# Schedule page publish date (NOT publication's date).
publishDate: "2019-12-02T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*Scientific Reports*"
publication_short: ""

abstract: Heart failure (HF) is one of the leading causes of hospital admissions in the US. Readmission within 30 days after a HF hospitalization is both a recognized indicator for disease progression and a source of considerable financial burden to the healthcare system. Consequently, the identification of patients at risk for readmission is a key step in improving disease management and patient outcome. In this work, we used a large administrative claims dataset to (1) explore the systematic application of neural network-based models versus logistic regression for predicting 30 days all-cause readmission after discharge from a HF admission, and (2) to examine the additive value of patients’ hospitalization timelines on prediction performance. Based on data from 272,778 (49% female) patients with a mean (SD) age of 73 years (14) and 343,328 HF admissions (67% of total admissions), we trained and tested our predictive readmission models following a stratified 5-fold cross-validation scheme. Among the deep learning approaches, a recurrent neural network (RNN) combined with conditional random fields (CRF) model (RNNCRF) achieved the best performance in readmission prediction with 0.642 AUC (95% CI, 0.640–0.645). Other models, such as those based on RNN, convolutional neural networks and CRF alone had lower performance, with a non-timeline based model (MLP) performing worst. A competitive model based on logistic regression with LASSO achieved a performance of 0.643 AUC (95% CI, 0.640–0.646). We conclude that data from patient timelines improve 30 day readmission prediction, that a logistic regression with LASSO has equal performance to the best neural network model and that the use of administrative data result in competitive performance compared to published approaches based on richer clinical datasets.
# Summary. An optional shortened abstract.
summary: We conclude that data from patient timelines improve 30 day readmission prediction, that a logistic regression with LASSO has equal performance to the best neural network model and that the use of administrative data result in competitive performance compared to published approaches based on richer clinical datasets.

tags:
- Deep Learning
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://www.nature.com/articles/s41598-019-45685-z.pdf
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
#   focal_point: ""
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [readmission]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

