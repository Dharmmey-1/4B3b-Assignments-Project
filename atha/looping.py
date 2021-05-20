# file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

# file = open(file_name, "r")

# file_data = file.readlines()
# total_credits = 0

# for line in file_data:

#     # print(line.upper() )

#     split_line = line.split(",")

#     credit = split_line[4]

#     if not credit.isalpha() and len(credit)> 1:
#         total_credits = total_credits + float(credit)

#         # print(credit)

# print(total_credits)


file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

file = open(file_name, "r")

file_data = file.readlines()
total_debits = 0

for line in file_data:

    # print(line.upper() )

    split_line = line.split(",")

    debit = split_line[3]
    remarks = split_line[6]

    target_remark = "CHEQUE DEPOSIT"
    
    if not debit.isalpha() and len(debit)> 1 and target_remark in remarks:
        total_debits = total_debits + float(debit)

        # print(debit)

print(total_debits)