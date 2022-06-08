"""
P11 (*) Modified run-length encoding.
Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as (N, E) terms.
Example:

scala> encodeModified(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
res0: List[Any] = List((4,'a), 'b, (2,'c), (2,'a), 'd, (4,'e))
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

def encode1(l):
    new_list = []

    for sub_list in pack(l):
        n = len(sub_list)
        elem = sub_list[0]
        if n==1:
            new_list.append(elem)
        else:
            new_list.append((n, elem))

    return new_list

def encode2(l):
    from itertools import groupby

    new_list = []

    for (k, g) in groupby(l):
        n = len(list(g))
        if n==1:
            new_list.append(k)
        else:
            new_list.append((n, k))

    return new_list

in_list = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
print('Input: {}'.format(in_list))

out1 = encode1(in_list) # solution 1: without std lib
print('Output (solution 1 - from scratch): {}'.format(out1))

out2 = encode2(in_list) # solution 2: with std lib
print('Output (solution 2 - with std lib): {}'.format(out2))