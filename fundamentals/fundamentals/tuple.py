tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)

# print(dog[2])
"X"
#TypeError: 'tuple' object does not support item assignment

#result is: carnivore


# dog[0] = "X"
# #TypeError: 'tuple' object does not support item assignment

# dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")



# dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment


# dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")


x = (1,5,6,9,2)
# print(len(x))
# output:
# 5

# def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    # c = 2 * math.pi * r
    # a = math.pi * r * r
    # return (c, a)


# import language
# print(language.translate(dog))
# output would look something like: ("dog", "chien", "perro")



# Conditionals in Python

x =5

fruits = ['mango', 'apple', 'pear', 'banana']

# if x > 50: 
#     print("Value is bigger than 50")
# elif x == 50:
#     print("Value is exactly 50")
# else:
#     print("value is less than 50")


# for i in range(4):
#     print(i)

# for i in range(3, 5):
#     print(i)



# 3, 5, 7, 9, 11,13,15

# for i in range(3,16, 2):
#     print(i)


# 0 mango
# 1 apple
# 2 pear
# 3 banana

fruits = ['mango', 'apple', 'pear', 'banana']

# for i in range(len(fruits)):
#     print(i, fruits[i])

# Mango is  stored at index 0 in the fruits list
# Apple is  stored at index 1 in the fruits list
# Pear is  stored at index 2 in the fruits list
# Banana is  stored at index 3 in the fruits list


for character in "string":
    if character == "i":
        continue
    print(character)





