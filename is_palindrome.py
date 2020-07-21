
def is_palindrome(s):
    '''Returns boolean for whether a string is a palidrome or not.
    
    Numbers are part of the palindrome while punctuation is not.
    
    Arguments:
        s (str): string to be assessed
    Returns:
        (bool): True if string is a palindrome
    '''
    
    used = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
    for letter in s.lower():
        if letter not in used:
            s = s.replace(letter, '')
    print(s)
    
    lst = list(s.lower())
    reverse = lst[::-1]
    
    if lst == reverse:
        return True
    else:
        return False
