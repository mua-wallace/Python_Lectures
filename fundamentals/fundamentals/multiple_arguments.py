
def addTwoNumbers(x,y):
    return x +y

# print(addTwoNumbers(4, -7))


# splat operator in python *
# spread operator in JS ...

def addManyNumbers(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(addManyNumbers(2,4, 5))
print(addManyNumbers(2,456,2, 45, 45,231))
print(addManyNumbers(2,4, 34,235))


