import random
import time
import matplotlib.pyplot as plt

class Sorter:

    def plot_bar_graph(self, x):
        sx = len ( x )
        y =  [str(i) for i in range(sx)]
        sy = len(y)
        plt.bar (x,y)
        plt.title ( 'Sort' )
        plt.xlabel ( 'X' )
        plt.ylabel ( 'Y' )
        plt.show ()


    def bubble_sort(self, array) :
        n = len ( array )
        for i in range ( n ) :
            already_sorted = True
            self.plot_bar_graph(array)
            for j in range ( n - i - 1 ) :
                if array[j] > array[j + 1] :
                    array[j], array[j + 1] = array[j + 1], array[j]
                    already_sorted = False
            if already_sorted :
                break
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
        for i in range(1, len(array)):
            key_item = array[i]
            j = i - 1
            while j >= 0 and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key_item
        return array

print("Sort Comparisons")
s = Sorter()
rand_array = [random.randint(0,100) for i in range(100)]


start_time_bs = time.perf_counter()
sorted_rand_array_bs = s.bubble_sort(rand_array)
stop_time_bs = time.perf_counter()

start_time_ms = time.perf_counter()
sorted_rand_array_ms = s.merge_sort(rand_array)
stop_time_ms = time.perf_counter()

start_time_is = time.perf_counter()
sorted_rand_array_is = s.insertion_sort(rand_array)
stop_time_is = time.perf_counter()

#print(f"Bubble Sort: {stop_time_bs - start_time_bs:0.4f} seconds")
print(f"Merge Sort: {stop_time_ms - start_time_ms:0.4f} seconds")
print(f"Insertion Sort: {stop_time_is - start_time_is:0.4f} seconds")