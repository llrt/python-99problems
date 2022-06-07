"""
P10 (*) Run-length encoding of a list.
Use the result of problem P09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as tuples (N, E) where N is the number of duplicates of the element E.
Example:

scala> encode(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
res0: List[(Int, Symbol)] = List((4,'a), (1,'b), (2,'c), (2,'a), (1,'d), (4,'e))
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

def encode(l):
    new_list = []

    for sub_list in pack(l):
        n = len(sub_list)
        elem = sub_list[0]
        new_list.append((n, elem))

    return new_list

in_list = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
print('Input: {}'.format(in_list))

out = encode(in_list) # solution 1: without std lib
print('Output: {}'.format(out))