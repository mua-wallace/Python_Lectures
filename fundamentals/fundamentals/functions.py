# function declaration in python


def add(a, b):
    x = a + b
    return x

sum1  = add(4,6)
sum2  = add(1,4)

sum3 = add(sum1, sum2)


# print(sum1)
# print(sum2)
# print(sum3)


# def be_cheerful(name='', repeat= 2):
#     print(f"Good morning {name}" * repeat)
  

# be_cheerful()
    # Good morning wallace 
    # Good morning wallace 


"""
This is 
an example of 
a multi line comment
"""

# This is an example a a single line comment


# def say_Hi(name= '', repeat= 2):
#    return print(f"Good morning {name}\n"* repeat)


# say_Hi("Peace")

def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2, 4, 10, 16]
b = multiply(a, 5)
print(b)


# my_numbers=[2,4, 6, 8,10]

# for i in my_numbers:
#     print(i)