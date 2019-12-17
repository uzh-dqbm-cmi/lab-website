---
title: Automated Reports from Xrays
summary: Using deep learning for automatically generated medical reports describing radiological images.
authors: 
- nicoperez
date: 2019-10-10
tags: 
- Data Science
categories:
- Deep Learning
image:
  placement: 1
  caption: 'Sample x ray from BBC.co.uk [1]'
  focal_point: ""
  preview_only: false
projects: []
---

Today's world is truly living a revolution due to the increased use of machine learning applications. Yet, in the clinical setting, very few applications seem to be making their way through. This is mainly due to the fact that to this day, we heavily rely on experienced doctors to make all decisions about patients. The idea of somehow replacing them seems risky and offensive. That is why our approach focuses on developing models that, once applied in the clinical setting, would streamline the job of the radiologist, allowing the physician to spend less time with trivial tasks.

Considering this context, we focused on the tasks performed by a radiologist. In particular, when labeling the results of an x-ray. Typically, an experienced radiologist spends a few minutes per x-ray and writes a report that evaluates possible conditions about this patient. In her evaluation, she writes specific sentences linked to certain patterns present in the image. One common reference mentioned in medical reports is "atelectasis", which in simple words refers to the collapse or incomplete expansion of the lung and can be seen in images as a darkened portion of the lung. In this case, the trained physician links visual patterns with particular sentences that describe that condition, a task which fits perfectly for the application of machine learning. 

In our project, we seek to build multimodal machine learning models that efficiently link radiological images and their associated reports to streamline the work of a radiologist. For this, we combine different approaches: On the one hand, we use pre-trained convolutional neural networks to extract visual features from the images and on the other hand, we use models from the Natural Language Processing domain to learn underlying structures within the medical reports. By combining both of these approaches we are able to mimic what a physician normally does when assessing radiological images, with the advantage that our model will more consistently make predictions and write reports.

In the larger picture, we hope to develop models that will be able to support the physicians work by generating medical reports for images with equal or better performance. 

[1] How AI could speed-xray processing, BBC, https://www.bbc.co.uk/programmes/p06yqysy (2019)
