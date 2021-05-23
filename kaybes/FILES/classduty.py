# headache_prognosis = input("Do you have a headache (t/f): ")
# if headache_prognosis == "f":
#     print("E go be!")
# else:
#     has_fever = input("Do you have fever (t/f): ")
#     if has_fever == "t":
#         is_coughing = input("Are you coughing (t/f): ")
#         print("See a doctor!")
#     else:
#         bitter_taste = input("Bitter taste?: ")
#         if bitter_taste == "t":
#             print("It is probably malaria")
#         else:
#             print("It's a heart break")
    

#FOR LOOPS AND WHILE LOOPS

# file_path = r"C:\Users\nezepue\Desktop\4B3b-Assignments-Project\atha\FILES\gtb_doc.csv"
# class_file = open(file_path, "r")
# file_data = class_file.readlines()

# credit_list = []
# for line in file_data:
#     split_line = line.split (",")
#     credit = split_line[4]
#     credit_list.append(credit)


# credit_real = credit_list[1:-1]
# print(credit_real)
    
# function = map(int, credit_real)
# print(list(function))


# file_path = r"C:\Users\nezepue\Desktop\4B3b-Assignments-Project\a   tha\FILES\gtb_doc.csv"
# class_file = open(file_path, "r")
# file_data = class_file.readlines()

# function = lambda score: 
# # filtered_list = filter(function, numbers)

def nkechi(start_at=1, stop_at=9):
    result = []
    for x in range(start_at, stop_at):
        for y in range(start_at, stop_at):
            for z in range(start_at, stop_at):
                sum = x * 100 + y * 10 + z
                target = z * 100 + z * 10 + z
                if sum * 3 == target:
                    result.append(sum)
    return result



print(nkechi())
print(nkechi(0, 20))
print(nkechi(0, 50))