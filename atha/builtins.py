# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\assignments\FILES\kpk.txt"
# # file = open(file_path, "r") # OPEN FILE IN READ MODE
# # # print(file)
# # print(file.read())

# # file.close()

# # file2 = open(file_path, "w") # OPEN FILE IN WRITE MODE

# # file2.write("hello i am a boy\n")
# # file2.write("and i am 10years old\n")
# # file2.write("and i leave i the west\n")
# # file2.write("Where do you leave\n")

# # file2.close()


# # file.close()

# # file2 = open(file_path, "a") # OPEN FILE IN WRITE MODE

# # file2.write("This is an update\n")

# # file2.close()

# # PRINT

# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\assignments\FILES\kpk.txt"

# file2 = open(file_path, "a") # OPEN FILE IN WRITE MODE


# # print(1991, 2, 3)
# # print(1991, 2, 3)
# # print(1991, 2, 3)
# # print(1991, 2, 3)

# # print(1991, 2, 3, sep = "->")
# print(1991, 2, 3, sep = "->", end = " | ")
# print(1991, 2, 3, sep = "->", end = " | ")
# # print(1991, 2, 3, sep = "->", end = " | ")
# print(1991, 2, 3, sep = "->", end = " | ", file= file2)


# 

# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\assignments\FILES\kpk.txt"

# file = open(file_path, "a") # OPEN FILE IN WRITE MODE

# x = int(input("Please enter x > "))
# y = int(input("Please enter y > "))

# product = x * y
# print(f"{x} x {y} = {product}")

# reversed

# x = "Ade is my name"

# reversed_x = list(reversed(x))
# print(reversed_x)
# joined = "".join(reversed_x)
# print(joined)

# RANGE BUILTIN FUNCTION

# numbers = range(10)
# print(numbers) # returns a GENERATOR OBJECT
# list_numbers = list(numbers) # CONVERT GENERATOR OBJECT INTO LIST IN ORDER TO SEE THE VALUES OF OUR RANGE
# print(list_numbers)

# even_numbers = range(2, 20, 2) # numbers from 2- 20 taking steps of 2
# print(even_numbers)
# print(list(even_numbers)) # convert to list in order to see values generated.

# # the range function is mostly used in for loops as shown below.
# prefered_number = 20
# for value in range(2, 6, 1):
#     print(prefered_number)

# Map

# map allows running a function on an iterable's members

# names = ["ali", "john", "jonah"]
# list_of_name_lens = map(len, names)
# print(list_of_name_lens) # returns a generator object
# print(list(list_of_name_lens))

# func = lambda value: f"{value}-> {len(value)}"

# list_of_name_lens = map(func, names)

# print(list(list_of_name_lens))

# numbers = range(1,8)

# func = lambda number: number * number

# # print(func(12))

# squared_numbers = map(func, numbers)

# print(list(squared_numbers))

# FILTER 

numbers = [90, 80, 20, 95, 55, 48, 23, 74]
# func = lambda score: score < 60
# filtered_list = filter(func, numbers)

# print(list(filtered_list))

# enumerate
# print(list(enumerate(numbers)))

for value in enumerate(numbers):
    print(value)