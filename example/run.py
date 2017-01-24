# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)
    
    x = np.random.rand(10)
    r = len(x)-1
    p=0
    
    lst2=x[:]

    print("Unsorted input: ", x)
    
    bubblesort(x)
    quicksort(lst2,p,r)

    print("Bubble sort output: ", x)
    print("Quick sort output: ", lst2)
