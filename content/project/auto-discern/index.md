---
title: autoDISCERN
summary: Assessing the quality of online health information with AI.
tags:
- Clinical Data Science
date: "2019-12-02T00:00:00Z"
authors:
- laurakinkead

# Optional external URL for project (replaces project detail page).
# external_link: ""

image:
  caption: Mock Up of the autoDISCERN validator.
  focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: View Code
  url: https://github.com/uzh-dqbm-cmi/auto-discern
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

Patients increasingly turn to the web for health information. This is great news for patient engagement... but only if they find good information! Unfortunately, low quality articles are common on the internet. This presents risks to the patient in the form of misinformation and a possibly poorer relationship with their physician. To address this, researchers at the University of Oxford developed the [DISCERN instrument](http://www.discern.org.uk/index.php): a set of criteria that any lay-person can use to evaluate the quality of online health information. However, patients are unlikely to take the time to apply these criteria to the health websites they visit. Enter machine learning!

We built an automated implementation of the DISCERN instrument (Brief version) using machine learning models. We compared the performance of a traditional model (Random Forest) with that of a hierarchical encoder attention-based neural network (HEA) model using two language embeddings, BERT and BioBERT. The figure below summarizes the architecture of the HEA model.

{{< figure src="architecture_overview.png" title="Architecture of the Hierarchical Encoder Attention-based model used to evaluate health articles according to the DISCERN critera." >}}

Overall, we found that our models were able to reproduce the DISCERN criteria reasonably well. The HEA architecture with BioBERT encodings achieved an average F1 score of 0.74 across all criteria. This translates to an accuracy of 81%. In comparison, human raters achieve an accuracy of 94% on this task.

The attention mechanism implemented in the HEA architectures not only provided _model explainability_ by identifying reasonable supporting sentences for the documents fulfilling the Brief DISCERN criteria, but also boosted F1 performance by 0.05 compared to the same architecture without an attention mechanism.

| Discern Criteria                | Attended Sentence    |
| ----------------------- | ------------------------- |
| Is it clear what sources of information were used to compile the publication (other than the author or producer)? | _American Journal of Geriatric Psychiatry._ |
| Is it clear when the information used or reported in the publication was produced? | _Review Date: 3/8/2013._               |
| Does it describe how each treatment works? | _Gentler martial arts which focus on internal control, breathing and mental discipline can be especially useful for combating depressed thinking and improving relaxation skills._ |
| Does it describe the benefits of each treatment? | _The mindfulness approach uses meditation, yoga, and breathing exercises to focus awareness on the present moment and break negative thinking_ |
| Does it describe the risks of each treatment? | _Common side effects of SSRIs include:_ |


Our research suggests that it is feasible to automate online health information quality assessment, which is an important step towards empowering patients to become informed partners in the healthcare process.
