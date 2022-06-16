"""
P12 (**) Decode a run-length encoded list.
Given a run-length code list generated as specified in problem P10, construct its uncompressed version.
Example:

scala> decode(List((4, 'a), (1, 'b), (2, 'c), (2, 'a), (1, 'd), (4, 'e)))
res0: List[Symbol] = List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)
""" 


def decode(l):
    new_list = []

    for (n, elem) in l: # for each pair of n times and respective element,
                        # add computed elements to the final list 
        new_list.extend( 
          # the elements itself are arrays of elements repeated n times
          ([elem]*n)
        )

    return new_list


in_list = [(4, 'a'), (1, 'b'), (2, 'c'), (2, 'a'), (1, 'd'), (4, 'e')]
print('Input: {}'.format(in_list))

out = decode(in_list)
print('Output: {}'.format(out))
