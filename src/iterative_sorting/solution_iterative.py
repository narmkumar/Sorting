# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    # (n-1 because after the sort, the one remaining will be the largest)
    for i in range(0, len(arr) - 1):
        print(arr)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Make a flag to show if swaps have occured
    swaps_occured = True
    # Run until you get through a loop without any swaps
    while swaps_occured:
        swaps_occured = False
        # For each element in the array...
        for i in range(len(arr) - 1):
            print(arr)
            # Check it's neighbor to the right...
            if arr[i] > arr[i+1]:
                # If neighbor is smaller, swap and make Flag true
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occured = True

import time
import random

l1 = list(range(1000))
random.shuffle(l1)
l2 = list(range(2000))
random.shuffle(l2)
l3 = list(range(3000))
random.shuffle(l3)
l4 = list(range(4000))
random.shuffle(l4)
l5 = list(range(5000))
random.shuffle(l5)
l6 = list(range(6000))
random.shuffle(l6)
l7 = list(range(7000))
random.shuffle(l7)
l8 = list(range(8000))
random.shuffle(l8)
l9 = list(range(9000))
random.shuffle(l9)
l10 = list(range(10000))
random.shuffle(l10)

shuffled_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]


results = []
for shuffled_list in shuffled_lists:
    l_copy = shuffled_list.copy()
    start_time = time.time()
    bubble_sort(l_copy)
    end_time = time.time()
    print(f"runtime: {end_time - start_time}")
    results.append(end_time - start_time)

for result in results:
    print(result)

def shuff(n=10):
    arr = list(range(n))
    random.shuffle(arr)
    return arr