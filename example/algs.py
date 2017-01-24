import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(lst_bubble):
    """
    Implements bubblesort algorithm. Goes through entire input list, lst_bubble, 
    one element at a time, starting from the left and moving right. Each element
    is compared to its neighbor on the right. If the element on the left is 
    greater than the element to its right, they are swapped. Since the highest value 
    will always ultimately be moved to its correct position, each round the list
    need only be iterated through (length of list - iteration), which saves computation
    time. The end result is a list sorted from smallest to greatest.
    
    This function also counts the conditionals and assignments for the hw writeup.
    """
    n = len(lst_bubble)
    if all(type(item)!=str for item in lst_bubble) != True:
        return
    else:
        cond = 0
        assign = 0
        for i in range(n):
            for j in range(1,n-i):
                cond +=1
                if lst_bubble[j-1] > lst_bubble[j]:
                    lst_bubble[j],lst_bubble[j-1] = swap(lst_bubble[j],lst_bubble[j-1])
                    assign +=3
        return (cond, assign)
    
    
def partition(lst_part, p, r):
    """
    This is part of the quicksort algorithm. This partition function goes through
    the input list, lst_part, and sets the right-most value in the list as the pivot.
    The input list is then iterated through from the left-most value (p) to the right. The 
    values in the list are then separated by their relationship to (greater or lesser than) the pivot value.
    The location of the split is maintained by pivot_index. This partitioning is done by swapping
    any values less than the pivot value with the value at pivot index, keeping the pivot index
    as the partition, to the right of all values less than pivot. Any values greater than
    the pivot value are left in place, to the right of pivot_index. For helpful video,
    see: https://www.youtube.com/watch?v=COk73cpQbFQ.
    
    This function also counts the conditionals and assignments for the hw writeup.
    """
    cond_part = 0
    assign_part = 0
    pivot = lst_part[r] # Set pivot to last (right-most) value in list
    pivot_index = p
    for j in range(p,r):
        cond_part +=1
        if lst_part[j] <= pivot:
            lst_part[pivot_index],lst_part[j] = swap(lst_part[pivot_index],lst_part[j])  
            assign_part +=3
            pivot_index += 1    
    lst_part[pivot_index],lst_part[r] = swap(lst_part[pivot_index],lst_part[r])
    assign_part +=3
    return pivot_index,cond_part,assign_part
    
def quicksort(lst2, p, r):
    """
    This, along with the partition function, implements the quicksort algorithm.
    As long as we are not at the end of the list (r>p), this function calls partition
    to split the list into 2 parts, one containing values greater and one containg 
    values lesser than the pivot value (set in partition). This function recursively
    calls itself to sort these 2 sub-lists using partition...until all values in
    the list are sorted.
    
    This function also counts the conditionals and assignments for the hw writeup.
    """
    if all(type(item)!=str for item in lst2) != True:
        return
    else:
        cond_quick = 0
        assign_quick = 0
        assign_quick +=1
        if (r>p):
            pivot, c_qck, a_qck = partition(lst2,p,r)
            cond_quick += c_qck
            assign_quick += a_qck
            c_qck, a_qck = quicksort(lst2, p, pivot-1)
            cond_quick += c_qck
            assign_quick += a_qck
            c_qck, a_qck = quicksort(lst2, pivot+1,r)
            cond_quick += c_qck
            assign_quick += a_qck
        return cond_quick, assign_quick


def swap(a,b):
    """
    This function simply swaps two values within a list
    """
    temp = a
    a = b
    b = temp
    return(a,b)