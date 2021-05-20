# file_name = r"C:\Users\nezepue\Desktop\4B3b-Assignments-Project\kaybes\FILES\kpk.txt"
# file = open(file_name, "r")
# #print(file)
# print(file.read())

# #file.close()

# file2 = open(file_name, "w")
# file2.write("Hello, I am female\n")
# file2.write("and I am four years old\n")
# file2.write("I also live in the North\n")

# #file2.close()

# print(1991, 1992, 1993)
# print(1989, 1990, 1991, sep = "-")
# print(1, 2, 3, sep = "-", end = "|")
# print(1, 2, 3, sep = "-", end = "|")
# print(1, 2, 3, sep = "-", end = "|")
# print("Today is a beautiful day", file = file2)




# file_path = r"C:\Users\nezepue\Desktop\4B3b-Assignments-Project\kaybes\FILES\opg.txt"
# class_file =  open(file_path, "a")

# value_of_x = int(input("x = "))
# value_of_y = int(input("y = "))
# Answer = (value_of_x * value_of_y)
# print(f"{value_of_x} x {value_of_y} = {Answer}", file = class_file)

# name = "Nkechi is my name"
# reversed_name = (reversed(name))
# print(reversed_name)

# reversed_name = list(reversed(name))
# print(reversed_name)

# joined_name = ".". join(reversed_name)
# print(joined_name)

# name_input = input("Enter name here: ")
# reversed_name = list(reversed(name_input))
# print(reversed_name)
# joined_name = "".join(reversed_name)
# print(joined_name)
# print( f"{name_input}| {joined_name}", end = "|", file = class_file)


file_path = r"C:\Users\nezepue\Desktop\4B3b-Assignments-Project\kaybes\FILES\classwork.csv"
class_file = open(file_path, "a")
full_name = input("Enter Full Name: ")
date_of_birth = input("Enter Date of Birth: ")
split_date = date_of_birth.split("-")
year_of_birth = split_date[0]
age = 2021 - int(year_of_birth)
split_name = full_name.split()
last_name = split_name [1]
print(f"{last_name}, {len(last_name)}, {age}",file = class_file)

