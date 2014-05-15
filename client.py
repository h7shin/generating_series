""" The client module allows
customization to the generating series
computation"""

# optional import
from subset import get_set_of_subsets

# weight function
def weight (lst):
    #return sum(lst)
    return len(lst)

# get number of map nodes to use for
# computation (the more the faster until
# some limit)

def get_num_map_nodes(size_param):

    """ comment if else block for testing 
    The number of map nodes are chosen based
    on the test results
    """

    # Increase mamp nodes according to
    # the value n
    n = size_param
    if n >= 17:
        return 120
    elif n >= 16:
        return 80
    elif n >= 15:
        return 40    
    elif n >= 13:
        return 20    
    elif n >= 11:
        return 10    
    else:
        return 1

# return a value that will substitute
# for variable x in the series
def x():
    return 1

# generate set of subsets (as lists)
# from {1...n}
def create_list(n):
    lst = list(range(1,n+1))
    return get_set_of_subsets (lst, [])    