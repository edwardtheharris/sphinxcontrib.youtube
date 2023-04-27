---
abstract: This package allows inserting YouTube videos into Sphinx documents.
authors: xander.harris@databricks.com
---

# Sphinx-Contrib YouTube

```{note}
This package was forked from
[this fork](https://github.com/divi255/sphinxcontrib.youtube/)
of the [original](https://github.com/shomah4a/sphinxcontrib.youtube).
```

## Usage

Mostly because I don't feel like making a new package on PyPi, the installation
for this is a little funky. You've got a couple of choices, first is to
clone this repository then install it into your virtual environment[^pipenv],
as an editable package like this.

1. Clone the repository.

    ```{code-block} shell
    src_dir="~/Documents/src/github.com/edwardtheharris/sphinxcontrib.youtube"
    git clone https://github.com/edwardtheharris/sphinxcontrib.youtube "$src_dir"
    ```

2. Update your working directory.

    ```{code-block} shell
    cd "$src_dir"
    ```

3. Create your virtual environment, perhaps by creating some local copies of
   a few handy wheels.

    ```{code-block} shell
    python3.10 -m pip install -U pip pipenv
    python3.10 -m pipenv --python 3.10 run pip wheel -w wheels/sphinx -f wheels/sphinx myst-parser
    python3.10 -m pipenv --python 3.10 run pip wheel -w wheels/sphinx -f wheels/sphinx myst-nb
    python3.10 -m pipenv --python 3.10 run pip wheel -w wheels/sphinx -f wheels/sphinx sphinx
    ```

4. Install Sphinx into your new virtual environment.

    ```shell
    pip3 install sphinxcontrib.yt
    ```

```{toctree}
CHANGELOG
contributing
license
security
semver
```
