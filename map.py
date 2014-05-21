from client import weight

""" map function takes (slice_number, sublist_of_element, emissions)
as inputs and appends (weight(element), min, max) (weight(element) is the key)
to emissions"""


"""
min and max are minimum and maximum keys emitted from
completed map processes. This is to keep track of the upper and 
lower bound of key range, and avoid going through the
list again to determine the maximum and minimum key values.
"""

def map (slice_number, sublist_of_element, emissions):
    print("map:",slice_number)
    
    for element in sublist_of_element:
        w = weight(element)

        # mutate emissions (made slight changes
        # to the original Map Reduce Pattern to avoid 
        # going over the entire list again to find max and min
        
        # emit key value
        w = weight(element)
        if len(emissions) == 0:
            emit = [w, w, w]
        else:
            emit = [w,min(emissions[-1][1],w),max(emissions[-1][2],w)]
        emissions.append(emit)
