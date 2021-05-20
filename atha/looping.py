file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

file = open(file_name, "r")

file_data = file.readlines()

for line in file_data:

    print(line.upper() )