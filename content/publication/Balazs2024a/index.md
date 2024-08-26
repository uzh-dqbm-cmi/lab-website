---
title: "Fragmentstein—facilitating data reuse for cell-free DNA fragment analysis"
date: 2024-01-15
publishDate: 2024-01-15
authors: 
- Zsolt Balazs
- Todor Gitchev
- Ivna Ivankovic
- Michael Krauthammer
publication_types: ["2"]
abstract: "Fragmentstein is a tool for converting non-sensitive cfDNA fragmentation data into BAM files, allowing for the analysis of copy number variants, nucleosome occupancy, and fragment length without compromising genomic data sensitivity."
featured: false
summary: "Method development for the analysis of cell-free DNA (cfDNA) sequencing data is impeded by limited data sharing due to the strict control of sensitive genomic data. An existing solution for facilitating data sharing removes nucleotide-level information from raw cfDNA sequencing data, keeping alignment coordinates only. This simplified format can be publicly shared and would, theoretically, suffice for common functional analyses of cfDNA data. However, current bioinformatics software requires nucleotide-level information and cannot process the simplified format. We present Fragmentstein, a command-line tool for converting non-sensitive cfDNA-fragmentation data into alignment mapping (BAM) files. Fragmentstein complements fragment coordinates with sequence information from a reference genome to reconstruct BAM files. We demonstrate the utility of Fragmentstein by showing the feasibility of copy number variant (CNV), nucleosome occupancy, and fragment length analyses from non-sensitive fragmentation data."
tags:
- Bioinformatics
- Data Sharing
publication: "*Bioinformatics*"
doi: "https://doi.org/10.1093/bioinformatics/btae017"
---
