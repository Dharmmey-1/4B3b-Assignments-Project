
# FUNCTION DEFINITION
# import datetime

# def display_time():

#     print( datetime.datetime.now())
# # create function once and call it as many times as required

# display_time()
# display_time()
# display_time()

# def show_primes():

#     i = 0

#     while i < 100:

#         j = 2

#         while  j < i:

#             if i%j == 0:
#                 break

#             j+=1

#         else:
#             print(i)

#         i+=1


# show_primes()

# def fetch_and_agg_file():
#     file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

#     file = open(file_name, "r")

#     file_data = file.readlines()
#     total_credits = 0

#     for line in file_data:

#         # print(line.upper() )

#         split_line = line.split(",")

#         credit = split_line[4]

#         if not credit.isalpha() and len(credit)> 1:
#             total_credits = total_credits + float(credit)

#             # print(credit)

#     print(total_credits)

# def write_to_file(val1, val2):

#     file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\random.csv"

#     file = open(file_path, "a")

#     file.write(f"{val1},{val2}\n")

#     file.close()

# value = True

# while value != "end":

#     value = input("Please enter a number\n use (end) to break out > ")

#     if value.isnumeric():
#         product = int(value) * 2

#         write_to_file(value, product)
        

# def fetch_and_agg_file():
#     file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

#     file = open(file_name, "r")

#     file_data = file.readlines()
#     total_credits = 0

#     months = []
#     debits = []
#     credits = []

#     for line in file_data:

#         # print(line.upper() )

#         split_line = line.split(",")

#         credit = split_line[4]
#         credit = split_line[4]

#         if not credit.isalpha() and len(credit)> 1:
#             total_credits = total_credits + float(credit)

#             # print(credit)

#     print(total_credits)
# fetch_and_agg_file()

# available_months = []
# debits = []
# credits = []

# file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

# file = open(file_name, "r")

# file_data = file.readlines()
# header = file_data.pop(0) # REMOVE FIRST ROW OR FIRST LINE IN THE READLINES LIST AS THIS IS THE HEADER

# for line in file_data:
    
#     splitted_line = line.split(",") # split line into the individual values by comma since values are seperated by comma
#     trx_date = splitted_line[0]
#     month_n_year = trx_date[3:] # GET JUST MONTH AND YEAR
#     debit_value = splitted_line[3]
#     credit_value = splitted_line[4]

#     debit_value = float(debit_value) if debit_value != "" else 0
#     credit_value = float(credit_value) if credit_value != "" else 0

#     if month_n_year in available_months:
#         pass
#     else:
#         available_months.append(month_n_year)
#         debits.append([])
#         credits.append([])

#     debit_position = available_months.index(month_n_year)
#     debits[debit_position].append(debit_value)
#     credit_position = available_months.index(month_n_year)
#     credits[credit_position].append(credit_value)

# # print(available_months)
# # print(debits)
# # print(credits)

# # SUM UP VALUES 

# # debits_sum = list(map(sum, debits))
# # credits_sum = list(map(sum, credits))

# # print(credits_sum)
# # print(debits_sum)


# file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc_agg.csv"

# file = open(file_name, "w+")

# file.write(f"month,debit,credit\n")

# for month, debit, credit in zip(available_months, debits_sum, credits_sum):

#     # print(value)
#     statement = f"{month},{debit},{credit}\n"
#     file.write(statement)


# *



def aggregate():
    available_months = []
    debits = []
    credits = []

    file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

    file = open(file_name, "r")

    file_data = file.readlines()
    header = file_data.pop(0) # REMOVE FIRST ROW OR FIRST LINE IN THE READLINES LIST AS THIS IS THE HEADER

    for line in file_data:
        
        splitted_line = line.split(",") # split line into the individual values by comma since values are seperated by comma
        trx_date = splitted_line[0]
        month_n_year = trx_date[3:] # GET JUST MONTH AND YEAR
        debit_value = splitted_line[3]
        credit_value = splitted_line[4]

        debit_value = float(debit_value) if debit_value != "" else 0
        credit_value = float(credit_value) if credit_value != "" else 0

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

        # SUM UP VALUES 

        debits_sum = list(map(sum, debits))
        credits_sum = list(map(sum, credits))

    return {
        "available_months":available_months,
        "debits": debits_sum,
        "credits": credits_sum
    }


# def write_data(filename, **kwargs):

#     file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc_agg.csv"

#     file = open(file_name, "w+")

#     file.write(f"month,debit,credit\n")

#     for month, debit, credit in zip(*kwargs.values()):

#         # print(value)
#         statement = f"{month},{debit},{credit}\n"
#         file.write(statement)

# aggregates = aggregate()
# write_data("", **aggregates)



#  ARGS AND KWARGS

# def add_nums(x, y):
#     print(x + y)

# add_nums(10, 20)

# def add_nums(x, y, z, q, c, d):
#     print(x + y + z + q+c+d)

# add_nums(10, 20, 12, 42, 9,13)

# def add_nums(*nkechi):
#     print(nkechi)
#     print(sum(nkechi))

# # add_nums(10, 20, 2,3, 4,5,65,57,67,87,4,12)
# add_nums(10, 20, 2,3, 4,5,65,57,67,87,4,12)

# def greet(*kwargs):
#     print(kwargs)

# greet(x = 1, y = 3, z= 5)

# def write_data(filename, **kwargs):

#     file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc_agg.csv"

#     file = open(file_name, "w+")

#     file.write(f"month,debit,credit\n")

#     for values in zip(*kwargs.values()):

#         # print(value)
#         values = map(str, values)
#         statement = f"{','.join(values)}\n"
#         file.write(statement)

# a = ["a", "b", "c"]
# b = [1,2,3]
# c = [5,6,7]
# d = [12, 23, 90]
# f = [23,54,1,9]

# write_data("", a=a, b=b, c=c, d=d,f = f)

# aggregates = aggregate()
# write_data("", **aggregates)