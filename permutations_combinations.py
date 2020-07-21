from math import factorial

def ncr_npr(n, r, ordered = 'c'):
    '''Calculates the number of possible combinations or permutations.

    For more effecient / diverse tools see itertools library,
    this is just a coding exercise.

    Arguments:
        n (int): population, entire set from which to draw from
        r (int): how many will be chosen
        type (str): 'c' for combinations (non-ordered)
                    or 'p' for permutations (ordered)
    Returns:
        (int): number of possible combinations or permutations
        (None): in the event of an error
    '''

    # Conditions that don't need an equation
    try:
        int(n)
        int(r)
    except:
        return None

    if n <= 0 or r <= 0 or r > n:
        return None
    elif n == r and ordered == 'p':
        return factorial(n)
    elif n == r and ordered == 'c':
        return 1

    # Permutation and combination equations
    if ordered == 'p':
        return int(factorial(n) / factorial(n-r))
    elif ordered == 'c':
        return int(factorial(n) / (factorial(n-r) * factorial(r)))
    else:
        return None
