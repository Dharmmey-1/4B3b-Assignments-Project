file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

file = open(file_path, "r")
file_lines = file.readlines()

new_file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\cleaned_statement.csv"
cleaned_file = open(new_file_path, "a")

csv_statements = []
target = "Nov"

trans_date_list = []
credit_list = []
debit_list = []

for lines in file_lines:
    split_lines = lines.split(',')
    trans_date = split_lines[0]
    debits = split_lines[3]
    credits = split_lines[4]
    if target in trans_date:
        debit_list.append(debits)
        credit_list.append(credits)
        trans_date_list.append(trans_date)

# main_list = csv_statements.append(trans_date_list)

print(f"{trans_date_list},{credit_list},{debit_list}", file=cleaned_file)