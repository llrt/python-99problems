"""
P03 (*) Find the Kth element of a list.
By convention, the first element in the list is element 0.

Example:
scala> nth(2, List(1, 1, 2, 3, 5, 8))
res0: Int = 2
""" 

def kth_element(k, l):
    return l[k-1] # in python, indexes start at 0



in_list = [1, 1, 2, 3, 5, 8]
print('Input: {}'.format(in_list))

out = kth_element(3, in_list) # 3rd element
print('Output: {}'.format(out))
    