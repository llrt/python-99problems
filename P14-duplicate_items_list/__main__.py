"""
P14 (*) Duplicate the elements of a list.
Example:

scala> duplicate(List('a, 'b, 'c, 'c, 'd))
res0: List[Symbol] = List('a, 'a, 'b, 'b, 'c, 'c, 'c, 'c, 'd, 'd)""" 


def duplicate(l):
    new_list = []

    for elem in l: # for each element,
                        # add 2 copies of this element to the final list 
        new_list.extend( 
          ([elem]*2) # 2 copies of each element
        )

    return new_list


in_list = ['a', 'b', 'c', 'c', 'd']
print('Input: {}'.format(in_list))

out = duplicate(in_list)
print('Output: {}'.format(out))
