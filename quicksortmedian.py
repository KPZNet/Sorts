
class QuickSortMedian:
    def swap(self, array,a,b):
        array[a],array[b] = array[b],array[a]

    def partition(self, array,start,end):
        median = int( (end-1-start) / 2)
        median = median + start
        left = start + 1
        if (array[median]-array[end-1])*(array[start]-array[median]) >= 0:
            self.swap(array,start,median)
        elif (array[end-1]-array[median]) * (array[start]-array[end-1]) >=0:
             self.swap(array,start,end-1)
        pivot = array[start]
        for right in range(start,end):
            if pivot > array[right]:
                self.swap(array,left,right)
                left = left + 1
        self.swap(array,start,left-1)
        return left-1

    def quickSortHelper(self, array,start,end):
        if start < end:
            splitPoint = self.partition(array,start,end)
            self.quickSortHelper(array,start,splitPoint)
            self.quickSortHelper(array,splitPoint+1,end)
    def sort(self, array):
        self.quickSortHelper(array,0,len(array))


-----


class QuickSort:
    def quick_sort_partition(self, arr, low, high):
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

    def quick_sort_in_place(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.quick_sort_partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quick_sort_in_place(arr, low, pi-1)
            self.quick_sort_in_place(arr, pi+1, high)

    def sort(self, array):
        n = len(array)
        self.quick_sort_in_place(array, 0, n-1)
        return array