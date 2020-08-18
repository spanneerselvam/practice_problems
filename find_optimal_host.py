"""
Given a list of dictionary items, find the most optimal host with the least distance.
"""
import math

friends = [{"name": 'Bob', 'location': (5,2,10)}, {"name": 'Radha', 'location': (2,3,5)}, 
    {"name": 'Mary', 'location': (19,3,4)}, {"name": 'Skyler', 'location': (1,5,3)}]
    
def find_host(friends):
    initial_value = friends[0]['location']
    distances = []
    d = {}
    for i in range(0, len(friends)):
        for j in range(0, len(friends)):
            if i != j:
                x1 = friends[i]['location'][0]
                y1 = friends[i]['location'][1]
                z1 = friends[i]['location'][2]
                x2 = friends[j]['location'][0]
                y2 = friends[j]['location'][1]
                z2 = friends[j]['location'][2]
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 +(z2-z1)**2) 
                d[friends[i]['name']] = dist
    
    initial_value = list(d.values())[0]

    for key, value in d.items():
        initial_value = min(value, initial_value)
        min_item = initial_value
    for key, value in d.items():
        if value == min_item:
            return key

print(find_host(friends))

