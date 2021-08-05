#File path
sales_data = open("C:/Users/HP/OneDrive/Documents/Data_Science/Data Wrangling/Rawfile.txt", mode = "r", encoding = "utf-8")

#reading the txt file
entire_doc = sales_data.readlines()
# print(entire_doc[:7])#seeing the first seven 
# print(len(entire_doc))

refined_doc = [a.rstrip("\n") for a in entire_doc]# to strip \n in data

# print(refined_doc[:7])

# #Get Unique Dates
unique_dates = []
for item in refined_doc:
    date = item.split(" on ")[1]
    if date in unique_dates:
        pass
    else:
        unique_dates.append(date)
# print(unique_dates)

#To sort the unique dates
from datetime import datetime as dt
sorted_unique_dates = sorted(unique_dates, key = lambda a : dt.strptime(a, "%d-%m-%Y"))

for nd in sorted_unique_dates:
    # print(nd[3:])

# print(split_date)
    # print(sorted_unique_dates)


    sorted_transaction = []

for date in sorted_unique_dates:
    for transaction in refined_doc:
        if date == transaction.split(" on ")[1]:
            sorted_transaction.append(transaction)
        else:
            pass

# print(sorted_transaction[10:])

#To get the names, amount and dates separately
list_of_names = []
list_of_sales = []
list_of_dates = []

for transaction in sorted_transaction:
    name_to_append = transaction.split(" : ")[0]
    list_of_names.append(name_to_append)

    sales_to_append = transaction.split(" : ")[1].split(" on ")[0].lstrip("₦")
    list_of_sales.append(int(sales_to_append))

    date_to_append = transaction.split(" on ")[1]
    list_of_dates.append(date_to_append)
    
# print(list_of_names[:10])

#Preparation of second sheet
unique_agent = list(set(list_of_names))
unique_agent.sort()
# print(len(unique_agent))

#Total sales made by each agent
total_agent_sales = []

for person in unique_agent:
    individual_sum = 0
    for index, name in enumerate(list_of_names):
        if person == name:
            individual_sum += list_of_sales[index]
        else:
            pass
    
    total_agent_sales.append(individual_sum)


#To get the sum of all sales
sum_of_all_sales = sum(total_agent_sales)

contribution_list = [(item / sum_of_all_sales) * 100 for item in total_agent_sales]# contribution for each agents

#to get agent's commission
agents_commission = [item * 0.07 for item in total_agent_sales]

#Total revenue
total_revenue = sum(total_agent_sales)

#Total agent commission
total_agent_commission = sum(agents_commission)

#Net profit
net_profit = total_revenue - total_agent_commission


#Month with the highest and lowest sales
month_list = ["Jan", "Feb", "Mar" , "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
month_total_sales = []

for num in month_list:
    month_sales = 0
    for months in sorted_transaction:
        date_position = months.split(" on ")[1]
        converted_date = dt.strptime(date_position, "%d-%m-%Y")
        if converted_date.strftime("%b-%Y") == num +"-"+"2020":
            amount = months.split(" : ")[1].split(" on ")[0].lstrip("₦")
            # print(amount)
            month_sales += int(amount)
        else:
            pass  
    month_total_sales.append(month_sales)

max_month_sale = str(max(month_total_sales))
min_month_sale = str(min(month_total_sales))
for index, month in enumerate(month_total_sales):
    month = str(month) 
    if max_month_sale == month:
        highest_month = dt.strptime(month_list[index], "%b")
        full_month1 = highest_month.strftime("%B")
        print(f"The highest sales month is {full_month1}")
    elif min_month_sale == month:
        lowest_month = dt.strptime(month_list[index], "%b")
        full_month2 = lowest_month.strftime("%B")
        print(f"The lowest sales month is {full_month2}")
