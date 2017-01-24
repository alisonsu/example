# example
## edited to recommit to run Travis correctly

[![Build
Status](https://travis-ci.org/alisonsu/example.svg?branch=master)](https://travis-ci.org/alisonsu/example)

HW1 Bubblesort and Quicksort with testing

## usage

To use the package, first run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `example/__main__.py`) can be run as follows

```
python -m example
```
This runs bubblesort and quicksort on a list of 10 randomly generated values.


## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project. This tests typical edge cases for both bubblesort and quicksort.
