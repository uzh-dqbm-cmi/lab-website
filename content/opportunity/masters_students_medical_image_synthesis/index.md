---
title: We are looking for Master Students in Medical Image Synthesis using Generative Models!
draft: false
authors:
- leabogensperger
- soniadifrancesco
- michaelkrauthammer
tags: 
- Machine learning
#- Bioinformatics
- Opportunities
categories:
- Machine learning
#- Bioinformatics

# list the projects you want masters students for here, if there are pages for them
# projects: []
---


We are currently looking for a Master student with a background in machine learning and/or computer vision for a project on medical image synthesis using generative models.

Nailfold capillaroscopy (NFC) is an imaging procedure to detect signs of microangiopathy in patients for system sclerosis. Previsouly, AI-based systems using a vision transformer have shown great potential for automated NFC image classification [1]. However, due to label imbalances and limited available medical images this project should investigate the feasibility of generated synthetic images to improve the downstream task of image classification.

We are particulary interested in finetuning latent diffusion models (LDMs) [2,3] to generate label-conditioned NFC images. The main tasks will be to adapt the LDM pipeline to medical NFC images, generate label conditioned images, and conduct a comparison with existing approaches, explore the potential of LDMs in augmenting the medical data set for image classification,
investigate whether text embeddings extracted from medical reports can be used to improve the quality of the generated images.

You can apply by sending a CV to this e-mail [lea.bogensperger@uzh.ch] along with a short description of your motivation to join our lab.

[1] Garaiman, Alexandru, et al. "Vision transformer assisting rheumatologists in screening for capillaroscopy changes in systemic sclerosis: an artificial intelligence model." Rheumatology 62.7 (2023): 2492-2500.

[2] Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2022). High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition.

[3] Navidi, Zeinab, et al. "MorphoDiff: Cellular Morphology Painting with Diffusion Models." The Thirteenth International Conference on Learning Representations.