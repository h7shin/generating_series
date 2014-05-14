from client import weight

""" map function takes (slice_number, sublist_of_subset)
as inputs and emits (weight(subset),min, max)
where min, max are the lowest and highest weight so far in 
previous emisions
"""

def map_ (slice_number, sublist_of_subset, emissions):
    print("map:",slice_number)
    
    for subset in sublist_of_subset:
        w = weight(subset)

        # mutate emissions dictionary (made slight changes
        # to the original MapReduce Pattern to avoid 
        # going over the entire list again to find max and min
        
        # emit key value
        w = weight(subset)
        if len(emissions) == 0:
            emit = [w, w, w]
        else:
            emit = [w,min(emissions[-1][1],w),max(emissions[-1][2],w)]
        emissions.append(emit)
