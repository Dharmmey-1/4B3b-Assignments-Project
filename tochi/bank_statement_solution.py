
available_months = []
debits = []
credits = []

file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\atha\gtb_doc.csv"
file = open(file_path, 'r')
file_data = file.readlines()
file_data.pop(0)

for line in file_data:
    splitted_line = line.split(',')
    trx_date = splitted_line[0]
    month_n_year = trx_date[3:]
    debit_value = splitted_line[3]
    credit_value = splitted_line[4]

    debit_value = float(debit_value) if debit_value else 0
    credit_value = float(credit_value) if credit_value else 0

    if month_n_year in available_months:
        pass
    else:
        available_months.append(month_n_year)
        debits.append([])
        credits.append([])
    debit_position = available_months.index(month_n_year)
    debits[debit_position].append(debit_value)
    credit_position = available_months.index(month_n_year)
    credits[credit_position].append(credit_value)

debits_sum = list(map(sum, debits))
credits_sum = list(map(sum, credits))


# print(available_months)
print(debits_sum)
print(credits_sum)


file_name = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\atha\gtb_doc_agg.csv"

file = open(file_name, 'w+')

for month, debit, credit, in zip(available_months, credits_sum, debits_sum):
    # print(value)
    statement = f"{month}, {debit}, {credit}\n"
    file.write(statement)