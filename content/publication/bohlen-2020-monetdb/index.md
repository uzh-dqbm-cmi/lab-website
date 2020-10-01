---
title: " Iterations for Propensity Score Matching in MonetDB"
date: 2020-08-17
publishDate: 2019-12-12T16:26:43.106027Z
authors: 
- Böhlen, Michael H.
- Dolmatova, Oksana
- Krauthammer, Michael
- Mariyagnanaseelan, Alphonse
- Stahl, Jonathan
- Surbeck, Timo
publication_types: ["2"]
abstract: The amount of data that is stored in databases and must be analyzed is growing fast. Many analytical tasks are based on iterative methods that approximate optimal solutions. Propensity score matching is a technique that is used to reduce bias during cohort building. The main step is the propensity score computation, which is usually implemented via iterative methods such as gradient descent. Our goal is to support efficient and scalable propensity score computation over relations in a column-oriented database. To achieve this goal, we introduce shape-preserving iterations that update values in existing tuples until a fix point is reached. Shape-preserving iterations enable gradient descent over relations and, thus, propensity score matching. We also show how to create appropriate input relations for shape-preserving iterations with randomly initialized relations. The empirical evaluation compares in-database iterations with the native implementation in MonetDB where iterations are flattened.
featured: false
publication: "Advances in Databases and Information Systems. ADBIS 2020. Lecture Notes in Computer Science"
url_source: "https://link.springer.com/chapter/10.1007/978-3-030-54832-2_15"
doi: "https://doi.org/10.1007/978-3-030-54832-2_15"
---

