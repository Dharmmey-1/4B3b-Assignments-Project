# file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\biodata.csv"

# file = open(file_path, 'a')

# full_name = input('enter your full name: ')
# dob = input('enter your Date of Birth (yyyy-mm-dd): ')

# split_name = full_name.split(" ")
# last_name = split_name[1]
# name_length = len(last_name)

# dob_list = dob.split('-')
# year_of_birth = dob_list[0]
# birth_year = int(year_of_birth)

# age = 2021 - birth_year

# print(last_name, age, name_length)
# print(f"{last_name}, {name_length}, {age}", file=file)


# num_range = range(2,100)


# for numbers in num_range:
#     calculation = numbers/4

#     if type(calculation) == int:
#         print(numbers)


# # num = 29.8

# # print(type(num))


# for i in range(1,100):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#         else:
#             continue
#     else:
#         print(i)


# for i in range(1,10000000):
#     for j in range(2,i):
#         if (i*j)==2000000:
#             print(i,j)

# while loops

# x = 0
# while x <= 100:
#     print(x)
#     x+=1

# i = 1
# j = 1
# while  i<100:
#     while  j < 100:
#         if i%j == 0:
#              print(i,j)
       
#         i+=1
#         j+=1
# i = 0

# while i < 100:
#     j = 2

#     while j < i:
#         if i%j == 0:
#             break

#         j+=1

#     else:
#         print(i)

#     i+=1
# names = ["ali", "ade", "john", "sam"]
# scores = [89, 55, 23, 67]

# # for name, score in zip(names, scores):

# #     print(name, score)
# # print(list(zip(names,scores)))

# i = 0

# while i < len(scores):
#     name = names[i]
#     score = scores[i]

#     print(list(zip(names,scores)))
#     i += 1


#  FUNCTIONS THAT SHOWS A DATE

# import datetime

# def display_time():
#     print(type(datetime.datetime.now()))


# display_time()

def write_to_file(val1,val2):
    file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\random.csv"

    file = open(file_path, "a")
    file.write(f"{val1}, {val2}\n")

    file.close()


value = True
while value != "end":
    value = input('please enter a number \n use (end) to break out ->')

    if value.isnumeric():
        product = int(value) * 2

        write_to_file(value, product) 