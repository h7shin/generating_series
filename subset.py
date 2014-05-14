
"""get_set_of_subsets returns the extended set of the current_set
so that every subset of set lst is a set in the extended set."""

def get_set_of_subsets (lst, current_set):
    if len(lst) == 0:
        return [current_set]
    else:
        last = lst.pop()        # get the last element of the lst   
        new_set = []
        new_set = get_set_of_subsets(lst, current_set)  # recursive call
        for i in range(len(new_set)):
            tmp_lst = new_set[i]
            tmp_lst = tmp_lst + [last]                       # generate new subset
            new_set.append(tmp_lst)
        #print(new_set)
        return new_set
    