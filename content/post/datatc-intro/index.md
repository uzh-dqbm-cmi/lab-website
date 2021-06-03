---
title: Data Traffic Control
summary: Whhrrrr... Voooooosh... That's the sound of your data coming and going exactly where it belongs
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

# ✈️ data traffic control

Data files are the building materials we work with *every day, all day*. Working with them should be *effortless*.

In my work as a data scientist, I kept encountering the same frustrations that slowed me down every day. 
Some were small, like having to look up a data file format read method multiple times a week. 
Larger frustrations cost me multiple days worth of work, like not having a record of how I generated a key data file, and spending multiple days trying to recreate it.
To make my every-day life easier - and so I can focus on the more interesting problems in data science! - I built data traffic control, a python package for data management magic.

Data traffic control solves 3 common problems & annoyances in interacting with data:

 1. Keeping track of finicky filepaths and filenames
 2. Having to look up data format read and write methods... over and over again...
 3. Guessing at how I generated a data file, and spending days trying to re-create it

Do you also have these frustrations? Data traffic control is here to help!
Let me give you a tour!


As data scientists, we have a different relationship with our code than most software engineers. 
We don't just build software- we talk in code. We 
We don't just write code to build software- we write code to ask questions, test a hypothesis, and see the result.
And like any other scientist, the speed and ease with which we can ask our questions and get our answers makes a big difference!

A filepath isn't just something we set once and it's done- it's something we have to remember and re-type every day to access that latest version of processed data.
We're constantly accessing and re-accessing data files from multiple environments - not only programatically in our code but also interactively 
We spend a lot of time coding interactively- in Jupyter or IPython

For example,
Say I just trained a model, and after taking a look at the results, I want to open it up and see what hyperparameters it landed on.
To access that file, I would open up `IPython` and type the following:
 
```python
import pickle
data_dir = '/cluster/dataset/tenant/projects/my_project'
with open(data_dir+'models/2021-03-01_16-55-32.pkl', 'rb+') as f:
    model = pickle.load(f)
```
That's 163 characters to type! Not to mention the annoyance of having to look up the time stamp of the lastest model filename.

Here's what the same code looks like in data traffic control:

```python
import datatc as dtc
dd = dtc.DataDirectory.load('my_project')
model = dd['models'].latest().load()
```

Down to only 99 characters of typing! And more importantly, a lot less to remember- no finicky filepaths, no obtuse file read syntax, and no timestamps to look up.

I know there have been times in my past where the feeling of having to remember and re-type that first code segment at 4pm - for the 7th time that day - is enough for me to think to myself "... eh, the model is probably fine", and keep me from being the thorough and rigorous of a data scientist.
 
This kind of simplicity makes the difference between me deciding "let me take a look to make sure that model trained correctly..." and "ehh I don't want to have to type all that... it was probably fine". Make the underlying work of accessing data files easy, so you save your energy for the real challenges of data science!

Curious how this works in data traffic control?


Data traffic control's interface for interacting with data directories is called `DataDirectory`.
To boot up a `DataDirectory`, just call load:

```python
import datatc as dtc
dd = dtc.DataDirectory.load('project_name')
```

For this magic to happen, you have to have once-upon-a-time registered this project with data traffic contol, by running:

```python
dtc.DataDirectory.register_project('project_name', '/path/to/project/data/dir/')
```

`DataDirectory` provides a pythonic way of interacting with your data directory interatively. 

Use `DataDirectory` to `ls` your project directory:

```python
dd.ls()
```

And you'll see your project data directory as a file tree:
```
raw/
    EntityViews/
        7 mixed items
    data_extracts/
        2019-11-23_Extract_3days/
            1 mixed items
        2020-01-05_Extract_3days_withHistory_v2/
            2 mixed items
        2020-02-04_Extract_3months/
            3 mixed items
```

Access the subdirectories using `[]`.


```python
dd['data_extracts'].ls()
```
```
data_extracts/
    2019-11-23_Extract_3days/
        2019-11-23_Extract_3days.xlsx
    2020-01-05_Extract_3days_withHistory_v2/
        2020-01-05_Extract_3days_withHistory_v2.xlsx
        2020-01-05_Extract_3days_withHistory_v2_sql.sql
    2020-02-04_Extract_3months/
        2020-02-04_Extract_3months.sql
        2020-02-04_Extract_3months.xlsx
        3_month_export.csv
```

And loading and saving files in your Data Directory is just as simple as `load` and `save`. 

To load a file, navigate the file system using `[]` operators, and then call `.load()`.


```python
raw_df = dd['data_extracts']['2020-02-04_Extract_3months']['2020-02-04_Extract_3months.xlsx'].load()
```

Don't worry about what format the file is in- `datatc` will intuit how to load the file.

Is your filename long and annoying to type? Use `.select('hint')` method to search for files & directories matching a substring.

For example,

```python
raw_df = dd['data_extracts']['2020-02-04_Extract_3months']['2020-02-04_Extract_3months.xlsx'].load()
```
can be shortened to...

```python
raw_df = dd['data_extracts']['2020-02-04_Extract_3months'].select('xlsx').load()
```
There is also a shortcut to load the latest file or subdirectory within a directory, with `.latest()`
*(if your data directory is organized by alphabetical time stamps)*

This means that 
```python
raw_df = dd['data_extracts']['2020-02-04_Extract_3months'].select('xlsx').load()
```
can be further shortened to:

```python
raw_df = dd['data_extracts'].latest().select('xlsx').load()
```





### Let's get some data


```python
import pandas as pd

raw_df = iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

raw_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
raw_sad = SelfAwareData(raw_df)
```

### Transform the data


```python
def normalize_sepal_dimensions(raw_df):
    """Normalize sepal dimensions"""
    df = raw_df.copy()
    df['sepal_length'] = df['sepal_length'] / df['sepal_length'].mean()
    df['sepal_width'] = df['sepal_width'] / df['sepal_width'].mean()
    return df

processed_sad = raw_sad.transform(normalize_sepal_dimensions, enforce_clean_git=False)
processed_sad.data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.872790</td>
      <td>1.144788</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.838562</td>
      <td>0.981247</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.804335</td>
      <td>1.046664</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.787222</td>
      <td>1.013956</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.855676</td>
      <td>1.177497</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



### Save!


```python
dd['data']['processed'].save(processed_sad, 'normalized_df.csv')
```

    created new SAD directory /Users/laurakinkead/Documents/Work/projects/datatc/data/processed/sad_dir__2021-02-17_22-26-19__normalized_df


### We've saved a data transform


```python
dd['data'].ls()
```

    data/
        area.csv              (2020-12-22 17:41)
        normalized_df.csv     (2020-05-11 09:56)
        processed/
            normalized_df.csv     (2021-02-17 22:26)
        re_sad.csv            (2020-12-22 17:11)
        re_sad_2.csv          (2020-12-22 17:32)
        re_sad_direct_3.csv   (2020-12-22 17:33)
        test.csv
        test.yaml
        test_no_index.csv
        test_pipe_separated.csv


Take a look under the hood...


```python
! ls /Users/laurakinkead/Documents/Work/projects/datatc/data/processed
```

    [1m[36msad_dir__2021-02-17_22-26-19__normalized_df[m[m



```python
! ls -l /Users/laurakinkead/Documents/Work/projects/datatc/data/processed/sad_dir__2021-02-17_22-26-19__normalized_df
```

    total 48
    -rw-r--r--  1 laurakinkead  staff  8795 Feb 17 22:26 data.csv
    -rw-r--r--  1 laurakinkead  staff   413 Feb 17 22:26 provenance.yaml
    -rw-r--r--  1 laurakinkead  staff  7264 Feb 17 22:26 sad.dill


### Load the saved data transform


```python
processed_sad = dd['data']['processed'].latest().load()
```

### Access the data


```python
processed_sad.data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.872790</td>
      <td>1.144788</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.838562</td>
      <td>0.981247</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.804335</td>
      <td>1.046664</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.787222</td>
      <td>1.013956</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.855676</td>
      <td>1.177497</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



### Want to know how a dataset was generated? Just take a look at the code!


```python
processed_sad.print_steps()
```

    --------------------------------------------------------------------------------
    Step  0               2021-02-17 22:26          no_git_hash
    --------------------------------------------------------------------------------
    def normalize_sepal_dimensions(raw_df):
        """Normalize sepal dimensions"""
        df = raw_df.copy()
        df['sepal_length'] = df['sepal_length'] / df['sepal_length'].mean()
        df['sepal_width'] = df['sepal_width'] / df['sepal_width'].mean()
        return df
    
    


### You can even use the saved data transform to reapply the transformer function to a new dataset


```python
raw_df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
processed_sad.rerun(raw_df).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.872790</td>
      <td>1.144788</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.838562</td>
      <td>0.981247</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.804335</td>
      <td>1.046664</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.787222</td>
      <td>1.013956</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.855676</td>
      <td>1.177497</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



# Summary

`data-traffic-control` automates every day interactions with your data

* Navigate your data directories with ease, without having to memorize long file paths

* Load data files without having to think about it (or looking it up yet again)

* Be certain of how a datafile was generated, and rest easy knowing you could reproduce it. 

