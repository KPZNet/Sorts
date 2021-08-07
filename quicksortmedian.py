
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