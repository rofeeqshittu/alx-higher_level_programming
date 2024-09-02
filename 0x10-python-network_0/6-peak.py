#!/usr/bin/python3
""" Contains find_peak fxn """

def find_peak(list_of_integers):
    """ find_peak fxn """

    def peak_helper(low, high):
        """ peak_helper """
        if low == high:
            return list_of_integers[low]
        
        mid = (low + high) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        
        # If the left neighbor is greater, search in the left half
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return peak_helper(low, mid - 1)
        
        # Otherwise, search in the right half
        return peak_helper(mid + 1, high)
    
    if not list_of_integers:
        return None
    
    return peak_helper(0, len(list_of_integers) - 1)

