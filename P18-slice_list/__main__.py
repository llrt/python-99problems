"""
P18 (**) Extract a slice from a list.
Given two indices, I and K, the slice is the list containing the elements from and including the Ith element up to but not including the Kth element of the original list. Start counting the elements with 0.
Example:

scala> slice(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
res0: List[Symbol] = List('d, 'e, 'f, 'g)
""" 


def slice(i, j, l):
    new_list = []
    
    new_list.extend(l[(i-1):j]) # from i-th to j-th element 
    
    return new_list


def slice2(i, j, l):
    import builtins
    return l[builtins.slice(i-1, j)] # to make sure we are using std lib's slice, use builtins package


in_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print('Input: {}'.format(in_list))

out = slice(3, 7, in_list) # solution 1: without std lib
print('Output (from scratch): {}'.format(out))

out = slice2(3, 7, in_list) # solution 2: with std lib
print('Output (with std lib): {}'.format(out))
