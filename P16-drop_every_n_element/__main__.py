"""
P16 (**) Drop every Nth element from a list.
Example:

scala> drop(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
res0: List[Symbol] = List('a, 'b, 'd, 'e, 'g, 'h, 'j, 'k)
""" 


def drop(n, l):
    new_list = []

    for (i, elem) in enumerate(l): 
       
        if (i+1)%n==0:
          continue
        else:
          new_list.append(elem) 

    return new_list


in_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print('Input: {}'.format(in_list))

out = drop(3, in_list)
print('Output: {}'.format(out))
