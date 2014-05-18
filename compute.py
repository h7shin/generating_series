from multiprocessing import Process, Manager
import time
from map import map
from reduce import reduce
from client import get_num_map_nodes, create_list

""" Compute(lst) computes the sum of the generating series
for set, lst = [1,...,n] (n >= 1), with respect
to weight function w (in client.py)"""

def compute(lst):
    
    # number of map nodes num_map_nodes
    num_map_nodes = get_num_map_nodes()
    
    # Manager to keep track of all map results
    manager = Manager()

    # Map processes emit key-value pairs to emissions
    emissions = manager.list()    

    
    # Job is a list of processes
    jobs = []
        
    # Process number
    num_p = 0    
    
    
    
    start_time = time.time()    
    
    list_of_list = lst
       
    print ("Up to Permutation:", str(time.time() - start_time ) + " seconds"  )
    
    len_list_of_list = len(list_of_list)
    
    print ("Size of S: ", len_list_of_list)
    len_sublist = max(1,int(len_list_of_list/float(num_map_nodes)))
    
    i=0
    
    while i < len_list_of_list:
        
        if (len_list_of_list - i <= len_sublist):
            # last step
            sliced_list = list_of_list[i:]
        else:
            sliced_list = list_of_list[i:i + len_sublist]
        print(len(sliced_list))
        p = Process(target=map, args=(num_p, sliced_list, emissions))
        i += len_sublist
        jobs.append(p)
        p.start()
        num_p += 1  
        
    
    
    print ("Wait for Catch Up\n")
    for p in jobs:
        p.join() 
    print(len(emissions))
    print ("Up to Mapping Stage:", str(time.time() - start_time ) + " seconds"  )

    #---------------------------------------------------
    # Shuffle/Reduce
    
    jobs = []   
    manager_2 = Manager()    
    result_lst = manager_2.list()    


    for key in range(emissions[-1][1],emissions[-1][2]+5):
        key_list = [1 for x in emissions if x[0] == key]
        q = Process(target=reduce, args=(key,key_list,result_lst))
        jobs.append(q)
        q.start()

    print ("Wait for Catch Up\n")
    for q in jobs:
        q.join()     
        
    print ("Up to Reducing Stage:", str(time.time() - start_time ) + " seconds"  )
    print("Input Size: ", len_list_of_list )
    return sum(result_lst)

# list_generator returns a list [1...n]

def list_generator (n):
    return list(range(1,n+1))

if __name__ == "__main__":
    print(compute(create_list()))