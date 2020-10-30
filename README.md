# teaching-colleagues

This repository contains examples of common Python operations.

If you want to play around with the code: 
- clone this repo to your computer
- build a virtual environment (described below)
- start playing around with the notebooks


If you're interested in contributing examples:
- make a fork of the repo into your own GitHub account
- modify your version and commit your changes to your personal fork
- when you're finished contributing, open up a pull request to get your new notebooks merged into this repo

## Content
- [general examples](examples/general)
    - `csv` module
    - `datetime` module
    - `list` comprehension
- [`pandas` examples](examples/pandas)
    - read files
    - merge multiple files
    - filter dataframes
    - aggregate dataframes
    - plot dataframes with `seaborn`
- [`SQL` through Python examples](<examples/SQL data>)
    - Use `psycopg2` to make a new PostgreSQL database
    - Use `sqlalchemy` to write a `pandas` dataframe to SQL
    - Query data stored within a SQL database


## Setup

If you don't have `conda` on your computer, follow [this link](https://docs.conda.io/en/latest/miniconda.html)
and download/install the latest version of `miniconda`.
Make sure to use the version that matches your operating system and bit size.

To install a Python environment with all necessary dependencies, execute the following command:

```shell script
(base) $ conda env create -f env.yml
```

This command installs all of the modules listed in [`env.yml`](env.yml)

Now that you've created the environment, you can activate it and start using notebooks with the following commands:

``` shell script
(base) $ conda activate teaching
(teaching) $ jupyter lab
```

For a more detailed explanation of Python environments, as well as a 
step-by-step installation process, follow the [installation instructions](documentation/installation.md).

## Resources
Additional web-based resouces can be found [here](documentation/resources.md)