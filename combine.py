def combine(key, emissions, combined_list):
    keylist = [1 for x in emissions if x[0] == key]
    combined_list.extend(keylist)