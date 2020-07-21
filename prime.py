def primes_below(target):
    '''Returns all prime numbers leading up to and including a given integer.
    
    Arguments:
        target (int): the target integer (limited to 10,000)
    
    Returns:
        (list): all primes leading up to the target
    '''

    try:
        int(target)
    except:
        print('Please use an integer above 1')
        return None

    if target > 10000:
        print('Slow down, this is a simple function!')
        return None
    
    # Makes a list of all integers from 2 to the target
    plist = list(range(2, target + 1))

    index = 0

    # Finds multiples of each item in the list and
    # knocks those multiples out of the prime list
    while True:
        
        multilist = list()
        m = plist[index] * 2
        
        while m < target + 1:
            multilist.append(m)
            m += plist[index]
        
        plist = [y for y in plist if y not in multilist]
        index += 1

        if index >= len(plist):
            break
    
    return plist
