# n = int(input("Enter any number:  "))

# for i in range(n):
#     for j in range(1, n-i + 1):
#         # print(j, end=' ')
#         pass
#     print('')


# Sets in python

# set1 = {1, 2, 3, 4, 5}
# set1.add(7 )

# print(set1)

ls = [1, 3 , 5, 7]



ls[0], ls[1]  = ls[1], ls[3]

# [3, 7, 5, 7]

# print(ls)

# Ternary operator in python
# <result_if_true> if condition else <result_if_false>

stacks = 1
# traditional
if stacks >= 3:
    # print('Coding Dojo')
    pass
else:
    # print('You are not Coding Dojo!')
    pass


# ternary
# print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')



def squre(num):
    x = num**2
    return x

print(squre(add(0)))


# anonymous lambda 

lambda num: num**2






