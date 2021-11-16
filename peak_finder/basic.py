#
# The first version of our function!
# Write doc strings 
#
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities or tuples
    Intensities are defined as local maxima if the
    intensities of the elements in the list before and after
    are smaller than the peak we want to determine.

    For example given a list:
        1 5 [6] 4 1 2 [3] 2

    We expect 6 and 3 to be returned. [6, 3]
    

    Args:
        list_of_intensities (list of floats, ints or tuple of ints): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)

    """
    maxima_list = []
    tuple_check = all([isinstance(element, tuple) for element in list_of_intensities])
    int_check = all([isinstance(element, int) for element in list_of_intensities])

    if int_check:
        for step in range(len(list_of_intensities)):
            if step == 0:
                if list_of_intensities[step] > list_of_intensities[step+1]:
                    maxima_list.append(list_of_intensities[step])
            if step == (len(list_of_intensities)-1):
                if list_of_intensities[step] > list_of_intensities[step-1]:
                    maxima_list.append(list_of_intensities[step])
            if (step != 0) and (step != (len(list_of_intensities)-1)):
                if list_of_intensities[step-1] < list_of_intensities[step] > list_of_intensities[step+1]:
                    maxima_list.append(list_of_intensities[step])

    def tuple_sum (element):
        sum = 0
        for pos in range(len(element)):
            sum += element[pos]
        return sum

    if tuple_check:
        for step in range(len(list_of_intensities)):
            tuple_sum(list_of_intensities[step])
        
            if step == 0:
                if tuple_sum(list_of_intensities[step]) > tuple_sum(list_of_intensities[step+1]):
                    maxima_list.append(list_of_intensities[step])
            if step == (len(list_of_intensities)-1):
                if tuple_sum(list_of_intensities[step]) > tuple_sum(list_of_intensities[step-1]):
                    maxima_list.append(list_of_intensities[step])
            if (step != 0) and (step != (len(list_of_intensities)-1)):
                if tuple_sum(list_of_intensities[step-1]) < tuple_sum(list_of_intensities[step]) > tuple_sum(list_of_intensities[step+1]):
                    maxima_list.append(list_of_intensities[step])

    return maxima_list
