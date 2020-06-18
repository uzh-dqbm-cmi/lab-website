---
title: "AutoDiscern: Rating the Quality of Online Health Information with Hierarchical Encoder Attention-based Neural Networks"
authors:
- laurakinkead
- ahmedallam
- michaelkrauthammer
date: "2020-06-09T00:00:00Z"
doi: "10.1186/s12911-020-01131-z"

# Schedule page publish date (NOT publication's date).
publishDate: "2020-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*BMC Medical Informatics and Decision Making*"
# publication_short: ""

abstract: Patients increasingly turn to search engines and online content before, or in place of, talking with a health professional. Low quality health information, which is common on the internet, presents risks to the patient in the form of misinformation and a possibly poorer relationship with their physician. To address this, the DISCERN criteria (developed at University of Oxford) are used to evaluate the quality of online health information. However, patients are unlikely to take the time to apply these criteria to the health websites they visit. We built an automated implementation of the DISCERN instrument (Brief version) using machine learning models. We compared the performance of a traditional model (Random Forest) with that of a hierarchical encoder attention-based neural network (HEA) model using two language embeddings, BERT and BioBERT. The HEA BERT and BioBERT models achieved average F1-macro scores across all criteria of 0.75 and 0.74, respectively, outperforming the Random Forest model (average F1-macro = 0.69). Overall, the neural network based models achieved 81% and 86% average accuracy at 100% and 80% coverage, respectively, compared to 94% manual rating accuracy. The attention mechanism implemented in the HEA architectures not only provided ’model explainability’ by identifying reasonable supporting sentences for the documents fulfilling the Brief DISCERN criteria, but also boosted F1 performance by 0.05 compared to the same architecture without an attention mechanism. Our research suggests that it is feasible to automate online health information quality assessment, which is an important step towards empowering patients to become informed partners in the healthcare process.
# Summary. An optional shortened abstract.
summary: To help patients find high quality health information online, we developed a Deep Learning system that evaluates the quality of online health articles. The system implements the DISCERN criteria, which checks for references, balanced writing, and more.

tags:
- Data Science
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://bmcmedinformdecismak.biomedcentral.com/track/pdf/10.1186/s12911-020-01131-z
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
projects: [auto-discern]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

