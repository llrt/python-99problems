"""
P09 (**) Pack consecutive duplicates of list elements into sublists.
If a list contains repeated elements they should be placed in separate sublists.

Example:

scala> pack(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
res0: List[List[Symbol]] = List(List('a, 'a, 'a, 'a), List('b), List('c, 'c), List('a, 'a), List('d), List('e, 'e, 'e, 'e))
""" 


def pack(l): # from scratch
    new_list = []
    last = None
    
    consecutive_list = None

    for elem in l:
        if elem == last:
            consecutive_list.append(elem)
        else:
            if consecutive_list is not None: # except for the initial empty list
                new_list.append(consecutive_list)  

            last = elem
            consecutive_list = [elem]

    if consecutive_list is not None: # as we add only when elem changes, the last sequence was not written; fix it
        new_list.append(consecutive_list)  


    return new_list


in_list = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
print('Input: {}'.format(in_list))

out = pack(in_list) # solution 1: without std lib
print('Output: {}'.format(out))