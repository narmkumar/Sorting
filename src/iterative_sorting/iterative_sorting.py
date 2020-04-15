# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for iX in range(cur_index + 1, len(arr)):
            if arr[iX] < arr[smallest_index]:
                smallest_index = iX

        # TO-DO: swap
        # tempItem = arr[cur_index]
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # arr[smallest_index] = tempItem

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    repeatBubble = True
    while repeatBubble:
        repeatBubble = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                repeatBubble = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
