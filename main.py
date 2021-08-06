import random
import time
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd 
import scipy.stats as stats

from bubble import BubbleSort
from insertion import InsertionSort
from merge import MergeSort
from quicksortinsert import QuickSortInsertion
from quicksort import QuickSort


class SortType:
    def __init__(self, _name_type = "none", _sort_times =[]):
        self.name_type = _name_type
        self.sort_times = _sort_times
    

class Sorter:

    def bubble_sort(self, array) :
        sorter = BubbleSort()
        return sorter.bubble_sort(array)

    def merge_sort(self, array) :
        sorter = MergeSort()
        return sorter.merge_sort(array)

    def insertion_sort(self, array):
        sorter = InsertionSort()
        return sorter.insertion_sort(array)

    def quick_sort(self, array):
        sorter = QuickSort()
        return sorter.quick_sort(array)

    def hybrid_quick_sort(self, array):
        sorter = QuickSortInsertion()
        return sorter.hybrid_quick_sort(array)


print("Sort Comparisons")
s = Sorter()

BASE_SIZE = 1000
LOOP_SIZE = 5
NANO_TO_MS = 1000000
NUM_AVERAGES = 1
OUTLIER_Z_SCORE = 66

def remove_outliers_z_score(data, z_score):
    #find absolute value of z-score for each observation
    z = np.abs(stats.zscore(data))
    #only keep rows in dataframe with all z-scores less than absolute value of 3 
    clean_data = []
    for i in range( len(z) ):
        if z[i] < z_score:
            clean_data.append(data[i])
    return clean_data

def remove_outliers_inner_quartile(data):
    #find Q1, Q3, and interquartile range for each column
    Q1 = data.quantile(q=.25)
    Q3 = data.quantile(q=.75)
    IQR = data.apply(stats.iqr)
    #only keep rows in dataframe that have values within 1.5*IQR of Q1 and Q3
    data_clean = data[~((data < (Q1-1.5*IQR)) | (data > (Q3+1.5*IQR))).any(axis=1)]
    return data_clean

def plot_test_times( test_times, array_sizes):
    plt.plot (array_sizes, test_times )
    plt.show()

def make_random_arrays(BASE_SIZE, LOOP_SIZE):
    array_sizes = []
    rand_arrays = []
    for i in range(1,1+LOOP_SIZE):
        test_size = BASE_SIZE * (i)
        array_sizes.append(test_size)
        rand_array = [random.randint(0,test_size) for i in range(test_size)]
        rand_arrays.append(rand_array)
    return rand_arrays, array_sizes

def sort_run(fn, rand_arrays, runs):
    sorted_array_test_times = []
    for rand_array in rand_arrays:
        run_list = []
        for j in range(runs):
            rand_array_copy = rand_array.copy()
            start_time = time.perf_counter_ns()
            sorted_rand_array = fn(rand_array_copy)
            stop_time = time.perf_counter_ns()
            test_time = (stop_time - start_time) / NANO_TO_MS
            run_list.append(test_time)
        test_time = statistics.mean(run_list)
        sorted_array_test_times.append(test_time)
    return sorted_array_test_times

sorted_array_test_times = []

rand_arrays, array_sizes = make_random_arrays(BASE_SIZE, LOOP_SIZE)
sorted_array_test_times_bubble = sort_run(s.bubble_sort, rand_arrays, NUM_AVERAGES)
sorted_array_test_times_merge = sort_run(s.merge_sort, rand_arrays, NUM_AVERAGES)
sorted_array_test_times_insert = sort_run(s.insertion_sort, rand_arrays, NUM_AVERAGES)
sorted_array_test_times_quick = sort_run(s.quick_sort, rand_arrays, NUM_AVERAGES)
sorted_array_test_times_quick_hybrid = sort_run(s.hybrid_quick_sort, rand_arrays, NUM_AVERAGES)

sort_times_df = pd.DataFrame()
sort_times_df['bubble'] = sorted_array_test_times_bubble
sort_times_df['merge'] = sorted_array_test_times_merge
sort_times_df['insert'] = sorted_array_test_times_insert
sort_times_df['quick'] = sorted_array_test_times_quick
sort_times_df['quick-insert'] = sorted_array_test_times_quick_hybrid

plt.plot(array_sizes, sort_times_df['bubble'], label='bubble', color='red')
plt.plot(array_sizes, sort_times_df['merge'], label='merge', color='steelblue')
plt.plot(array_sizes, sort_times_df['insert'], label='insert', color='purple')
plt.plot(array_sizes, sort_times_df['quick'], label='quick', color='orange')
plt.plot(array_sizes, sort_times_df['quick-insert'], label='quick + insert', color='green')
plt.legend()
plt.ylabel('Milliseconds')
plt.xlabel('Array Size')
plt.title('Sorting Times')
plt.show()
exit(0)


