---
title: Drug-Drug Interactions
summary: Write a short summary here.
authors: 
- kyriakosschwarz
date: 2019-11-27
tags: 
- Data Science
- Bioinformatics
categories:
- Deep Learning
image:
  placement: 1
  # caption: 'Sample x ray from BBC.co.uk [1]'
  focal_point: ""
  preview_only: false
projects: []
---

Drug-drug interactions (**DDIs**) refer to drugs' effect upon their concurrent administration. Under those conditions additional side effects may surface which would not manifest in case of individual drug administration. Consequently, DDIs are an important consideration for patient treatment where the aim is to maximize drug effectiveness while simultaneously minimizing unwanted side effects. Due to the combinatorial explosion of possible drug pairs, it is impossible to test them all and discover previously unobserved side effects. Therefore, computational methods and more recently **Deep Learning** based models are being employed for this task. 

{{< figure src="sideEffectsWordCloud.jpg" title="Side Effects" >}}

For instance, Lee et al. [[1](https://doi.org/10.1186/s12859-019-3013-0)] used Autoencoders coupled with Feed Forward Neural Network that takes drug structure, target gene and Gene Ontology (GO) term data as input, in order to predict the DDI type (example type: "DRUG A may increase the hypoglycemic activities of DRUG B."). Similarly, Ryu et al. [[2](https://doi.org/10.1073/pnas.1803294115)] proposed DeepDDI, a multilabel classification model, which also takes drug structure data as input, along with drug names, in order to output DDIs as human-readable sentences.

Due to these exciting opportunities, in one of our projects, we seek to improve our understanding of drug-drug interactions by developing and applying novel and interpretable Deep Learning models.

**References**

- [1] Lee, Geonhee, Chihyun Park, and Jaegyoon Ahn. “Novel Deep Learning Model for More Accurate Prediction of Drug-Drug Interaction Effects.” BMC Bioinformatics 20, no. 1 (August 6, 2019): 415. [https://doi.org/10.1186/s12859-019-3013-0](https://doi.org/10.1186/s12859-019-3013-0).
- [2] Ryu, Jae Yong, Hyun Uk Kim, and Sang Yup Lee. “Deep Learning Improves Prediction of Drug–Drug and Drug–Food Interactions.” Proceedings of the National Academy of Sciences 115, no. 18 (May 1, 2018): E4304–11. [https://doi.org/10.1073/pnas.1803294115](https://doi.org/10.1073/pnas.1803294115).
