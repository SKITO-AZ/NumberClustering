def cluster(data, num=1):
    
    if len(data) < num:
        return 0

    datastats = {}
    distribution_min = min(data)
    distribution_length = max(data) - min(data)
    if distribution_length == 0:
        return None
    for i in range(len(data)):
        datastats[i] = {'cnt' : 1, 'location' : (data[i] - distribution_min) / distribution_length, 'values' : [data[i]]}
    

    while len(datastats) != num:
        length = len(datastats)
        key = list(datastats.keys())
        distance = 1
        keyname = [None, None]
        for i in range(length):
            for j in range(i+1, length):
                if (datastats[key[i]]['location']-datastats[key[j]]['location']) ** 2 < distance:
                    distance = (datastats[key[i]]['location']-datastats[key[j]]['location']) ** 2
                    keyname = [key[i], key[j]]
        if keyname[0] == None:
            continue
        datastats[keyname[0]]['location'] = (datastats[keyname[0]]['location'] + datastats[keyname[1]]['location']) / 2
        datastats[keyname[0]]['values'] += datastats[keyname[1]]['values']
        datastats[keyname[0]]['cnt'] += datastats[keyname[1]]['cnt']
        del datastats[keyname[1]]
    
    return datastats
