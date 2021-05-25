
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

def write_to_file(val1, val2):

    file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\4B3b-Assignments-Project\atha\FILES\random.csv"

    file = open(file_path, "a")

    file.write(f"{val1},{val2}\n")

    file.close()

value = True

while value != "end":

    value = input("Please enter a number\n use (end) to break out > ")

    if value.isnumeric():
        product = int(value) * 2

        write_to_file(value, product)
        