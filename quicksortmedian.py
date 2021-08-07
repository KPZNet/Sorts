

class QuickSortMedian:

    def swap(self, array,a,b):
        array[a],array[b] = array[b],array[a]

    def quick_sort_partition(self, arr, low, high):
        i = (low-1)		 # index of smaller element

        median = int( (high-1-low) / 2)
        median = median + low
        if (arr[median]-arr[high-1])*(arr[low]-arr[median]) >= 0:
            arr[high-1], arr[median] = arr[median], arr[high-1]
        elif (arr[low]-arr[high-1]) * (arr[median]-arr[low]) >=0:
            arr[high-1], arr[low] = arr[low], arr[high-1]

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