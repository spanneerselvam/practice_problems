"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
l = [1, 2, 3, 4, 5]
k = 2
def rotate_list(l, k):
    new_list = []
    length = len(l)
    for i in range(0, length):
        new_index = (i+k) % length
        new_list.insert(new_index, l[i])

    return new_list

print(rotate_list(l, k))
