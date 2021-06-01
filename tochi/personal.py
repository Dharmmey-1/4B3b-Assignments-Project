file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

file = open(file_path, 'r')

file_data = file.readlines()

# total_credits = 0
# total_debits = 0

# for line in file_data:
#     split_line = line.split(',')
#     credit_list = split_line[4]
#     debit_list = split_line[5]

#     if not credit_list.isalpha() and len(credit_list) > 1:
#         total_credits = total_credits + float(credit_list)

#     if not debit_list.isalpha() and len(debit_list)>1:
#         total_debits = total_debits + float(debit_list)

# print (total_credits)
# print(total_debits)

# print(f"Your account balance is: {total_credits-total_debits} ")
for line in file_data:
    split_line = line.split(',')
    credit = split_line[5]
    remark = split_line[6]

    if not credit.isalpha() and len(credit) > 1:
        total_credits = total_credits + float(credit)

    for item in remark:
        if item == "VALUE ADDED TAX":
            print(remark)
print(total_credits)


#     split_line = line.split(',')
#     balance_list.append(split_line[5])
#     debit_list.append(split_line[3])
#     remark_list.append(split_line[6])


# cleaned_balance = balance_list[1:-1]
# cleaned_debit = debit_list[1:-1]
# cleaned_remarks = remark_list[1:-1]

# # print(cleaned_balance)

# mapped_list = map(string_to_int, cleaned_balance)
# mapped_debit = map(string_to_int, cleaned_debit)


# for item in cleaned_remarks:
#     if item != "TRANSFER BETWEEN CUSTOMERS FRM SAMASKY NIG LTD TO ADEBESHI MUSIBAU":
#         print()


# main_list = (list(mapped_list))
# total_sum = max(main_list)
# print(total_sum)
