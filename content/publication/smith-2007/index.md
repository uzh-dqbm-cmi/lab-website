---
title: "Leveraging the structure of the Semantic Web to enhance information retrieval for proteomics."
date: 2007-11-01
publishDate: 2019-12-12T16:26:43.118935Z
authors: ["Andrew Smith", "Kei Cheung", "Michael Krauthammer", "Martin Schultz", "Mark Gerstein"]
publication_types: ["2"]
abstract: "MOTIVATION: Proteomics researchers need to be able to quickly retrieve relevant information from the web and the biomedical literature. To improve information retrieval, we leverage the structure of the semantic web, developing an approach for joining it with the largely opposing paradigm of unsupervised web search. RESULTS: Our approach uses a Resource-Description-Framework (RDF) graph that inter-relates documents through their associated biological identifiers (e.g., protein ID). A search begins with a simple query term (UniProt identifier), which is expanded with terms extracted from documents in the RDF graph surrounding the query (\"the subgraph\"). We re-rank documents in the full corpus (e.g. all PubMed) by their cosine-similarity scores against a composite word-weight vector created from the subgraph. This vector is a weighted sum of individual word-weight vectors for documents at each node of the subgraph, taking into account the types of relationships between the central query identifier and the nodes connected to it. The computation also uses inverse document frequency (IDF) in a novel way to rescale the local word frequencies in the query's subgraph relative to that in other subgraphs. Applying our procedure to PubMed, we optimize weights for various relationships in the subgraph and benchmark overall performance in detail. Using a subgraph containing family relationships (from PFAM) results in a significant improvement in accuracy (as compared to not considering the subgraph in the search) when assessed against known relationships in the yeast literature. Moreover, we achieve this accuracy using only relatively simple and computationally efficient methods."
featured: false
publication: "*Bioinformatics (Oxford, England)*"
tags: ["Artificial Intelligence", "Database Management Systems", "Databases", "Protein", "Information Storage and Retrieval", "Internet", "Natural Language Processing", "Proteins", "Proteomics", "chemistry", "classification", "metabolism", "methods"]
doi: "10.1093/bioinformatics/btm452"
---

