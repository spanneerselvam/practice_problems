"""
Given a list of dictionary items, find the most optimal host with the least distance.
"""
friends = [{"name": 'Bob', 'location': (5,2,10)}, {"name": 'David', 'location': (2,3,5)}, 
    {"name": 'Mary', 'location': (19,3,4)}, {"name": 'Skyler', 'location': (3,5,1)}]
    
def find_host(friends):
    initial_value = friends[0]['location']
    for friend in friends:
        initial_value = min(friend['location'], initial_value)
        min_item = initial_value
    
    for i in range(0, len(friends)):
        if friends[i]['location'] == min_item:
            name = friends[i]['name']
    return name, min_item
print(find_host(friends))

