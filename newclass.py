file_path = r"C:\Users\HP\OneDrive\Desktop\4B3b-Assignments-Project\VIctor\Files\data.csv"
file_edit = open(file_path, "a")


full_name = input("Enter full name: ")
DateofBirth = input("Enter Date of Birth: ")

split_name = full_name.split()
last_name = split_name[1]

split_date = DateofBirth.split("-")
YearofBirth = split_date[0]
age = 2021 - int(YearofBirth)

print(f'{last_name}, {len(last_name)}, {age}', file = file_edit)
