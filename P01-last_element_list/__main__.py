"""
P01 (*) Find the last element of a list.

Example:
scala> last(List(1, 1, 2, 3, 5, 8))
res0: Int = 8
""" 

def last_element(l):
    return l[-1] # in python, special index "-1" denotes last element of a list



in_list = [1, 1, 2, 3, 5, 8]
print('Input: {}'.format(in_list))

out = last_element(in_list)
print('Output: {}'.format(out))
    