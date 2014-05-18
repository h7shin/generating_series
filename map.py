from client import weight

""" map function takes (slice_number, sublist_of_element, emissions)
as inputs and appends (weight(element), min, max) (weight(element) is the key)
to emissions, where min, max are the lowest and highest weight(element) keys
in emissions
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
