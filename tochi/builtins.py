# file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\kpk.txt"

# # file = open(file_path, "r")
# # print(file)
# # print(file.read())


# file2 = open(file_path, 'a')  # open the file in write mode

# print(1991, 2, 3, sep='\n', end=" | ", file=file2)


# numbers = range(10)
# list_numbers = list(numbers)

# print(list_numbers)


# even_numbers = range(2, 20, 2)

# list_even = list(even_numbers)

# for value in range(2, 6, 1):
#     print(value*100)


# names = ['ali', 'john', 'busayo']


# def func(value): return f"{value} -> {len(value)}"


# map_names = map(func, names)

# list_map = list(map_names)

# print(list_map)


# numbers = range(1, 8)


# def square_funtion(x): return x * x


# list_numbers = list(numbers)

# map_numbers = map(square_funtion, list_numbers)

# print(list(map_numbers))


# filter

# numbers = [90, 80, 20, 30, 60, ]

# function = lambda score: score > 60

# filtered_list = filter(function, numbers)

# print(list(enumerate(filtered_list)))

# for value in enumerate(numbers):
#     print (value)


# # practiceing if statements

# if len(numbers)<5:
#     print('true')else:
#     ()


# score = 70

# ade = "passed" if score >=60 else "Fail"


# print (ade)


# numbers = [90, 80, 20, 85, 55, 48, 23, 74]


# def func(score): return score > 60


# map_score = map(func, numbers)

# list_map = list(map_score)

# for value in list_map:
#     if value == True:
#         print('passed')
#     else:
#         print('failed')


# numbers = [90, 80, 20, 85, 55, 48, 23, 74]

# func = lambda score: "Passed" if score>=60 else "Average" if score > 49 and score< 60 else "Fail"

# mapped = map(func, numbers)

# print(list(mapped))

# headache = input("Do you have a headache(t/f): ")

# if headache == 't':
#     has_fever = input('Do you have fever ? (t/f) ')
#     if has_fever == 't':
#         is_coughing = input(' Are you coughing? (t/f) ')
#         if is_coughing == "f":
#             print('see a doctor')
#         else:
#             print('contact NCDC')

#     else:
#         bitter_taste = input(' Do you have biiter taste ? (t/f) ')
#         if bitter_taste == 't':
#             print('You probably have malaria')
#         else:
#             print( "You have a heart break. Go and see a therapist")

# else:
#     print('ee go be ')


# file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

# file = open(file_path, 'r')

# file_data = file.readlines()

# credit_list = []
# for line in file_data:
#     split_line = line.split(',')
#     credit_list.append(split_line[4])


# # print(credit_list)
# cleaned_list = credit_list[1:-1]
# # print(cleaned_list)


# def func(num): return float(num)


# mapped_list = map(func, cleaned_list)

# print(list(mapped_list))


# num_range = range(100, 340)

# for value in num_range:
#     var = value*3
#     var_string = str(var)
#     multiplied_list = list(var_string)

#     val_string = str(value)
#     original_values = list(val_string)

#     if original_values[2] == multiplied_list[0] == multiplied_list[1] == multiplied_list[2]:
#         print(original_values)



