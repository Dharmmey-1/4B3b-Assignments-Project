file_name = r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/KPK.TXT" #RElATIVE
# file = open(file_name, "r") #OPEN FILE IN REAM ME
# # print(file)
# print(file.read())

# file.close()

# file2 = open(file_name, "w") #OPEN FILE IN WRITE MODE
# file2.write("Hello, I am a Man \n")
# file2.write("Hello, I am a  Data Scientist")
# file2.write("Where do  you leave")
# # print(file2)
# file2.close()

# file2 = open(file_name, "r")
# print(file2)

# file.close()

# file2 = open(file_name, "a")
# file2.write("This is an update \n")

# file2.close()

# print(1991, 2, 3, sep = "->")
# print(1991, 2, 3, sep = "->", end = " | ")
# print(1991, 2, 3, sep = "->", end = " | ", file=file2)



#CLASS WORK
# class_work = r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/classwork.txt"

# file_class = open(class_work, "a")

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# z = x * y
# print(f'{x} * {y} = {z}', file=file_class)


# name = input("Enter the name: ")


# back = list(reversed(name))
# back_join = "".join(back)
# print(f'{name} | {back_join}', file=file_class )


#HOME-WORK
#CREATING A PATH FOR THE CSV

# home_work = r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/atha/FILES/data.csv"

# file_csv = open(home_work, "a") #OPENING A FILE 


# full_name = input("Enter your name: ") 
# DOB = input("Enter your DOB: ")

# split_DOB = DOB.split("-") # SPLITING BY DASH TO HAVE A LIST OF DOB1995-

# list_year =split_DOB[0] #INDEXING TO CALL OUT THE  YEAR
# # print(list_year)
# age = 2021 - int(list_year) #ARITHMETIC TO GET THE AGE
# # print(age)


# # CODING FOR THE NAME
# split_name = full_name.split(" ") # SPLITING BY DASH TO HAVE A LIST OF NAME

# last_name = split_name[1] #INDEXING TO CALL OUT THE YEAR

# len_name = len(last_name) # ADDING LEN TO GET THE LENGTH OF THE LAST NAME
# # print(last_name)

# output  =print(f"{last_name}, {len_name}, {age}", file=file_csv) #PRINTING USING FORMAT STRING AND ADDING IT TO THE CSV FILE.



# #RANGE
# for value in range(2, 6, 1):
#     print(value)


#MAP
# it allows running a 

name = ['all', 'john', 'jonah']
# list_of_name_lens = map(len, name)
# print(list_of_name_lens) #RETURNS A GENERATOR OBJECT
# print(list(list_of_name_lens))


# #LAMDA
# func = lambda value: f" {value} ->  {len(value)}"
# list_of_func = map(func, name)
# print(list(list_of_func))



number = range(1, 8)
func = lambda number: number * number
# print(func)
squared_number = map(func, number)
print(list(squared_number))

# #FILTER
# numbers = [90, 80, 20, 95, 55,48, 23, 74]
# func =lambda score: score > 60
# filtered_list = filter(func, numbers)
# print(list(filtered_list))

#ENUMEARTE
# print(list(enumerate(numbers)))

# for value in enumerate(numbers):  # I WANT IT TO SHOW VERTICALLY
#     print(value[1])

# MY SOlUTION
# numbers = [90, 80, 20, 95, 55,48, 23, 74]

# func = lambda score: score >= 60
# check_number =  map(func, numbers)

# correct = (list(check_number))


# for score in correct:
#     if score == True:
#         print('Passed')
#     else:
#         print('Fail')

# print("True") if correct >= 60  else print('False')


# # ATHA SOLUTION
# numbers = [90, 80, 20, 95, 55,48, 23, 74]
# func = lambda score: "passed" if score >=60 else 'fail'
# mapped = map(func, numbers)
# print(list(mapped))



#DIAGONOSTIC
# headache = input("Do you have a headache ?  (t/f): ")

# if headache == "t":
#     has_fever = input("Do you have fever ? (t/f): ")
#     if has_fever == "t":
#         is_coughing = input("Are you coughing? : ")
#         if is_coughing == "t":
#             print("Contact NCDC")
#         else:
#             print("See a Doctor")


#     else:
#         bitter_taste = input("Bitter Taste: ") 
#         if bitter_taste == "t":
#             print("Probably Malaria")
#         else:
#             print("Heart Break")    


# else:
#     print("E go be")




file_name = r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/atha/gtb_doc.csv"

file = open(file_name, "r")

file_data = file.readlines()

total_credit = 0

for line in file_data:
    split_line  = line.split(",")
    credit = split_line[4]

    if not credit.isalpha() and len(credit) > 1:
        total_credit = total_credit + float(credit)
        print(total_credit)

2, 
total-debits = 0
debit = split_line[3]
remarks = split_line[6]
target_remark = "VALUE ADDED TAX"

if not debit.isalpha() and len(debit) > 1 and target_remark in remarks:
      total_debits = total_debits + float(debit)
        print(total_debit)
    




    


    

    





