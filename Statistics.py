%matplotlib inline
import matplotlib.pyplot as plt
from collections import Counter

def median(values):
    """Return the median value from a sequence of values
    
    >>> median([1, 3, 5])          # odd number of values
    3
    
    >>> median([1, 3, 5, 7])       # even number of values
    4.0
    """
    
    sorted_values = sorted(values)
    num = len(values)
    centerpoint = num // 2         # find the index for the midpoint, truncating
                                   #     any floats...
    
    if num % 2 == 1: 
        # return the center value 
        #     if n is ODD
        return sorted_values[centerpoint]
    
    else:
        # return the average of the two center-most values
        #     if num is EVEN
        c1 = centerpoint - 1
        c2 = centerpoint
        return (sorted_values[c1] + sorted_values[c2]) / 2
    
median([1,3,5])