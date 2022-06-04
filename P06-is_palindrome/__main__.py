"""
P06 (*) Find out whether a list is a palindrome.
Example:

scala> isPalindrome(List(1, 2, 3, 2, 1))
res0: Boolean = true
""" 

def is_palindrome1(l): # from scratch
    n = len(l)
    new_list = []
    for i in range(n-1, -1, -1): # iterates from indexes n-1 (included) to -1 (excluded), 
                                 # i.e. n-1, n-2, n-3, ..., 2, 1, 0
        new_list.append(l[i])

    return l == new_list

def is_palindrome2(l): # using std lib
    return l == list(reversed(l))



in_list = [1, 2, 3, 2, 1]
print('Input: {}'.format(in_list))

out1 = is_palindrome1(in_list) # solution 1: without std lib
print('Output (solution 1 - from scratch): {}'.format(out1))
    
out2 = is_palindrome2(in_list) # solution 2: with std lib
print('Output (solution 2 - with std lib): {}'.format(out2))


print('....')

in_list = [0, 2, 3, 2, 1]
print('Input: {}'.format(in_list))

out1 = is_palindrome1(in_list) # solution 1: without std lib
print('Output (solution 1 - from scratch): {}'.format(out1))
    
out2 = is_palindrome2(in_list) # solution 2: with std lib
print('Output (solution 2 - with std lib): {}'.format(out2))
