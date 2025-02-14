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
