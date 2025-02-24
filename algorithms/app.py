from typing import List


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
            

def selection_sort(lst):
    
    n = len(lst)
    
    for i in range(n-1):
        min_index = i
    
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                lst[j], lst[min_index] = lst[min_index], lst[j]
            
    return lst        


## Binary search approach
def countNegatives(grid: List[List[int]]) -> int:
    cnt = 0
    
    for row in grid:
        l,r = 0, len(row)-1
        
        while l <= r:
            mid = (l+r) // 2
            
            if row[mid] >= 0:
                l = mid + 1
            
            else:
                r = mid - 1
                
                
        cnt += len(row) - l
        
    return cnt


## Greedy approach
def countNegatives(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    r, c, cnt = m - 1, 0, 0
    while r >= 0 and c < n:
        if grid[r][c] < 0:
            cnt += n - c
            r -= 1
        else:
            c += 1
    return cnt
                            
                            
## Binary search approach
## In ascending list we ALWAYS have to find the first positive number
## In descending list we ALWAYS have to find the first negative number
## Only the if condition and cnt changes
def countNegativesAsc(grid: List[List[int]]) -> int:
    
    cnt = 0
    for row in grid:
        l,r = 0, len(row)-1
        while l<=r:
            mid = (l+r) // 2
            if row[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
                
        cnt += l 
                
    return cnt         


def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    
    
    l, r = 0, len(letters) - 1
    
    while l<=r:
        mid = (l+r) // 2
        
        if letters[mid] == target and mid != len(letters) - 1:
            return letters[mid+1]
        
        elif letters[mid] < target:
            l = mid + 1
            
        else:
            r = mid - 1
    # This avoids index out of range error when element is not found        
    if l == len(letters): 
        return letters[0]
    else:
        return letters[l]       
    
    

def searchRange(nums: List[int], target: int) -> List[int]:
        def check_side(is_left: bool) -> int:
            l, r = 0, len(nums) - 1
            bound = -1  # Default to -1 if target is not found
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    bound = mid  # Store potential boundary
                    if is_left:
                        r = mid - 1  # Search further left
                    else:
                        l = mid + 1   # Search further right
                elif nums[mid] < target:
                    l = mid + 1  # Move right
                else:
                    r = mid - 1  # Move left
            return bound

        left = check_side(True)  # Find leftmost index
        right = check_side(False)  # Find rightmost index
        return [left, right] if left != -1 else [-1, -1]      
   
                
                                          