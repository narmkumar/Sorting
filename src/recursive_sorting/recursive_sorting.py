# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for x in range(0, len(merged_arr)):
        if arrA == []:
            merged_arr[x] = arrB.pop(0)
        elif arrB == []:
            merged_arr[x] = arrA.pop(0)
        else:
            merged_arr[x] = arrA.pop(0) if arrA[0] <= arrB[0] else arrB.pop(0)
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Confirm list w/ data
    if not arr:
        return []

    # Base case
    if len(arr) == 1:
        if type(arr[0]) is int:
            return arr
        else:
            return arr[0]

    new_arr = arr

    # Creating list of lists
    if type(arr[0]) is int:
        new_arr = []
        for i in range(0, len(arr)):
            new_arr.append([arr[i]])

    # Make list if odd, an even value
    if len(new_arr) % 2 != 0:
        temp = merge(new_arr[-2], new_arr[-1])
        new_arr.pop(-2)
        new_arr.pop(-1)
        new_arr.append(temp)

    # Merge each pair of lists
    array = []
    for i in range(0, len(new_arr), 2):
        temp = merge(new_arr[i], new_arr[i + 1])
        array.append(temp)
    return merge_sort(array)


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr
#
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr
#
#
# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):
#
#     return arr
