from multiprocessing import Process, Manager
import time
from map import map
from reduce import reduce
from client import get_num_map_nodes, create_list

# HEROKU SUPPORT DISABLE BY COMMENTING OUT

from flask import Flask

app = Flask(__name__)
@app.route('/')
app.debug = True

def compute(lst, size_param = 0, option='not_fixed'):
    try:       
        # number of map nodes num_map_nodes
        if option=='not_fixed':
            num_map_nodes = get_num_map_nodes(size_param)
        elif option == 'fixed':
            num_map_nodes = 5
        else:
            raise NameError('second parameter [option] should be either `not_fixed` or `fixed` ... see documentation')
        
        # Manager to keep track of all map results
        list_of_emissions = []
        
        # Job is a list of processes
        jobs = []
            
        # Process number
        num_p = 0    
        
        manager = Manager()
        
        start_time = time.time() 
        
        print ("Up to Permutation:", str(time.time() - start_time ) + " seconds"  )
        
        len_lst = len(lst)
        
        print ("Size of S: ", len_lst)
        len_sublist = max(1,int(len_lst/float(num_map_nodes)))
        
        i=0
        
        #Split input into muliple sliced_list each sent to one map node
        
        while i < len_lst:
            list_of_emissions.append(manager.list())
            if (len_lst - i <= len_sublist):
                # last step
                sliced_list = lst[i:]
            else:
                sliced_list = lst[i:i + len_sublist]
            #print(len(sliced_list))
            p = Process(target=map, args=(num_p, sliced_list, list_of_emissions[-1]))
            i += len_sublist
            jobs.append(p)
            p.start()
            num_p += 1  
            
        
        print ("Wait for Catch Up\n")
        for p in jobs:
            p.join() 
        
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
        print("Length of List of List: ", len_lst )
        return sum(result_lst)
        
    except NameError as e:
        print('Usage Error:', e)
    return jsonify(result={"status": 200})
if __name__ == "__main__":
    #with open("output.txt", "a") as myfile:
        
    #   compute(create_list(n),,'fixed') # run test for fixed number of map nodes    
    
    #   for n in [4,11,12,13,14,15,16,17]: # run test for list of all subsets of {1...n}
    #       start_time = time.time()
    #       computed = str(compute(create_list(n), n))
    #       myfile.write(str(n) + " "+ computed + " "+ str(time.time() - start_time) +"\n")  
    #       myfile.flush()
    pass