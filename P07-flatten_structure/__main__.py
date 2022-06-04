"""
P07 (**) Flatten a nested list structure.

Example:
scala> flatten(List(List(1, 1), 2, List(3, List(5, 8))))
res0: List[Any] = List(1, 1, 2, 3, 5, 8)
""" 

from collections.abc import Iterable

def flatten(struct): # from scratch
    def _flat(st):
        l = []

        for e in st:
            if isinstance(e, Iterable): #if is iterable
                l.extend(_flat(e)) 
            else:
                l.append(e)

        return l

    new_list = _flat(struct)

    return new_list

in_struct = [[1, [1]], 2, [3, [5, 8]]]
print('Input: {}'.format(in_struct))

out = flatten(in_struct) 
print('Output: {}'.format(out))