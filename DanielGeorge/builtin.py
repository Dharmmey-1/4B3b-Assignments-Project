# file_path = r"/home/dg/Documents/DataScience/Git/4B3b-Assignments-Project/DanielGeorge/FILES/kpk.txt"
# file = open(file_path, "r") #This is to open file in read mode
# print(file)
# print(file.read())

# file.close()


# file2 = open(file_path, "w") #Open file in write mode
# file2.write("Hello i am a boy")
# file2.write(" and i am 10 years old")
# file2.write(" and i leave in the west. ")
# file2.write("Where do you leave.\n")

# file2.close()

# file2 = open(file_path, "a") #Open file in write mode
# file2.write("This is an update\n")


# file2.close()



# file_path = r"/home/dg/Documents/DataScience/Git/4B3b-Assignments-Project/DanielGeorge/FILES/kpk.txt"
# file2 = open(file_path, "a") #Open file in write mode

# print(1991, 2, 3, sep = "->", end = " | ", file=file2)


# file_path = r"/home/dg/Documents/DataScience/Git/4B3b-Assignments-Project/DanielGeorge/FILES/classwork.txt"
# file3 = open(file_path, "a")

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# z = x * y
# print(f' {x} * {y} = {z}', file = file3)



# file_path = r"/home/dg/Documents/DataScience/Git/4B3b-Assignments-Project/DanielGeorge/FILES/classwork.txt"
# file3 = open(file_path, "a")

# name = (input("Enter any name:"))
# new_name = list(reversed(name))
# joined = "".join(new_name)
# print(f"{name} | {joined}", file = file3)



file_path = r"/home/dg/Documents/DataScience/Git/4B3b-Assignments-Project/DanielGeorge/FILES/classwork.csv"
assignment_file = open(file_path, "a")

fullname = input("Enter first name and Surname: ")
date_of_birth = input("Enter your date of birth: ")
fullname_split = fullname.split()
surname = fullname_split[1]
date_of_birth_split = date_of_birth.split("-")
birth_year = date_of_birth_split[0]
age = 2021 - int(birth_year)
print(f"{surname}, {len(surname)}, {age}", file = assignment_file)


print(fullname)



