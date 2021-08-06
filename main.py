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

NANO_TO_MS = 1000000

class SortType:
    def __init__(self, _name_type = "none", _sort_times =[]):
        self.name_type = _name_type
        self.sort_times = _sort_times
    

class Sorter:

    def __init__(self):
        pass

    def bubble_sort(self, array, odata) :
        sorter = BubbleSort()
        return sorter.bubble_sort(array, odata)

    def merge_sort(self, array, odata) :
        sorter = MergeSort()
        return sorter.merge_sort(array, odata)

    def insertion_sort(self, array, odata):
        sorter = InsertionSort()
        return sorter.insertion_sort(array, odata)

    def quick_sort(self, array, odata):
        sorter = QuickSort()
        return sorter.quick_sort(array, odata)

    def hybrid_quick_sort(self, array, odata):
        sorter = QuickSortInsertion()
        return sorter.hybrid_quick_sort(array, odata)

    def make_random_arrays(self, BASE_SIZE, LOOP_SIZE):
        array_sizes = []
        rand_arrays = []
        for i in range(1,1+LOOP_SIZE):
            test_size = BASE_SIZE * (i)
            array_sizes.append(test_size)
            rand_array = [random.randint(0,test_size) for i in range(test_size)]
            rand_arrays.append(rand_array)
        return rand_arrays, array_sizes 

    def sort_run(self, fn, rand_arrays, runs, odata=0):
        sorted_array_test_times = []
        for rand_array in rand_arrays:
            run_list = []
            for j in range(runs):
                rand_array_copy = rand_array.copy()
                start_time = time.perf_counter_ns()
                sorted_rand_array = fn(rand_array_copy, odata)
                stop_time = time.perf_counter_ns()
                test_time = (stop_time - start_time) / NANO_TO_MS
                run_list.append(test_time)
            test_time = statistics.mean(run_list)
            sorted_array_test_times.append(test_time)
        return sorted_array_test_times

    def get_sort_comparisons_times(self, base_size, loop_size, num_averages):
        rand_arrays, array_sizes = self.make_random_arrays(base_size, loop_size)
        #sorted_array_test_times_bubble = self.sort_run(s.bubble_sort, rand_arrays, num_averages)
        #sorted_array_test_times_insert = self.sort_run(s.insertion_sort, rand_arrays, num_averages)
        sorted_array_test_times_merge = self.sort_run(s.merge_sort, rand_arrays, num_averages)
        sorted_array_test_times_quick = self.sort_run(s.quick_sort, rand_arrays, num_averages)
        sorted_array_test_times_quick_hybrid = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages)

        sort_times_df = pd.DataFrame()
        #sort_times_df['bubble'] = sorted_array_test_times_bubble
        #sort_times_df['insert'] = sorted_array_test_times_insert
        sort_times_df['merge'] = sorted_array_test_times_merge
        sort_times_df['quick'] = sorted_array_test_times_quick
        sort_times_df['quick-insert'] = sorted_array_test_times_quick_hybrid
        sort_times_df['array_sizes'] = array_sizes

        return sort_times_df

    def plot_sort_comparisons(self, sort_times_df):
        #plt.plot(sort_times_df['array_sizes'], sort_times_df['bubble'], label='bubble', color='red')
        #plt.plot(sort_times_df['array_sizes'], sort_times_df['insert'], label='insert', color='purple')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['merge'], label='merge', color='steelblue')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['quick'], label='quick', color='orange')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['quick-insert'], label='quick + insert', color='green')
        plt.legend()
        plt.ylabel('Milliseconds')
        plt.xlabel('Array Size')
        plt.title('Sorting Times')
        plt.show()

    def run_sort_comparison(self, base_size, loop_size, num_averages):
        df = self.get_sort_comparisons_times(base_size, loop_size, num_averages)
        self.plot_sort_comparisons(df)

    def get_quick_sort_comparisons_times(self, base_size, loop_size, num_averages):
        
        rand_arrays, array_sizes = self.make_random_arrays(base_size, loop_size)
        
        sorted_array_test_times_quick_sort = self.sort_run(s.quick_sort, rand_arrays, num_averages)
        sorted_array_test_times_quick_hybrid_5 = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages,5)
        sorted_array_test_times_quick_hybrid_10 = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages,10)
        sorted_array_test_times_quick_hybrid_20 = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages,20)
        sorted_array_test_times_quick_hybrid_50 = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages,50)
        sorted_array_test_times_quick_hybrid_100 = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages,100)
        sorted_array_test_times_quick_hybrid_200 = self.sort_run(s.hybrid_quick_sort, rand_arrays, num_averages,200)

        sort_times_df = pd.DataFrame()
        sort_times_df['quick-sort'] = sorted_array_test_times_quick_sort
        sort_times_df['quick-insert-5'] = sorted_array_test_times_quick_hybrid_5
        sort_times_df['quick-insert-10'] = sorted_array_test_times_quick_hybrid_10
        sort_times_df['quick-insert-20'] = sorted_array_test_times_quick_hybrid_20
        sort_times_df['quick-insert-50'] = sorted_array_test_times_quick_hybrid_50
        sort_times_df['quick-insert-100'] = sorted_array_test_times_quick_hybrid_100
        sort_times_df['quick-insert-200'] = sorted_array_test_times_quick_hybrid_200
        sort_times_df['array_sizes'] = array_sizes

        return sort_times_df

    def run_quick_sort_comparison(self, base_size, loop_size, num_averages):
        df = self.get_quick_sort_comparisons_times(base_size, loop_size, num_averages)

        plt.plot(df['array_sizes'], df['quick-sort'], label='quick sort', color='brown')
        plt.plot(df['array_sizes'], df['quick-insert-5'], label='part_5', color='black')
        plt.plot(df['array_sizes'], df['quick-insert-10'], label='part_10', color='orange')
        plt.plot(df['array_sizes'], df['quick-insert-20'], label='part_20', color='green')
        plt.plot(df['array_sizes'], df['quick-insert-50'], label='part_50', color='blue')
        plt.plot(df['array_sizes'], df['quick-insert-100'], label='part_100', color='red')
        plt.plot(df['array_sizes'], df['quick-insert-200'], label='part_200', color='pink')
        plt.legend()
        plt.ylabel('Milliseconds')
        plt.xlabel('Array Size')
        plt.title('Sorting Times')
        plt.show()

print("Sort Comparisons")
s = Sorter()
#s.run_sort_comparison(1000, 5, 5)
s.run_quick_sort_comparison(5000, 5, 5)








exit(0)


