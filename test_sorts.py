from unittest import TestCase

import random

from bubble import BubbleSort
from insertion import InsertionSort
from merge import MergeSort
from quicksort import QuickSort
from quicksortinsert import QuickSortInsertion
from quicksortinsertmedian import QuickSortInsertionMedian
from quicksortmedian import QuickSortMedian

class TestQuickSortInsertion ( TestCase ) :
    def test_quicksort(self) :
        s = QuickSort ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

    def test_quicksort_insertion(self) :
        s = QuickSortInsertion ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array, 10 )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

    def test_quicksort_median(self) :
        s = QuickSortMedian ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

    def test_quicksort_insertion_median(self) :
        s = QuickSortInsertionMedian ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array, 10 )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

    def test_merge(self) :
        s = MergeSort ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

    def test_insertion(self) :
        s = InsertionSort ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

    def test_bubble(self) :
        s = BubbleSort ()
        rand_array = [random.randint ( 0, 250 ) for i in range ( 250 )]
        r = s.sort ( rand_array )
        pre = r[0]
        b = True
        for i in range ( len ( r ) ) :
            b = (pre <= r[i]) & b
            pre = r[i]
        assert b

