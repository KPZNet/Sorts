from quicksort import QuickSort


def test_sort():
    s = QuickSort()
    arr = [7, 4, 5, 6, 1, 3, 4, 5, 7, 8]
    arr = s.sort(arr)

    b = arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6] <= arr[7] <= arr[8] <= arr[9]

    assert b
