# -*- coding: utf-8 -*-
"""
This code plots the time and memory complexity (via number of conditionals and assignments)
for bubblesort and quicksort. It iterates through list sizes from 100-1000 in steps
of 100. For each list size, it randomly generates 100 lists in order to calculate means
and standard deviations for plotting. The data are plotted with and without normalization
to the expected complexity.
"""
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
import math
from example import algs

# Initialize variables 
bbl_mean = []
bbl_std = []
qcksrt_mean = []
qcksrt_std = []
cond_bubble_mean = []
cond_bubble_std = []
assign_bubble_mean = []
assign_bubble_std = []
cond_quick_mean = []
cond_quick_std = []
assign_quick_mean = []
assign_quick_std = []
bbl_norm = []
bbl_norm_mean = []
bbl_norm_std = []
quicksort_norm = []
quicksort_norm_mean = []
quicksort_norm_std = []
bbl_cond_norm = []
bbl_cond_norm_mean = []
bbl_cond_norm_std = []
bbl_assign_norm = []
bbl_assign_norm_mean = []
bbl_assign_norm_std = []
quicksort_cond_norm = []
quicksort_cond_norm_mean = []
quicksort_cond_norm_std = []
quicksort_assign_norm = []
quicksort_assign_norm_mean = []
quicksort_assign_norm_std = []


# Set list of input list lengths to test
trials = np.array([100,200,300,400,500,600,700,800,900,1000])

for n in trials:
    
    timer_quicksort = []
    timer_bubble=[]
    
    cond_bubble_list = []
    assign_bubble_list = []
    
    cond_quick_list = []
    assign_quick_list = []
    
    cond_bubble=0
    assign_bubble=0
    
    # Generate 100 lists for each input length to generate means and stdev
    for x in range (100):
        
        lst = [] 
        
        # Generate list of n random integers
        for k in range(n):
            lst.append(random.randint(0,10000))
        
        lst2=lst[:] # Copy list for quicksort
        
        # Run and time Bubblesort
        start_time1 = timeit.default_timer()
        cond_bubble,assign_bubble=(algs.bubblesort(lst))
        time_bbl = timeit.default_timer() - start_time1
        timer_bubble.append(timeit.default_timer() - start_time1)
        
        # Run and time Quicksort using rightmost value in lst as pivot
        r = n-1 # right-most index in list
        p=0
        start_time2 = timeit.default_timer()
        c_quick, a_quick = algs.quicksort(lst2,p,r)
        time_quicksort = timeit.default_timer() - start_time2
        timer_quicksort.append(timeit.default_timer() - start_time2)
        
        cond_bubble_list.append(cond_bubble)
        assign_bubble_list.append(assign_bubble)
        
        cond_quick_list.append(c_quick)
        assign_quick_list.append(a_quick)
        
        # Normalize runtimes and assig/cond to expected complexity        
        bbl_norm.append(time_bbl/math.pow(n,2))
        quicksort_norm.append(time_quicksort/(n * math.log10(n)))
        
        bbl_cond_norm.append(cond_bubble/math.pow(n,2))
        quicksort_cond_norm.append(c_quick/(n * math.log10(n)))
        
        bbl_assign_norm.append(assign_bubble/math.pow(n,2))
        quicksort_assign_norm.append(a_quick/(n * math.log10(n)))
    
   
    # Calculate mean and stdev for run time, conditionals, and assignments of 
    # each sorting algorithm
    bbl_norm_mean.append(np.mean(bbl_norm))
    bbl_norm_std.append(np.std(bbl_norm))
    
    bbl_cond_norm_mean.append(np.mean(bbl_cond_norm))
    bbl_cond_norm_std.append(np.std(bbl_cond_norm))
    
    bbl_assign_norm_mean.append(np.mean(bbl_assign_norm))
    bbl_assign_norm_std.append(np.std(bbl_assign_norm))   
        
    quicksort_norm_mean.append(np.mean(quicksort_norm))
    quicksort_norm_std.append(np.std(quicksort_norm)) 
    
    quicksort_cond_norm_mean.append(np.mean(quicksort_cond_norm))
    quicksort_cond_norm_std.append(np.std(quicksort_cond_norm))
    
    quicksort_assign_norm_mean.append(np.mean(quicksort_assign_norm))
    quicksort_assign_norm_std.append(np.std(quicksort_assign_norm))

    bbl_mean.append(np.mean(timer_bubble))
    bbl_std.append(np.std(timer_bubble))
    
    qcksrt_mean.append(np.mean(timer_quicksort))
    qcksrt_std.append(np.std(timer_quicksort))    
    
    cond_bubble_mean.append(np.mean(cond_bubble_list))
    cond_bubble_std.append(np.std(cond_bubble_list))
    
    assign_bubble_mean.append(np.mean(assign_bubble_list))
    assign_bubble_std.append(np.std(assign_bubble_list))
    
    cond_quick_mean.append(np.mean(cond_quick_list))
    cond_quick_std.append(np.std(cond_quick_list))
    
    assign_quick_mean.append(np.mean(assign_quick_list))
    assign_quick_std.append(np.std(assign_quick_list))

# Generate figures
plt.figure(0)
plt.errorbar(trials,bbl_mean,bbl_std)
plt.title("Time complexity of bubblesort")
plt.xlabel("Number of values in list")
plt.ylabel("Runtime (mean and stdev over 100 input lists)")
plt.savefig('Bubblesort_time')

plt.figure(1)
plt.errorbar(trials,qcksrt_mean,qcksrt_std)
plt.title("Time complexity of quicksort")
plt.xlabel("Number of values in list")
plt.ylabel("Runtime (mean and stdev over 100 input lists)")
plt.savefig('Quicksort_time')

plt.figure(2)
plt.errorbar(trials,bbl_mean,bbl_std)
plt.errorbar(trials,qcksrt_mean,qcksrt_std)
plt.title("Comparing time complexities of bubblesort and quicksort")
plt.legend(['bubblesort','quicksort'],loc='upper left')
plt.xlabel("Number of values in list")
plt.ylabel("Runtime (mean and stdev over 100 input lists)")
plt.savefig('bubble_vs_quicksort_time')

plt.figure(3)
plt.errorbar(trials,cond_bubble_mean,cond_bubble_std)
plt.errorbar(trials,assign_bubble_mean, assign_bubble_std)
plt.legend(['# of conditionals','# of assignments'],loc='upper left')
plt.title("Number of conditionals and assignments in bubblesort")
plt.xlabel("Number of values in list")
plt.ylabel("Count (mean and stdev over 100 input lists)")
plt.savefig('bubble_cond_assign')

plt.figure(4)
plt.errorbar(trials,bbl_cond_norm_mean,bbl_cond_norm_std)
plt.errorbar(trials, bbl_assign_norm_mean, bbl_assign_norm_std)
plt.legend(['# of conditionals','# of assignments'],loc='upper left')
plt.title("Normalized conditionals and assignments in bubblesort")
plt.xlabel("Number of values in list")
plt.ylabel("Normalized count (mean and stdev over 100 input lists)")
plt.savefig('bubble_cond_assign_normalized')

plt.figure(5)
plt.errorbar(trials,quicksort_cond_norm_mean,quicksort_cond_norm_std)
plt.errorbar(trials, quicksort_assign_norm_mean, quicksort_assign_norm_std)
plt.legend(['# of conditionals','# of assignments'],loc='upper left')
plt.title("Normalized conditionals and assignments in quicksort")
plt.xlabel("Number of values in list")
plt.ylabel("Normalized count (mean and stdev over 100 input lists)")
plt.savefig('quicksort_cond_assign_normalized')

plt.figure(6)
plt.errorbar(trials,cond_quick_mean,cond_quick_std)
plt.errorbar(trials,assign_quick_mean, assign_quick_std)
plt.legend(['# of conditionals','# of assignments'],loc='upper left')
plt.title("Number of conditionals and assignments in quicksort")
plt.xlabel("Number of values in list")
plt.ylabel("Count (mean and stdev over 100 input lists)")
plt.savefig('quicksort_cond_assign')


plt.figure(7)
plt.errorbar(trials,bbl_norm_mean,bbl_norm_std)
plt.title("Time complexity of bubblesort normalized to n^2")
plt.xlabel("Number of values in list")
plt.ylabel("Runtime (mean and stdev over 100 input lists)")
plt.savefig('bubblesort_normalized')

plt.figure(8)
plt.errorbar(trials,quicksort_norm_mean,quicksort_norm_std)
plt.title("Time complexity of quicksort normalized to n(logn)")
plt.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
plt.xlabel("Number of values in list")
plt.ylabel("Runtime (mean and stdev over 100 input lists)")
plt.savefig('quicksort_normalized')
