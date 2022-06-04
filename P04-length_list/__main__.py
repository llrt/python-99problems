"""
P04 (*) Find the number of elements of a list.

Example:
scala> length(List(1, 1, 2, 3, 5, 8))
res0: Int = 6
""" 

def length1(l): # from scratch
    n = 0
    for elem in l:
        n += 1
    
    return n

def length2(l): # using std lib
    return len(l)



in_list = [1, 1, 2, 3, 5, 8]
print('Input: {}'.format(in_list))

out1 = length1(in_list) # solution 1: without std lib
print('Output (solution 1 - from scratch): {}'.format(out1))
    
out2 = length1(in_list) # solution 2: with std lib
print('Output (solution 2 - with std lib): {}'.format(out2))
