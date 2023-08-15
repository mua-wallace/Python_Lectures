#print("Hello world");

x = "Hello Python";
#print(x);  

y = 42;
#print(y)

# true or false like this is not valid in python rather we use True or False

# Tuple in python
dog = ('cedrick', 45, False,)

# print(dog[0])

# dog[2] = "new item"








# List in python

empty_list = []

students = ['nanje', 'charles', 'brandaline', 'anderson', 'martin', 'cedrick', 'arlette', 'peace']

students[3] = "wallace"
students.append('njifand')

# print(students)
students.pop(6)
# print(students)


# dictionaries in python

empty_dict = {}
student_dict = {
    "name" : "wallace", 
    "dob": "19th Oct 1994",
    "occupation": "developer",
    "hobbies": ['eating', 'listening to music' ],
    "isMarried": False
}

student_dict['name'] = 'Brendaline'
student_dict['best_friend'] = "peace"

empty_dict['first_dict'] = student_dict
# print(empty_dict)
# print(student_dict)
# print(type(students))
# print(type(student_dict))
# print(type(x))
# print(type(y))
# print(type(students))


# Number type
int_to_float = float(35)
float_to_int = int(44.7)
int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))


# String type

# tring concatenation

# name = "Arltte"

sub_total1 = 35

sub_total2 = "56"

# print(sub_total1 + int(sub_total2))  #

# print("My name is "+ name)
# print('Hello ' + str(42))

# string interpolation

first_name = "brandaline"

last_name = "Monkam"

age = 23

# My name is brandaline Monkam and I am 45 years old

#  F-Sting (Literal string Interpolation)

# print(f"My name is {first_name} {last_name} and I am {age} years old")

# using .format() method

# print("My name is {} {} and I am {} years old".format(first_name, last_name, age))
# print("My name is {} {} and I am {} years old".format( age, last_name, first_name ))

#  %-formating

name = "Kalu Peace"

agepeace = 25

# print("I am called %s and I am %d days old" % (name.upper(), agepeace*365))
#  I am called Kalu Peace and I am  -----days old


# list in python

fruits = ["banana", "apple", "pineapple","pear", "strawberry", "oranges", "guava"]

fruits.append("peace")

sub_list = ["mango", "paw-paw"]

list_of_fruits = fruits + sub_list

# print(list_of_fruits)

# print(fruits[:5])

print(fruits.index('strawberry'))

# print(len(list_of_fruits))


#  tuple definition

tuple_of_numbers = (1, 2, 3, 4, 5)

tuple_of_number1 = 1, 2, 3, 4, 5

# tuple_of_numbers = tuple_of_numbers + int(67),

# print(tuple_of_numbers)

# dog = ("Canis Familiaris", "dog", "carnivore", 12)


#  tuples as return vallues

def calc_sum_and_diff(a, b):
    sum =a + b
    diff = a - b
    result = (sum, diff)
    return result

print(calc_sum_and_diff(34, 23))














