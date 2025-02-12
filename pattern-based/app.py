def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    
    Input: 3
    Output: ['***', '***', '***']
    """

    lst=[]
    s=''
    
    for _ in range(n):
       s = s + '*'
       
    for _ in range(n):
        lst.append(s)
        
    return lst

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    
    Input: 5
    Output: ['*****', '*   *', '*   *', '*   *', '*****']

    """
  
    lst=[]
    
    if n==1:
        lst.append('*')
        return lst
        
        
    ## First row    
    lst.append('*' * n)
      
    for _ in range(n-2):
        lst.append('*' + ' ' * (n-2) + '*')
        

def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    
    Input: n = 4, m = 5
    Output: ['*****', '*****', '*****', '*****']    
    """
    
    lst=[]
    s=''
    
    ## Define the string(columns)
    for _ in range(m):
        s = s + '*'
        
    ## Append the list(rows)
    for _ in range(n):
        lst.append(s)
        
    return lst            

def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    
    Input: 3
    Output: ['*', '**', '***']  
    """
       
    if n==1:
        return ['*']
    else:
        return generate_triangle(n - 1) + ['*' * n]        
    

def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    Input: 3
    Output: ['***', '**', '*']
    """
    
    if n==1:
        return ['*']
        
    else:
        return ['*' * n] + generate_inverted_triangle(n-1)    
    

def generate_pyramid(n, total=None):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    
    Input: 5
    Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
    """
    
    if total==None:
        total = n
    
    if n==1:
        return [' ' * (total - n) + '*' + ' ' * (total-n)]
        
    else:
        return generate_pyramid(n-1, total) + [' ' * (total-n) + '*' * (2*n-1) + ' ' * (total-n)]    
    
    
def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    
    Input: 5
    Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
    """
    lst = []
    
    for i in range(n, 0, -1):
        whitespace = ' ' * (n-i)
        asterix = '*' * (2*i-1)
        s = whitespace + asterix + whitespace
        lst.append(s)
        
    return lst    


def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    
    Input: 5
    Output: ['1', '22', '333', '4444', '55555']
    """
    
    lst=[]
    
    for i in range(1,n+1):
        lst.append(str(i) * i)
        
    return lst    


def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    
    Input: 5
    Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
    """
    
    lst = []
    counter = 1
    
    for i in range(1, n+1):
        temporary_numbers=[]
        for j in range (i):
            temporary_numbers.append(str(counter))
            counter = counter + 1
        row = " ".join(temporary_numbers)
        lst.append(row)
        
    return lst


def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    
    Input: 3
    Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
    """
    lst=[]
    
    for i in range(1, n*2):
        whitespace = ' ' * abs(n-i)
        asterix = '*' * (2 * (n - abs(n - i)) - 1)
        lst.append(whitespace + asterix + whitespace)
        
    return lst    


def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    
    Input: 4
    Output: ['   *', '  **', ' ***', '****']
    """
    
    lst=[]
    
    for i in range(1, n+1):
        whitespace = ' ' * (n-i)
        asterix = '*' * (n - (n-i))
        word = whitespace + asterix
        lst.append(word)
        
    return lst    


def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    
    Input: 4
    Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
    """
    
    lst = []

    for i in range(n):
        whitespace = ' ' * i
        asterix = '*' * (2 * (n-i) - 1)
             
        lst.append(whitespace + asterix + whitespace)
        
    return lst + lst[-2::-1]          


def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    
    Input: 5
    Output: ['*', '**', '* *', '*  *', '*****']
    """
    
    lst=[]

    for i in range(1, n+1):
        asterix = '*' * i
        lst.append(asterix)
        
    
    for index, _ in enumerate(lst):
        if not index in [0,1,n-1]:
            lst[index] = '*' + ' ' * (index-1) + '*'
            
    return lst    

        
def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    
    Input: 4
    Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']

    """
    
    lst=[]
    
    for i in range(1, n+1):
        whitespace = " " *  (n - i)
        tmp = []
        for j in range(1, i+1):
            numbers = str(j)
            tmp.append(numbers)
        
        s = whitespace + " ".join(tmp) + whitespace    
        lst.append(s)
        
    return lst    
            
    
    
