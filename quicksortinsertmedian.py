

class QuickSortInsertionMedian:
    # Function to perform the insertion sort
    def hybrid_insertion_sort(self, arr, low, n):
        for i in range(low + 1, n + 1):
            val = arr[i]
            j = i
            while j>low and arr[j-1]>val:
                arr[j]= arr[j-1]
                j-= 1
            arr[j]= val

    # The following two functions are used
    # to perform quicksort hybrid on the array.

    # Partition function for quicksort
    def hybrid_partition(self, arr, low, high):

        median = int( (high-1-low) / 2)
        median = median + low
        if (arr[median]-arr[high-1])*(arr[low]-arr[median]) >= 0:
            arr[high-1], arr[median] = arr[median], arr[high-1]
        elif (arr[low]-arr[high-1]) * (arr[median]-arr[low]) >=0:
            arr[high-1], arr[low] = arr[low], arr[high-1]

        pivot = arr[high]
        i = j = low
        for i in range(low, high):
            if arr[i]<pivot:
                arr[i], arr[j]= arr[j], arr[i]
                j+= 1
        arr[j], arr[high]= arr[high], arr[j]
        return j

    # Hybrid function -> Quick + Insertion sort
    def hybrid_quick_sort_in_place(self, arr, low, high, partition_len):
        while low<high:

            # If the size of the array is less
            # than threshold apply insertion sort
            # and stop recursion
            if high-low + 1< partition_len:
                self.hybrid_insertion_sort(arr, low, high)
                break

            else:
                pivot = self.hybrid_partition(arr, low, high)

                # Optimised quicksort which works on
                # the smaller arrays first

                # If the left side of the pivot
                # is less than right, sort left part
                # and move to the right part of the array
                if pivot-low<high-pivot:
                    self.hybrid_quick_sort_in_place(arr, low, pivot-1, partition_len)
                    low = pivot + 1
                else:
                    # If the right side of pivot is less
                    # than left, sort right side and
                    # move to the left side
                    self.hybrid_quick_sort_in_place(arr, pivot + 1, high, partition_len)
                    high = pivot-1

    def sort(self, array, odata=10):
        n = len(array)
        self.hybrid_quick_sort_in_place(array, 0, n-1, odata)
        return array

