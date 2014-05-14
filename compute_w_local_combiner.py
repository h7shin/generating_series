from multiprocessing import Process, Manager
from subset import get_set_of_subsets
import time
from map import map_
from reduce import reduce
from client import get_num_map_nodes

""" Compute(lst) computes the sum of the generating series
for set, lst = [1,...,n] (n >= 1), with respect
to weight function w (in client.py)"""

def compute(lst):
    
    
    # number of map nodes num_map_nodes
    num_map_nodes = get_num_map_nodes()
    
    # Manager to keep track of all map results
    list_of_emissions = []
    
    # Job is a list of processes
    jobs = []
        
    # Process number
    num_p = 0    
    
    manager = Manager()
    
    start_time = time.time()    
    
    set_of_subsets = get_set_of_subsets (lst, [])
       
    print ("Up to Permutation:", str(time.time() - start_time ) + " seconds"  )
    
    len_set_of_subsets = len(set_of_subsets)
    
    print ("Size of S: ", len_set_of_subsets)
    len_sublist = max(1,int(len_set_of_subsets/float(num_map_nodes)))
    
    i=0
    
    while i < len_set_of_subsets:
        list_of_emissions.append(manager.list())
        if (len_set_of_subsets - i <= len_sublist):
            # last step
            sliced_list = set_of_subsets[i:]
        else:
            sliced_list = set_of_subsets[i:i + len_sublist]
        print(len(sliced_list))
        p = Process(target=map_, args=(num_p, sliced_list, list_of_emissions[-1]))
        i += len_sublist
        jobs.append(p)
        p.start()
        num_p += 1  
        
    
    
    print ("Wait for Catch Up\n")
    for p in jobs:
        p.join() 
    #print(len(emissions))
    print ("Up to Mapping Stage:", str(time.time() - start_time ) + " seconds"  )

    #---------------------------------------------------
    # Shuffle/Reduce
    
    jobs = []   
    manager_2 = Manager()    
    result_lst = manager_2.list()    

    for emissions in list_of_emissions:
        for key in range(emissions[-1][1],emissions[-1][2]+5):
            key_list = [1 for x in emissions if x[0] == key]
            q = Process(target=reduce, args=(key,key_list,result_lst))
            jobs.append(q)
            q.start()

    print ("Wait for Catch Up\n")
    for q in jobs:
        q.join()     
        
    print ("Up to Reducing Stage:", str(time.time() - start_time ) + " seconds"  )
    print("Input Size: ", len_set_of_subsets )
    return sum(result_lst)

# list_generator returns a list [1...n]

def list_generator (n):
    return list(range(1,n+1))

if __name__ == "__main__":
    print(compute(list_generator(13)))