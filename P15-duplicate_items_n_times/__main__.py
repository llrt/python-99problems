"""
P15 (**) Duplicate the elements of a list a given number of times.
Example:

scala> duplicateN(3, List('a, 'b, 'c, 'c, 'd))
res0: List[Symbol] = List('a, 'a, 'a, 'b, 'b, 'b, 'c, 'c, 'c, 'c, 'c, 'c, 'd, 'd, 'd)
""" 


def duplicate_n(n, l):
    new_list = []

    for elem in l: # for each element,
                        # add 2 copies of this element to the final list 
        new_list.extend( 
          ([elem]*n) # 2 copies of each element
        )

    return new_list


in_list = ['a', 'b', 'c', 'c', 'd']
print('Input: {}'.format(in_list))

out = duplicate_n(3, in_list)
print('Output: {}'.format(out))
