---
title: Book Review: Causality, Probability and Medicine by Donald Gillies
authors: 
- matthiasdittberner
date: 2020-04-29
tags: 
- Talks
categories:
- Talks
image:
  placement: 1
  caption: 
  focal_point: ""
  preview_only: false
projects: []
---


I read Donald Gillies’ book “Causality, Probability and Medicine” a while ago
and wanted to give a brief comment and overview of the content. There is no
conflict of interest, this blog post simply represents my personal experience.
I am neither promoting the book nor have I received funding for this article.


## About the author

Donald Gillies studied Mathematics as well as Philosophy of Science at King’s
College Cambridge and received his PhD from Cambridge University. He currently
is Emeritus Professor of Philosophy of Science and Mathematics at University
College London. His major research area spans philosophy of probability
especially Bayesian networks and causality. Furthermore, he has worked in
philosophy of mathematics, philosophy of artificial intelligence (AI) and
philosophy of medicine.


## About the content

The book provides an overview of the historical development of causality in
medicine. It illustrates the history and philosophy of science by giving
examples from research conducted by Robert Koch on cholera and others as well as
the probabilistic causality of smoking and lung cancer. Furthermore, the book
explains applications of probability and causality in medicine.

The typical proposition that is taught in statistics courses states is that
correlation does not equal causation. Although one might think that causality
and probability do not intertwine, they can be related. Gilles explains that one
has to distinguish between deterministic and indeterministic causality. The
first, and probably most commonly known, follows the Newtonian view of the
world, where action equals reaction. That means whenever **A** occurs **B**
follows under same conditions, e.g. a stone will fall if it is thrown from a
cliff. Indeterministic causality on the other hand states, that **B** does not
always follows when **A** occurs. One can think of the case where smoking causes
lung cancer. Although this only occurs in approximately 5% of the cases, most
people would agree that this is a valid statement.

The book only considers general causation specifically causal laws that apply in
general settings rather than in specific circumstances. In that regard, Gillies
presents 3 categories of the theory of causality and illustrates the approaches.
Furthermore, he assesses the advantages and disadvantages of the competing
theories and undermines their development with examples from history of science.

The first category is the so-called AIM-theory, that takes a deterministic
approach. Here, Causality depends on Action, Intervention and Manipulation (AIM).
**A** causes or acts on **B** if and only if one can intervene on **A** such
that **B** changes (is manipulated).

Collingwood’s Principle of Interventional Evidence states: “A causal law cannot
be taken as established unless it has been confirmed by some interventional
evidence.” Objections with this theory include that in certain cases humans
cannot manipulate the cause for instance that the moon causes tides.
Furthermore, it should be considered that the past cannot be altered, meaning if
**A** occurs at time **T1** then **B** has to occur at time **T2** >= **T1**.
Another important feature is, that causality is usually asymmetrical i.e. **A**
causes **B** but not necessarily that **B** causes **A**.

The second category is a mechanistic theory, that states: **A** causes **B** if
and only if there exists a mechanism **M**, which links **A** to **B**:
**A → M → B**. The Wesley Salmon’s dog whistle example illustrates the
principle: A dog owner blows a dog whistle so that the dog arrives. To humans it
seems that blowing the whistle causes the dog to come. The problem with this
theory is that it relies too much on physical causality. Humans cannot hear that
whistle, since its frequency is too high to be audible for humans. In medicine
causal mechanisms are not necessarily physical but rather involve higher level
biochemical and physiological changes. Other types of mechanisms should be
allowed, for instance psychological or social ones.

In addition, confirmation and disconfirmation of causal hypothesis is equally
important. To validate the hypothesis, statistical evidence and evidence of
mechanisms can be used. The latter (dis)confirms correctness of a postulated
mechanism, for example through laboratory experiments. Both types can
furthermore be classified into observational, where a cohort for instance is
simply observed without any intervention, or interventional evidence e.g.
randomized controlled trials (RCT). Table 1 provides examples for the classes
of evidence.

Establishing a causal link does not have to originate simply from one type of
evidence. The evidence can be strengthened by combining multiple types of
evidence. In some cases, certain types of evidence are not even applicable. As
an example: There exists a high correlation of persons smoking and having lung
cancer (observational evidence), but is there also a mechanism, that links
smoking and cancer? RCTs would not be an option for additional evidence, because
we can’t force people randomly to smoke.

**Table 1: Examples for classes of evidence.**
|                       | Observational           | Interventional                                          |
|-----------------------|-------------------------|---------------------------------------------------------|
| Statistical evidence  | Epidemiological surveys | Clinical trials                                         |
| Evidence of Mechanism | Autopsies               | Laboratory experiments on animals, tissues, cells, etc. |

The third and last category is an indeterministic approach that links
probability and causality. The probabilistic theory of causality dates back to
Irving John Good in 1959. He understood causality in terms of propensity, i.e.
things tend to happen more frequently under certain conditions. **A** causes
**B** if and only if P(**B**|**A**) > P(**B**|~**A**) – This is also known as
the Causality Probability Connection Principle (CPCP or CP2). So, if we would
have a probability of P(**B**|**A**) = 1, we would conclude that there exists
deterministic causality. There is a problem with this approach though. Let’s
imagine a backyard where we can observe rain and mud (P(rain) > 0, P(mud) > 0).
In that case we can also define how likely it is to rain if we observe mud
P(rain|mud) and contrary if we observe rain what the chance is to also see mud
P(mud|rain). The problem is that only P(mud|rain) is causal. Causality is
asymmetrical, while probability is symmetrical. This raised the doubt that one
can define causality in terms of probability.

Judea Pearl is a harsh critic of the probabilistic causality and suggested a
different way called structural theory of causation. He devised causal and
Bayesian networks in the 1980s by interpreting probabilities of causal models
as beliefs. This approach is very popular among AI researchers because it
provides a mathematical language that can be implemented in computers. It is
criticized in other research communities due to a Markov condition (which
requires random variable to be independent), which might not hold in the reality.

This should just give an overview of the scope of the book. Obviously, a lot
more details would be required to understand the aspects toughly. Thus, I
encourage the reader to pick up Gillies book or consult additional references.


## Comment

This book provides an insightful overview about the history of science and
different streams of causal theory. Most importantly, no specific knowledge of
statistics, mathematics, causality or medicine is required, which makes this
content very accessible. The concepts are presented in a very intuitive way,
thus making it approachable to a broader audience of physicians, philosophers
or computer scientists for instance. This book will not be suitable for readers
who are looking for a mathematical or computational theory of causality. It is
definitely educational since it gives a clear explanation of opportunities and
problems of causality.

I recommend this book to any person interested in causality in general or
specifically in the medical domain. I think it is a wonderful read for medical
students, physicians, study nurses, engineers, computer or data scientists that
work in the medical domain.


## References

Author: Donald A. Gillies
Title: Causality, Probability, and Medicine
Hardcover: 316 pages
Publisher: Routledge; 1 edition (August 14, 2018)
Language: English
ISBN-10: 1138829285
ISBN-13: 978-1138829282
