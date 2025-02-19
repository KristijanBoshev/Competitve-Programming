def check_unique(lst):
    """Chck if all elements in the list are unique

    Args:
        lst (List):

    Returns:
        bool: True/False
    """    
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True

from collections import Counter


def count_even_odd(lst):
    """Count the occurrences of even and odd numbers in the list

    Args:
        lst (List): List of integers

    Returns:
        Tuple: int, int
    """    
    
    odd = []
    even = []
    
    d = Counter(lst)
    for key, value in d.items():
        if key % 2 == 1:
            odd.append(value)
        else:
            even.append(value)
    
    ans = (sum(even), sum(odd))    
    
    return ans


def max_consecutive_difference(lst):
    """Calculate the maximum difference between consecutive elements in the list

    Args:
        lst (List): List of integers

    Returns:
        int: maximum difference between consecutive elements
    """    
    maxx:int = 0
    curr: int = 0
    
    for i in range(len(lst) - 1):
        if not lst[i] == len(lst) - 1:
            curr = abs(lst[i] - lst[i+1])
        
        if curr > maxx:
            maxx = curr
             
                 
    return maxx      

def rotate_list(lst, k):
    """Rotate the list to the right by k steps

    Args:
        lst (List): List of integers
        k (int): int

    Returns:
        List[int]: 
    """    
    for _ in range(k):
        if lst:
            item = lst.pop()
            lst.insert(0, item)
        
    return lst    


def merge_lists_to_dictionary(keys, values):
    """Merge two lists into a dictionary where keys are from the first list and values are from the second list

    Args:
        keys (List): List of keys
        values (List): List of values

    Returns:
        Dict:
    """    
    d = {}
    
    if not len(keys) == len(values):
        return False
    
    for i,j in zip(keys,values):
        d[i] = j
        
    return d    


from collections import Counter

def count_word_frequency(sentence):
    """Count the frequency of each word in a given sentence

    Args:
        sentence str: A sentence containing words

    Returns:
         Dict[str, int]
    """    
    
    words = sentence.split()
    
    d = Counter(words)
    
    return d


def is_palindromic_tuple(tup):
    """Check if the given tuple is the same when reversed

    Args:
        tuple: tuple of elements

    Returns:
        bool: True if the tuple is palindromic, False otherwise
    """    
    if len(tup) == 1:
        return True
        
    return tup[::-1] == tup    


def merge_dicts_with_overlapping_keys(dicts):
    """Merge multiple dictionaries, summing values for overlapping keys

    Args:
        List[Dict]: List of dictionaries to merge

    Returns:
         Dict[str, int]
    """    
    d = {}
    
    for dictt in dicts:
        for key,value in dictt.items():
            d[key] = d.get(key, 0) + value
            
    return d


def is_subset(lst1, lst2):
    """Check if lst1 is a subset of lst2

    Args:
        lst1 : list of elements to check
        lst2: list of elements to check against

    Returns:
        bool: True if lst1 is a subset of lst2, False otherwise
    """    
    if not lst1:  # Empty lst1 is always a subset
        return True
    
    n, m = len(lst1), len(lst2)
    
    for i in range(m - n + 1):  # Iterate over all possible start positions in lst2
        if lst2[i:i + n] == lst1:
            return True
    
    return False       
            


def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    
    if n == 1:
        return False
        
    for i in range(2, n):
        if n % i == 0:
            return False
        
    if n % 1 == 0 and n % n == 0:
        return True


import math

def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    
    if num < 0:
        return False  
    
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num 



def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    minn = min(n,m)
    for i in range(minn, 1, -1):
        if n % i == 0 and m % i == 0:
            return i
            
    return 1                    
    
        
