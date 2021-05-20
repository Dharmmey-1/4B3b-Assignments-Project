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

home_work = r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/atha/FILES/data.csv"

file_csv = open(home_work, "a") #OPENING A FILE 


full_name = input("Enter your name: ") 
DOB = input("Enter your DOB: ")

split_DOB = DOB.split("-") # SPLITING BY DASH TO HAVE A LIST OF DOB1995-

list_year =split_DOB[0] #INDEXING TO CALL OUT THE  YEAR
# print(list_year)
age = 2021 - int(list_year) #ARITHMETIC TO GET THE AGE
# print(age)


# CODING FOR THE NAME
split_name = full_name.split(" ") # SPLITING BY DASH TO HAVE A LIST OF NAME

last_name = split_name[1] #INDEXING TO CALL OUT THE YEAR

len_name = len(last_name) # ADDING LEN TO GET THE LENGTH OF THE LAST NAME
# print(last_name)

output  =print(f"{last_name}, {len_name}, {age}", file=file_csv) #PRINTING USING FORMAT STRING AND ADDING IT TO THE CSV FILE.









