import random
import time
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd 
import scipy.stats as stats

class Sorter:

    def __init__(self, plot_sort = False):  
        self.PLOT_SORT = plot_sort


    def bubble_sort(self, array) :

        if self.PLOT_SORT: 
            y = [str ( i ) for i in range ( len ( array ) )]      
            plt.ion()

        
        n = len ( array )
        for i in range ( n ) :
            already_sorted = True

            for j in range ( n - i - 1 ) :
                if array[j] > array[j + 1] :
                    array[j], array[j + 1] = array[j + 1], array[j]

                    if self.PLOT_SORT:
                        self.update_plot(plt, array, y)
                
                    already_sorted = False
            if already_sorted :
                break
        plt.close()
        return array

    def merge(self, left, right) :
        if len ( left ) == 0 :
            return right
        if len ( right ) == 0 :
            return left
        result = []
        index_left = index_right = 0
        while len ( result ) < len ( left ) + len ( right ) :
            if left[index_left] <= right[index_right] :
                result.append ( left[index_left] )
                index_left += 1
            else :
                result.append ( right[index_right] )
                index_right += 1
            if index_right == len ( right ) :
                result += left[index_left :]
                break
            if index_left == len ( left ) :
                result += right[index_right :]
                break
        return result

    def merge_sort(self, array) :
        if len ( array ) < 2 :
            return array
        midpoint = len ( array ) // 2
        return self.merge (
            left=  self.merge_sort ( array[:midpoint] ),
            right= self.merge_sort ( array[midpoint :] ) )

    def insertion_sort(self, array):
            
        if self.PLOT_SORT:
            y = [str ( i ) for i in range ( len ( array ) )]
            plt.ion()
        
        for i in range(1, len(array)):
            key_item = array[i]
            j = i - 1
            while j >= 0 and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
                if self.PLOT_SORT:
                    self.update_plot(plt, array, y)

            array[j + 1] = key_item
        return array


    def partition(self, arr, low, high):
        i = (low-1)		 # index of smaller element
        pivot = arr[high]	 # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:

                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)

    def quick_sort(self, array):
        n = len(array)
        self.quickSort(array, 0, n-1)

    def update_plot(self, plt, array, y):
        plt.clf()
        plt.bar ( y, array )
        plt.draw()
        plt.pause(0.00001)
    


print("Sort Comparisons")
s = Sorter()

BASE_SIZE = 100
LOOP_SIZE = 10

NANO_TO_MS = 1000000

def remove_outliers_z_score(data, z_score):
    #find absolute value of z-score for each observation
    z = np.abs(stats.zscore(data))
    #only keep rows in dataframe with all z-scores less than absolute value of 3 
    clean_data = []
    for i in range( len(z) ):
        if z[i] >= z_score:
            data.pop(i)
    return data

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
            start_time = time.perf_counter_ns()
            sorted_rand_array = fn(rand_array)
            stop_time = time.perf_counter_ns()
            test_time = (stop_time - start_time) / NANO_TO_MS
            run_list.append(test_time)
        run_list_clean = remove_outliers_z_score(run_list, 3)
        test_time = statistics.mean(run_list_clean)
        sorted_array_test_times.append(test_time)
    return sorted_array_test_times

rand_arrays, array_sizes = make_random_arrays(BASE_SIZE, LOOP_SIZE)
sorted_array_test_times = sort_run(s.insertion_sort, rand_arrays, 50)
    
plot_test_times(sorted_array_test_times, array_sizes )
exit(0)


rand_array = [random.randint(0,100) for i in range(BASE_SIZE)]
start_time_bs = time.perf_counter()
sorted_rand_array_bs = s.bubble_sort(rand_array)
stop_time_bs = time.perf_counter()
    
rand_array = [random.randint(0,100) for i in range(BASE_SIZE)]
start_time_qs = time.perf_counter()
sorted_rand_array_qs = s.quick_sort(rand_array)
stop_time_qs = time.perf_counter()

rand_array = [random.randint(0,100) for i in range(BASE_SIZE)]
start_time_is = time.perf_counter()
sorted_rand_array_is = s.insertion_sort(rand_array)
stop_time_is = time.perf_counter()

print(f"Bubble Sort: {stop_time_bs - start_time_bs:0.4f} seconds")
print(f"Merge Sort: {stop_time_ms - start_time_ms:0.4f} seconds")
print(f"Insertion Sort: {stop_time_is - start_time_is:0.4f} seconds")
print(f"Quick Sort: {stop_time_qs - start_time_qs:0.4f} seconds")