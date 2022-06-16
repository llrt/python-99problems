"""
P17 (*) Split a list into two parts.
The length of the first part is given. Use a Tuple for your result.
Example:

scala> split(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
res0: (List[Symbol], List[Symbol]) = (List('a, 'b, 'c),List('d, 'e, 'f, 'g, 'h, 'i, 'j, 'k))""" 


def split(n, l):
    first_list = []
    second_list = []

    for (i, elem) in enumerate(l): 
        if i<n:
          first_list.append(elem)
        else:
          second_list.append(elem)

    return (first_list, second_list)


in_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print('Input: {}'.format(in_list))

out = split(3, in_list)
print('Output: {}'.format(out))
