from client import x

""" Reduce evaluates the value of the term 
x to the power of key taking (key,
list of pairs) as input"""

def reduce (key, lst_of_pairs, result_lst):
    count = len(lst_of_pairs)
    print (str(count)+"x^"+str(key)+" + ")
    result_lst.append(count*(x()**key))