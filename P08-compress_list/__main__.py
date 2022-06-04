"""
P08 (**) Eliminate consecutive duplicates of list elements.
If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.

Example:

scala> compress(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
res0: List[Symbol] = List('a, 'b, 'c, 'a, 'd, 'e)
""" 


def compress(l): # from scratch
    new_list = []
    last = None
    
    for elem in l:
        if elem == last:
            continue
        else:
            last = elem
            new_list.append(elem)
    
    return new_list


in_list = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
print('Input: {}'.format(in_list))

out = compress(in_list) # solution 1: without std lib
print('Output: {}'.format(out))