---
title: Federated Learning
summary: 
tags:
- Data Science
- Featured
date: "2021-01-01T00:00:00Z"
authors:
- matteoberchier

# Optional external URL for project (replaces project detail page).
# external_link: ""

image:
  caption: 
  focal_point: Smart

links:
#- icon: github
#  icon_pack: fab
#  name: View Code
#  url: https://github.com/uzh-dqbm-cmi/mridle
url_code: ""
url_pdf: ""
url_slides: "https://docs.google.com/presentation/d/1rp7Z1r1GELJYgmI0Ti1AbUa5k46ZvHFKyKLV_t63Yg4/edit?usp=sharing"
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Today, in every aspect of our lives, everything we do leaves a digital footprint. Health-care institutions are also increasingly collecting more data on their patients, thanks to improved IT infrastructure and new sensors that allow to record vital signs at high frequencies. Most hospitals still store and manage this information locally, under strict data privacy and protection regulations.

Although data privacy and protection are of the utmost importance, they become an obstacle for the large-scale analysis of such data and the extraction of new insights that could help doctors in the diagnosis and therapeutic process.

Federated learning aims to avoid the need for research institution and third party to have direct access to data, while still enabling them to extract high-level insights from it. In this project, our research focus is to enable the use of machine learning algorithms using federated learning in healthcare. We are working on testing the algorithm on a network of hospitals connected to a central server. The machine learning model is defined on the central server and shared to the hospital servers which proceed with training this model on their local data and sharing the model parameters once a training round is completed.

Upon receiving the model parameters from multiple hospitals, the central server aggregates these parameters (using averaging or more complex functions) and redistributes the new parameters to the hospital servers for a further training round.

This procedure is repeated until the model performance converges / stabilizes. The parameters of the optimized model in the central server have thus been trained without the central server ever receiving one single patient record.

The followig slides present an overview of `Federated learning` algorithms in healthcare with pointers to couple of research papers working in this area presented at on of our Labe meetings.

[{{< figure src="Federated Machine Learning@RIP.png" title="Federated Machine Learning Overview @RIP" >}}](https://docs.google.com/presentation/d/1rp7Z1r1GELJYgmI0Ti1AbUa5k46ZvHFKyKLV_t63Yg4/edit?usp=sharing)

