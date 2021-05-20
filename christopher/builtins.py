# Open file in read Mode 

# file_path = r"C:\Users\Don Uchris Family\Documents\data_python\4B3b-Assignments-Project\christopher\FILE\Kpk.txt"
# file = open(file_path, "r")
# print(file)
# print(file.read())

# file.close()

# # Open file in Write Mode

# file2 = open(file_path, "w")

# file2.write("hello i am a boy")
# file2.write("and i am 10yrs old")
# file2.write("and i leave in the west")
# file2.write("where do you leave?")

# file2.close()

# file3 = open(file_path, "a")

# file3.write("I want to do some thing awesome")

# file3.close()

classwrok = r"C:\Users\Don Uchris Family\Documents\data_python\4B3b-Assignments-Project\christopher\classwork.txt"

# file = open(classwrok, "a")

# x = int(input("please enter x > "))
# y = int(input("please enter y > "))

# product = x * y 
# print(f'{x} * {y} = {product}')


# name = input("Please enter a Name: ")
# reversed_name = list(reversed(name))
# # print(reversed_name)
# joined = "".join(reversed_name)
# print(f' {name} | {joined}', file=file)

# Assignment 
file_path = r"C:\Users\Don Uchris Family\Documents\data_python\4B3b-Assignments-Project\christopher\classwork.csv"
file = open(file_path, "a")

Name = input("Please enter Name : ")
date_of_birth = input("Please enter Date of Birth : ")
split_name = Name.split()
surname = split_name[1]
split_date = date_of_birth.split("-")
year_of_birth = split_date[0]
Age = 2021 - int(year_of_birth)
print(f'{surname} | {len(surname)} | {Age}', file=file)