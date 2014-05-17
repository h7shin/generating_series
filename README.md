generating_series
=================

Evaluating generating series with large input data using Map-Reduce pattern

##### Generating Series

Generating Series is defined by the generating function P(S,x)

![Equation](https://raw.githubusercontent.com/hyunwookshin/generating_series/master/equation/equation.png)

##### Support

  Python 3

##### Two Algorithms

The optimization is implemented in five steps:

Optimizations
* Step 1. Map Reduce Pattern
* Step 2. Local Combiner as opposed to Global Combiner
* Step 3. Adjustment in number of map nodes
* Step 4. Quick way to determine maximum and minimum key values
* Step 5. Multiple Reduce Nodes for Same Key


1. Up to Step 4 (compute_local_optimized_step_4.py):  Follows Map-Reduce Pattern
![Diagram](https://github.com/hyunwookshin/generating_series/blob/master/diagrams/optimized_step_4.png?raw=true)
2. Up to Step 5 (compute_local.py): Splits Reduce Nodes further to increase number of parallel reduce processes
![Diagram](https://github.com/hyunwookshin/generating_series/blob/master/diagrams/optimized_step_5.png?raw=true)

Comparison of Algorithms
![Diagram](https://github.com/hyunwookshin/generating_series/blob/master/diagrams/time.bmp?raw=true)
#####  How to run

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

   If unsure, it is recommended to set size_param = len(<input list>).
   
   It is also recommended to set option to not_fixed to minimize running time
   while 'fixed' option is recommended for testing purposes

5. General Implementation

   Map function generates the powers of x in the series, reduce function collects the like terms,
   and combiner returns the sum of the terms by susbstituting for x.

   Split Input:   Split list into sublists by the number of map nodes. The last list may be shorter
                  than all others.
                
   Map:           Input:   index of the sublist and its corresponding sublist contents <br>
                  Returns: key = weight(element of the sublist), value = "max and min"**
                
                  ** "max and min" means the largest and smallest key values emitted by
                  other map nodes. This is to keep track of upper and lower bound of the key range
                  
  Local Combine:  Aggregates all key value pairs with same keys into a list
  
  Reduce:         Input:  Counts number of key value pairs (one particular key for reduce) <br>
                  Returns:Value of ax^k where a is the coefficient (= count), x is obtained
                  from x() from client.py, and k is optained from weight function w() from client.py)
                  
  Combine:        Evaluates sum of all terms from reduce nodes
  
   

  
  
  
