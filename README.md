generating_series
=================

Evaluating generating series with large input data using Map-Reduce pattern

Support

  Python 3
  
How to run

1. Customize client.py
  * implement your own weight function w() that returns a power in the series that will operate on each element of the set
  * optional: implement get_num_map_nodes(size_param) -> (returns number of map nodes) 
    where size_param is a variable you can use to categorize input by size
    the number of map nodes should be higher with the larger input size
  * optional: inplement x() -> (returns a number) to be used to substitute for variable x
  * optional: implement create_list() -> (returns a list) to be used as input
  
2. Run command [your_path_to]/Python34/python.exe compute_local.py
  * Call function compute(lst,size_param,option)
    where lst is a list of (list, integer, or float)
  * size_param is a variable that indicates the size of the input (you define it in anyway you like)
  * option is one of 'fixed' or 'not_fixed'
  * 'fixed'         : set number of map nodes to 15 (you can modify this in compute_local.py)
  * 'not_fixed'     : set number of map nodes to get_num_map_nodes(size_param) in client.py

3. You can also run different tests by uncommenting some of the codes in __name__ == __main__
   at the bottom of compute_local.py source code. See compute_local.py for details.

4. Recommendation

   If unsure, it is recommended to set size_param = len(<input list>)
   It is recommended to set option to not_fixed to minimize running time
   while 'fixed' option is recommended for testing purposes

5. General Implementation

   Split Input: Split list into sublist by number of map nodes. The last list may be shorter
                than all others.
   Map:           Input:   index of the sublist and its corresponding sublist contents
                  Returns: key = weight(element of the sublist), value = "max and min"**
                
                  ** "max and min" means the largest and smallest key values emitted by
                  other map nodes. This is to keep track of upper and lower bound of key range
                  
  Local Combine:  Aggregate all key value pairs from a single map node
  
  Reduce:         Counts number of key value pairs (one particular key for reduce)
                  and returns ax^k where a is the coefficient (= count), x is obtained
                  from x() from client.py, and k is optained from weight function w() from client.py)
                  
  Combine:        Evaluate sum of all terms from reduce nodes
  
   

  
  
  
