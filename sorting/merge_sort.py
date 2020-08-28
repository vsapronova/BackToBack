


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)



def merge(list1, list2):
    new_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1

        else:
            new_list.append(list2[j])
            j += 1

    if i >= len(list1) and j < len(list2):
        new_list.append(list2[j])
        j += 1
    if i < len(list1) and j >= len(list2):
        new_list.append(list1[i])
        i += 1

    return new_list



print(merge_sort([5, 30, 6, 55, 4]))