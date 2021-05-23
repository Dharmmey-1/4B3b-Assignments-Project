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


# file_path = r"C:\Users\nezepue\Desktop\4B3b-Assignments-Project\kaybes\FILES\classwork.csv"
# class_file = open(file_path, "a")
# full_name = input("Enter Full Name: ")
# date_of_birth = input("Enter Date of Birth: ")
# split_date = date_of_birth.split("-")
# year_of_birth = split_date[0]
# age = 2021 - int(year_of_birth)
# split_name = full_name.split()
# last_name = split_name [1]
# print(f"{last_name}, {len(last_name)}, {age}",file = class_file)


#range
# numbers = range(10)
# print(numbers) #returns a generator object
# list_numbers = list(numbers) #convert object into list to view
# print(list_numbers)
# even_numbers = range(2,20,2)
# print(list(even_numbers))

# for value in range (2,6,1):
#     print(value)

# for value in range (2,6,1):
#     print(20)

# number = 14
# for value in range (2,6,1):
#     print(number)

# for value in range (2,6,1):
#     print(value * 50)

# names = ["ali", "john", "jonah"]
# len_names = map(len, names)
# print(list(len_names))

# numbers = ["2", "4", "6", "8"]
# func = lambda number: number * number
# print(func(12))

# numbers = range(1,8)
# function = lambda number: number * number
# squared_numbers = map(function, numbers)
# print(list(squared_numbers))

# numbers = [90, 80, 20, 95, 55, 48, 23, 74]
# function = lambda score: score > 60
# filtered_list = filter(function, numbers)
# print(list(filtered_list))


# numbers = [90, 80, 20, 95, 55, 48, 23, 74]
# enumerated_list = enumerate(numbers)
# listed_enumerated_numbers = list(enumerated_list)
# print(listed_enumerated_numbers)


# numbers = [90, 80, 20, 95, 55, 48, 23, 74]
# for x in enumerate(numbers):
#     print(x)
#     print(x[0])
#     print(x[1])

# if "a" in "ber":
#     print("foo")
# elif 10/2:
#     print("good")

# score = 60
# ade = "passed" if score >=60 else "fail"
# print(ade)

# numbers = [90, 80, 20, 95, 55, 48, 23, 74]
# function = lambda score: "passed" if score >= 60 else "failed"
# list_numbers = map(function, numbers)
# grade = list(list_numbers)
# print(grade)


# for number in range (len (list_result)):
#     if list_result[0] numbers = [0,1,2,3,4,5,6,7,8,9]
# function = lambda number: number * 3
# possible_x = map(function, numbers)
# possible_list = list(possible_x)
# result = zip(numbers, possible_list)
# list_result = lisin list_result[1]:
# print(list_result)



#METHOD ONE
numbers = range (0,10)
for x in numbers:
    for y in numbers:
        for z in numbers:
            sum = (x * 100) + (y * 10) + (z * 1)
            result_sum = (z * 100) + (z * 10) + (z * 1)
            if sum * 3 == result_sum:
                value_of_xyz = result_sum/3
                print(int(value_of_xyz))



#METHOD TWO
def nkechi(start_at=1, stop_at=9):
    result = []
    for x in range(start_at, stop_at):
        for y in range(start_at, stop_at):
            for z in range(start_at, stop_at):
                sum = x * 100 + y * 10 + z
                target = z * 100 + z * 10 + z
                if sum * 3 == target:
                    result.append(sum)
    return result
print(nkechi())
