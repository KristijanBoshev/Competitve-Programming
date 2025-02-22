def bubble_sort(lst):
    n = len(lst) - 1
    
    for i in range(n):
            for j in range(n-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    

    return lst


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1