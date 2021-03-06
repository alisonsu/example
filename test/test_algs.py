import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():

    # Test empty array
    x = []
    algs.bubblesort(x)
    
    # Test single element array:
    x = [4]
    algs.bubblesort(x)
    
    # Test sorted array:
    x = [0,1,2,3]
    algs.bubblesort(x)
    
    # Test negative elements in array:
    x = [0, 6, 3, -5, 2]
    algs.bubblesort(x)
    
    # Test duplicated elements in array:
    x = [4, 5, 4, 6, 10, 3]
    algs.bubblesort(x)
    
    # Test floats in array:
    x = [0.4, -3, 0.4, 10]
    algs.bubblesort(x)

def test_quicksort():
    p=0
    
    # Test empty array:
    x = []
    r = len(x)-1 
    algs.quicksort(x,p,r)
    
    # Test single element array:
    x = [4]
    r = len(x)-1
    algs.quicksort(x,p,r)
    
    # Test sorted array
    x = [0,1,2,3]
    r = len(x)-1
    algs.quicksort(x,p,r)
    
    # Test negative elements in array
    x = [0, 6, 3, -5, 2]
    r = len(x)-1
    algs.quicksort(x,p,r)

    # Test duplicated elements in array:
    x = [4, 5, 4, 6, 10, 3]
    r = len(x)-1
    algs.quicksort(x,p,r)
    
    # Test floats in array:
    x = [0.4, -3, 0.4, 10]
    r = len(x)-1
    algs.quicksort(x,p,r)
    