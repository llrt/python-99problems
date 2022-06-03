"""
P02 (*) Find the last but one element of a list.

Example:
scala> penultimate(List(1, 1, 2, 3, 5, 8))
res0: Int = 5
""" 

def penultimate_element(l):
    return l[-2] # in python, special index "-2" denotes the second element starting at the last of a list



in_list = [1, 1, 2, 3, 5, 8]
print('Input: {}'.format(in_list))

out = penultimate_element(in_list)
print('Output: {}'.format(out))
    