file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\cleaned_statement.csv"

file = open(file_path, "r")

# file_lines = file.readlines()
month = input("Which month do you want to see the total debits for? ->: ")


target = month.capitalize()
str_to_int = lambda num: int(num)
credit_list = []

for lines in file:
    split_lines = lines.split("]")
    if target in lines:
        credit_list.append(split_lines[2])

total = 0
for item in credit_list:
    if not item: 
        print(type(item))
        