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
from quicksortmedian import QuickSortMedian
from quicksortinsertmedian import QuickSortInsertionMedian

NANO_TO_MS = 1000000

class Sorter:

    def __init__(self):
        pass

    def make_random_arrays(self, BASE_SIZE, LOOP_SIZE):
        array_sizes = []
        rand_arrays = []
        for i in range(1,1+LOOP_SIZE):
            test_size = BASE_SIZE * (i)
            array_sizes.append(test_size)
            rand_array = [random.randint(0,test_size) for i in range(test_size)]
            rand_arrays.append(rand_array)
        return rand_arrays, array_sizes 

    def sort_run(self, fn, rand_arrays, runs, odata=None):
        sorted_array_test_times = []
        for rand_array in rand_arrays:
            run_list = []
            print ( "\tArray Size: {0}".format ( len(rand_array) ) )
            for j in range(runs):
                rand_array_copy = rand_array.copy()
                start_time = time.perf_counter_ns()
                if odata != None:
                    sorted_rand_array = fn.sort(rand_array_copy, odata)
                else:
                    sorted_rand_array = fn.sort( rand_array_copy )
                stop_time = time.perf_counter_ns()
                test_time = (stop_time - start_time) / NANO_TO_MS
                print ( "\t\tTime Trial: {0} : {1} ms ".format (j+1, test_time ) )
                run_list.append(test_time)
            test_time = statistics.mean(run_list)
            print ( "\tAverage Time: {0}".format ( test_time ) )
            sorted_array_test_times.append(test_time)
        return sorted_array_test_times

    def get_sort_comparisons_times(self, base_size, loop_size, num_averages):
        print("Generating random arrays...")
        rand_arrays, array_sizes = self.make_random_arrays(base_size, loop_size)
        print ("Bubble Sorting...")
        sorted_array_test_times_bubble = self.sort_run(BubbleSort(), rand_arrays, num_averages)
        print ( "Insertion Sorting..." )
        sorted_array_test_times_insert = self.sort_run(InsertionSort(), rand_arrays, num_averages)
        print ( "Merge Sorting..." )
        sorted_array_test_times_merge = self.sort_run(MergeSort(), rand_arrays, num_averages)
        print ( "Quick Sorting..." )
        sorted_array_test_times_quick = self.sort_run(QuickSort(), rand_arrays, num_averages)
        print ( "Hybrid Quick+Insertion Sorting..." )
        sorted_array_test_times_quick_hybrid = self.sort_run(QuickSortInsertion(), rand_arrays, num_averages, 10)
        print ( "Quick Median Sorting..." )
        sorted_array_test_times_quick_median = self.sort_run(QuickSortMedian(), rand_arrays, num_averages)
        print ( "Quick Insert Median Sorting..." )
        sorted_array_test_times_quick_insert_median = self.sort_run(QuickSortInsertionMedian(), rand_arrays, num_averages, 10)

        sort_times_df = pd.DataFrame()
        sort_times_df['bubble'] = sorted_array_test_times_bubble
        sort_times_df['insert'] = sorted_array_test_times_insert
        sort_times_df['merge'] = sorted_array_test_times_merge
        sort_times_df['quick'] = sorted_array_test_times_quick
        sort_times_df['Q+I'] = sorted_array_test_times_quick_hybrid
        sort_times_df['Q+M'] = sorted_array_test_times_quick_median
        sort_times_df['Q+I+M'] = sorted_array_test_times_quick_insert_median
        sort_times_df['array_sizes'] = array_sizes

        return sort_times_df

    def plot_sort_comparisons(self, sort_times_df):
        plt.plot(sort_times_df['array_sizes'], sort_times_df['bubble'], label='bubble', color='red')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['insert'], label='insert', color='purple')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['merge'], label='merge', color='steelblue')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['quick'], label='quick', color='orange')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['quick-insert'], label='quick + insert', color='green')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['quick-median'], label='quick + median', color='magenta')
        plt.plot(sort_times_df['array_sizes'], sort_times_df['quick-insert-median'], label='quick + insert + median', color='black')
        plt.legend()
        plt.ylabel('Milliseconds')
        plt.xlabel('Array Size')
        plt.title('Sorting Times')
        plt.show()

    def plot_sort_comparisons_bg(self, sort_times_df):
        for c in sort_times_df.columns:
            if c != 'array_sizes':
                plt.bar(c, sort_times_df[c], label=c)
        plt.xticks ( rotation=45 )
        plt.legend()
        plt.ylabel('Milliseconds')
        plt.title('Sorting Times')
        plt.show()

    def run_sort_comparison(self, base_size, loop_size, num_averages):
        df = self.get_sort_comparisons_times(base_size, loop_size, num_averages)
        self.plot_sort_comparisons_bg(df)

s = Sorter()
s.run_sort_comparison(500, 1, 100)



