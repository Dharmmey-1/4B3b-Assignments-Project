file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\biodata.csv"

file = open(file_path, 'a')

full_name = input('enter your full name: ')
dob = input('enter your Date of Birth (yyyy-mm-dd): ')

split_name = full_name.split(" ")
last_name = split_name[1]
name_length = len(last_name)

dob_list = dob.split('-')
year_of_birth = dob_list[0]
birth_year = int(year_of_birth)

age = 2021 - birth_year

print(last_name, age, name_length)
print(f"{last_name}, {name_length}, {age}", file=file)
