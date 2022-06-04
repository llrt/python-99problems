"""
P05 (*) Reverse a list.

Example:
scala> reverse(List(1, 1, 2, 3, 5, 8))
res0: List[Int] = List(8, 5, 3, 2, 1, 1)
""" 

def reverse1(l): # from scratch
    n = len(l)
    new_list = []
    for i in range(n-1, -1, -1): # iterates from indexes n-1 (included) to -1 (excluded), 
                                 # i.e. n-1, n-2, n-3, ..., 2, 1, 0
        new_list.append(l[i])

    return new_list

def reverse2(l): # using std lib
    return list(reversed(l))



in_list = [1, 1, 2, 3, 5, 8]
print('Input: {}'.format(in_list))

out1 = reverse1(in_list) # solution 1: without std lib
print('Output (solution 1 - from scratch): {}'.format(out1))
    
out2 = reverse2(in_list) # solution 2: with std lib
print('Output (solution 2 - with std lib): {}'.format(out2))
