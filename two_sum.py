def twoSum(nums, target):
    '''Returns two indices of the two numbers in a list that add up to a target.
    
    Arguments:
        nums (list): list of numbers at least 2 elements long
        target (int, float): number which is the sum of some two elements of nums
    
    Returns:
        (list): a list of two indices
    ''''

    i = 0
    i2 = 1
    winner = 0
    
    while i < len(nums):
        target2 = target - nums[i]
        
        while i2 < len(nums):
            if nums[i2] == target2:
                winner = 1
                break
            else:
                i2 += 1
        
        if winner == 1:
            break
        
        i += 1
        i2 = i + 1
        
    return [i, i2]
