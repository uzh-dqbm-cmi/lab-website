---
title: Data Traffic Control- a python library for human-friendly data interactions
summary: Data files are the building materials we work with every day, all day. Working with them should be effortless.
authors: 
- laurakinkead
date: 2021-06-22
tags: 
- Reproducibility
- Data Science
categories:
- Research
projects: []
---

One of my least favorite things to do in my job as a Data Scientist is to open data files. I open data files dozens of times a day- to check on model results, modify configs, and view log files. And yet for being such a common task, it always fills me with a small amount of disgruntlement.

Consider an example. Let's say I just trained a model, which I saved to the filesystem as a `.pkl`. I want to open it up and see what hyper-parameters it landed on. To access that file, I would open up IPython and type the following:

```python
import pickle
data_dir = '/cluster/dataset/tenant/projects/my_project'
with open(data_dir+'models/2021-03-01_16-55-32.pkl', 'rb+') as f:
    model = pickle.load(f)

```

That's 163 characters to type, just to open a file! Not to mention the annoyance of having to look up the time stamp of the latest model filename, and the frustration of remembering _"Does pickle use `r` mode, or `rb`, or `rb+` ...?"_ That is one snippet of code I am _not_ happy about writing and re-writing multiple times every day.


I didn't become a computer scientist to memorize long tedious strings- I became a computer scientist to automate all the things! That's why I built **data traffic control**- a python library that automates everyday interactions with your data.

Here's what the same data file access looks like in data traffic control:

```python
import datatc as dtc
dd = dtc.DataDirectory.load('my_project')
model = dd['models'].latest().load()

```

That's almost half as much typing! And more importantly, a lot less to remember- no finicky filepaths, no obtuse file read syntax, and no long timestamped filenames to look up.

Data files are the building materials we work with every day, all day. Working with them should be _effortless_.

## data traffic control: a tour
Curious how data traffic control makes data interactions easier? Let's take a closer look.

### Navigate your data directories with ease, without having to memorize long file paths
Data traffic control remembers your project data directories for you. The first time you use data traffic control for your project, register that project's data directory:

```python
import datatc as dtc
dtc.DataDirectory.register_project('project_name', '/path/to/project/data/dir/')
```
From then on, you can boot up a data traffic control `DataDirectory` object with a simple `load` call:
```python
dd = dtc.DataDirectory.load('project_name')
```

Why do I need this `DataDirectory` object, you ask? `DataDirectory` provides a human-friendly interface for easily accessing your files.

For example, `DataDirectory` can `ls` your project directory and print a nicely formatted file tree:
```
>>> dd.ls()
project_data/
    raw/
        iris.csv
    processed/
        clean_iris.csv
        clean_iris_bugfix.csv
    feature_sets/
        features.csv
        new_features.csv
        features_bugfix.csv
    models/
        2019-11-05_model.pkl
        2019-11-27_model_v2.pkl
        2019-12-04_model_v3.pkl
        2020-01-13_model_final.pkl
        2020-01-16_model_final2.pkl
```

### Load data files without having to think about it (or looking up the syntax yet again)

Navigate the subdirectories using `[]`. Once you've located the right file, just call `.load()`. Don't worry about what format the file is in- data traffic control will intuit how to load the file!

For example, you could access the `clean_iris_bugfix.csv` file like this:

```python
processed_df = dd['processed']['clean_iris_bugfix.csv'].load()
```

If that's too much typing (I admire your high standards), you can use helper methods like `select` and `latest` to quickly access the file you want.

#### The _select_ shortcut
For example, you can access the `features_bugfix.csv` file like this:

```python
features_df = dd['feature_sets']['features_bugfix.csv'].load()
```

...or you can use the `select` shortcut, which matches filenames with a search substrings:

```python
features_df = dd['feature_sets'].select('bugfix').load()
```

#### The _latest_ shortcut

Similarly, you could open up the latest model file by writing:

```python
latest_model = dd['models']['2020-01-16_model_final2.pkl'].load()
```

... or use the `latest` shortcut to get there faster:

```python
latest_model = dd['models'].latest().load()
```

#### Saving files

Saving files works the same way. Navigate to the destination directory, and call save with your data object and a name.

```python
dd['feature_sets'].save(new_features_df, 'new_features.csv')

```
## `pip install datatc`
Could data traffic control save you time interacting with your data files? Install it and give it a whirl!

`pip install datatc`

You can also find the full documentation on [readthedocs.io](https://data-traffic-control.readthedocs.io/)
