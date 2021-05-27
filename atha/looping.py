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


# file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

# file = open(file_name, "r")

# file_data = file.readlines()
# total_debits = 0

# for line in file_data:

#     # print(line.upper() )

#     split_line = line.split(",")

#     debit = split_line[3]
#     remarks = split_line[6]

#     target_remark = "CHEQUE DEPOSIT"
    
#     if not debit.isalpha() and len(debit)> 1 and target_remark in remarks:
#         total_debits = total_debits + float(debit)

#         # print(debit)

# print(total_debits)

# num_range = range(100, 340)

# for value in num_range:
    
#     if str(value)[-1]*3 == str(value*3):

#         print(value)


# for i in range(1,100):
#     for j in range(2,i):
#         if i%j ==0:
#             break
#         else:
#             continue

#     else:
#         print(i)

# for i in range(1,100):
#     print(i)

# i = 0

# while i < 100:
#     print(i)
#     i+= 1


# i = 0

# while i < 100:

#     j = 2

#     while  j < i:

#         if i%j == 0:
#             break

#         j+=1

#     else:
#         print(i)

#     i+=1


# names = ["ali", "ade", "john", "sam"]
# scores = [89, 55, 23, 67]

# for name, score in zip(names, scores):

#     print(name, score)

# print(list(zip(names, scores)))


# i = 0

# while i < len(scores):

#     name = names[i]
#     score = scores[i]

#     print(name, score)
#     i+=1

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

def fetch_and_agg_file():
    file_name = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"

    file = open(file_name, "r")

    file_data = file.readlines()
    total_credits = 0

    for line in file_data:

        # print(line.upper() )

        split_line = line.split(",")

        credit = split_line[4]

        if not credit.isalpha() and len(credit)> 1:
            total_credits = total_credits + float(credit)

            # print(credit)

    print(total_credits)