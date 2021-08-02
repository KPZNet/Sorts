import random

class Sorter:

    def merge(self, left, right) :
        # If the first array is empty, then nothing needs
        # to be merged, and you can return the second array as the result
        if len ( left ) == 0 :
            return right
        # If the second array is empty, then nothing needs
        # to be merged, and you can return the first array as the result
        if len ( right ) == 0 :
            return left
        result = []
        index_left = index_right = 0
        # Now go through both arrays until all the elements
        # make it into the resultant array
        while len ( result ) < len ( left ) + len ( right ) :
            # The elements need to be sorted to add them to the
            # resultant array, so you need to decide whether to get
            # the next element from the first or the second array
            if left[index_left] <= right[index_right] :
                result.append ( left[index_left] )
                index_left += 1
            else :
                result.append ( right[index_right] )
                index_right += 1
            # If you reach the end of either array, then you can
            # add the remaining elements from the other array to
            # the result and break the loop
            if index_right == len ( right ) :
                result += left[index_left :]
                break
            if index_left == len ( left ) :
                result += right[index_right :]
                break
        return result

    def merge_sort(self, array) :
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len ( array ) < 2 :
            return array
        midpoint = len ( array ) // 2
        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result
        return self.merge (
            left=  self.merge_sort ( array[:midpoint] ),
            right= self.merge_sort ( array[midpoint :] ) )

    def insertion_sort(self, array):
        # Loop from the second element of the array until
        # the last element
        for i in range(1, len(array)):
            # This is the element we want to position in its
            # correct place
            key_item = array[i]
            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1
            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if `key_item` is smaller than its adjacent values.
            while j >= 0 and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1
            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            array[j + 1] = key_item
        return array

print("Sort Comparisons")
s = Sorter()
rand_array = [random.randint(0,1000) for i in range(20)]
sorted_rand_array_is = s.insertion_sort(rand_array)
sorted_rand_array_ms = s.merge_sort(rand_array)

print(sorted_rand_array_ms)

print(sorted_rand_array_is)