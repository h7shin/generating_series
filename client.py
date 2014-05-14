""" The client module allows
customization to the generating series
computation"""

# weight function

def weight (lst):
    #return sum(lst)
    return len(lst)

# get number of map nodes to use for
# computation (the more the faster until
# some limit)

def get_num_map_nodes():
    return 40

# return a value that will substitute
# for variable x in the series
def x():
    return 1



