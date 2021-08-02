import xlwt
from tempfile import TemporaryFile

sales_data = open(r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/Rawfile.txt", mode = "r", encoding = "utf-8")

#reading the txt file
entire_doc = sales_data.readlines() # IT REYRNS A LIST OF LINES FROM THE FILE

#having an overview
# print(entire_doc[:7])

# to strip  out the new line line thingy
refined_doc = [a.rstrip("\n") for a in entire_doc]

# print(refined_doc[:7])



#GET UNIQUE DATES
unique_dates = []
for item in refined_doc:
    date = item.split(" on ")[1]
    if date in unique_dates:
        pass
    else:
        unique_dates.append(date)


# print(unique_dates)


#TO SORT THE UNIQUE DATES

from datetime import datetime as dt

sorted_unique_dates = sorted(unique_dates, key = lambda a : dt.strptime(a, "%d-%m-%Y"))

# print(sorted_unique_dates)



#TO MAKE THE DATA SORTED BY DATE
# SORTED TRANSACTION IS NOW THE CLEANED RWAFILE TEXT WITH (: AND ON)
sorted_transaction = []
for date in sorted_unique_dates:
    for transaction in refined_doc:
        if date == transaction.split(" on ")[1]:
            sorted_transaction.append(transaction)
        else:
            pass
# print(sorted_transaction[-10:]) 

#To GET THE NAMES, AMOUNT  AND DATES SEPERATELY
list_of_names = []
list_of_sales = []
list_of_date = []

for transaction in sorted_transaction:
    #SPLITING TO GET THE NAMES SEPERATELY
    name_to_append = transaction.split(" : ")[0]
    list_of_names.append(name_to_append)

#SPLITING TO FECTH THE SALES
    sales_to_append = transaction.split(" : ")[1].split(" on ")[0].lstrip("₦")
    list_of_sales.append(int(sales_to_append))

#SPLITTING TO FEATCH TGHE DATE
    date_to_append = transaction.split(" on ")[1]
    list_of_date.append(date_to_append)
# print(list_of_date[-10:])  
# 


#CODE FOR DATABASE
import csv 
greymart_to_csv = open(r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/Greymart_in_csv.csv", mode = "w", newline="", encoding = "utf-8") #the new line is to move the csv to new line


pen = csv.writer(greymart_to_csv)
pen.writerow(["name", "sales", "date"]) #is to write it a row  and it's must be a list.
for num in range(len(list_of_names)): # In range, we must know the number of times we want to iterate.
    pen.writerow([list_of_names[num], list_of_sales[num], list_of_date[num]])  #slicing to get the items for each names, sales and date

greymart_to_csv.close()


# END OF DATABASE CODE




##PREPARATION OF SECOND SHEET

#THe UNIQUE AGENT
unique_agent = list(set(list_of_names)) #we used set so that the AGENT NAME WON'T REPEAT IT SELF
unique_agent.sort() #TO MAKE THE UNIQUE AGENT GET SORTED ALPHABETICALLY
# print(unique_agent)


#TO GET THE TOTAL SALES MADE BY EACH AGENT
#The individual sum will append the total agent sales whenever person is equal to name and run the loop again to check till it can find where person is not equal to name
total_agent_sales = []

for person in unique_agent:
    individual_sum = 0
    for index, name in enumerate(list_of_names):
        if person == name:
            individual_sum += list_of_sales[index]
        else:
            pass
    total_agent_sales.append(individual_sum)
# print(total_agent_sales[-10:])
    

#To GET THE SUM OF ALL SALES
sum_of_all_sales = sum(total_agent_sales)

#TO GET THE CONTRIBUTIONS MADE BY EACH AGENT
#the 
contribution_list = [(item / sum_of_all_sales) * 100 for item in total_agent_sales]


#TO GET AGENT COMMISSION
agents_commission  = [item * 0.07 for item in total_agent_sales]


#TOTAL REVENUE
total_revenue = sum(total_agent_sales)


# TOTAL AGENT COMISSION
total_agent_commission = sum(agents_commission)

#NET PROFIT
net_profit = total_revenue - total_agent_commission






#GETTING THE BOOK
book = xlwt.Workbook()


#ADDING THE SHEETS TO THE BOOK/EXCEL FILE
sheet_one = book.add_sheet("All Transaction")
sheet_two = book.add_sheet("Agents' transaction")
sheet_three = book.add_sheet("Financial Statement")


#WRITING INTO THE FIRST SHEET

#THE FIRST THING IS TO WRITE  THE HEADER OF THE TABLE
sheet_one.write(0, 0, "Name")
sheet_one.write(0, 1, "Amount")
sheet_one.write(0, 2, "Date")


#WRITING THE REST OF THE DATA
for index, name  in enumerate(list_of_names):
    sheet_one.write(index + 1, 0, name)


for index, amount  in enumerate(list_of_sales):
    sheet_one.write(index + 1, 1, amount)


for index, date  in enumerate(list_of_date):
    sheet_one.write(index + 1, 2, date)


#WRITING INTO THE SECOND SHEET


#WRITING THE HEADERS IN SECOND SHEET USING FOR LOOP
list_of_sheet_two_headers = ["Agent Name", "Sales by Agent", "Contribution", "Commission"]
for index, header in enumerate(list_of_sheet_two_headers):
    sheet_two.write(0, index, header) #in this scenario we don't need to increment index beacause they are in the same row

#WRITING THE REST OF THE DATA 

for index, agent_name in enumerate(unique_agent):
    sheet_two.write(index +1, 0, agent_name)


for index, agent_sales in enumerate(total_agent_sales):
    sheet_two.write(index + 1, 1, agent_sales)


for index, agent_contribution in enumerate(contribution_list):
    sheet_two.write(index + 1, 2, agent_contribution)


for index, commission in enumerate(agents_commission):
    sheet_two.write(index + 1, 3, commission)




#WRITING INTO THE THIRD SHEET

sheet_three.write(0, 0, "Total revenue")
sheet_three.write(0, 1, "Total Agent Commissiom")
sheet_three.write(0, 2, "Net Profit")


#WRITING THE DATA
sheet_three.write(1, 0, total_revenue)
sheet_three.write(1, 1, total_agent_commission)
sheet_three.write(1, 2, net_profit)



#SPECIFYING THE FILRPATH AND FILENAME


book_path = "/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/grey.xls"
# book_path = "/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/greymart.xls"

#SAVING THE FILE
book.save(book_path)
book.save(TemporaryFile())

print("All Done")





#ASSIGNMENT FROM GREYMART
# N0 1
#TO GET THE MOST PERFORMING AGENT
sorted_total_agent_sales = sorted(total_agent_sales, reverse = True)
# print(sorted_total_agent_sales)

top_perfroming_sales = sorted_total_agent_sales[:1]
# print(top_perfroming_sales)


#USING THE  TOP PERFROMING SALES TO GET THE TOP PERFORMING AGENT, WE NEED TO RUN A NESTED FOR LOOP TO MATCH THE EXACT AGENT

top_performing_agent = []
for  sales in top_perfroming_sales:
    for agent, amount in list(zip(unique_agent,total_agent_sales)): #zip combines two or more iterable
        if sales == amount:
            top_performing_agent.append(agent)
        else:
            pass
print(f"The top performing agent is {top_performing_agent}")    #SHAE BUGS





#NO 2
#TO GET THE LEAST PERFORMING AGENT
sorted_total_agent_sales_two = sorted(total_agent_sales)
least_perfroming_sales = sorted_total_agent_sales_two[:1]



#USING THE  LEAST  PERFROMING SALES TO GET THE LEAST PERFORMING AGENT, WE NEED TO RUN A NESTED FOR LOOP TO MATCH THE EXACT AGENT
least_perfroming_agent = []

for sales in least_perfroming_sales:
    for agent, amount in list(zip(unique_agent, total_agent_sales)):
        if sales == amount:
            least_perfroming_agent.append(agent)
        else:
            pass
print(f"The least performing agent is {least_perfroming_agent}") #Darby Nakken


#NO3
#IF THE COMMISION IS MEANT TO BE THE CHANGE TO !7%, WHAT WILL BE THE PERCENTAGE DROP?


#TO GET AGENT COMMISSION FOR 17% 
agents_commission_2 = [item * 0.17 for item in total_agent_sales]



# TOTAL AGENT COMISSION(17%)
total_agent_commission_2= sum(agents_commission_2)
# print(sum(agents_commission_2))

#NET PROFIT(WHEN D COMISSION IS 17%)
net_profit_2 = total_revenue - total_agent_commission_2
# print(net_profit_2)
# print(net_profit)


#DROP 
decrease = net_profit_2 - net_profit
# print(decrease)

# % DROP
decrease_in_percentage = (decrease /  net_profit) * 100
print(f"The percentage drop is {decrease_in_percentage}")  #-10.752688172043028 # BEACUSE IT IS A NEGATIVE NUMBERS

 


#NO 4

# TO GET DATE WITH THE HIGHEST SALES

sorted_total_agent_sales = sorted(total_agent_sales, reverse=True)
top_perfroming_sales = sorted_total_agent_sales[:1]

date_with_the_most_sales = []
for sale in top_perfroming_sales:
    for date, amount in list(zip(unique_dates, sorted_total_agent_sales)):
        if sale == amount:
            date_with_the_most_sales.append(date)
        else:
            pass
print(f"(The date with the highest sales {date_with_the_most_sales})")



# ANOTHER WAY TO SOLVE NO 4.

date_with_the_most_sales = []
for sales in list_of_sales:
    sorted_for = sorted(zip(unique_dates,list_of_sales), key= lambda a: a[1])[-1]
print(sorted_for)
# for date, amount in sorted_for:
#     if sales == amount:
#         date_with_the_most_sales.append(sorted_for)
    
# print(date_with_the_most_sales)



# ('12-11-2020', 24737049)]








#NO 5
# A CSV FILE THAT HAS THE TRANSACTION GROUPED IN MONTH AND SALES

# We need to get the Total Sales made by month

list_of_month = ["Jan", "Feb", "Mar" , "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]

total_month_sales = []

for number in list_of_month:
    month_sum = 0
    for  months in sorted_transaction:
        split_of_date = months.split(" on ")[1]
        converted_date = dt.strptime(split_of_date, "%d-%m-%Y")
        if converted_date.strftime("%b-%Y") == number+"-"+"2020":
            amount = months.split(" : ")[1].split(" on ")[0].lstrip("₦")
            month_sum += int(amount)
        else:
            pass
    total_month_sales.append(month_sum)
# print(total_month_sales)

max_sales_of_month = str(max(total_month_sales))
# print(month_highest_sales)
min_sales_of_month = str(min(total_month_sales))


for index, month in enumerate(total_month_sales):
    month = str(month)

    if max_sales_of_month == month:
        highest_month =dt.strptime(list_of_month[index], "%b")
        month_with_highest_sales = highest_month.strftime("%B")
        # print(f"The month with highest sales is {highest_month}")
        print(f"The month with highest sales is {month_with_highest_sales}")
    elif min_sales_of_month == month:
        least_month = dt.strptime(list_of_month[index], "%b")
        month_with_lowest_sales = least_month.strftime("%B")
        print(f"The month with lowest sales is {month_with_lowest_sales}")








#TO WRITE THE TOTAL SALES BY MONTH INTO CSV  
import csv 
transaction_to_csv = open(r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/transaction_in_csv.csv", mode = "w", newline="", encoding = "utf-8") #the new line is to move the csv to new line


pen = csv.writer(transaction_to_csv)
pen.writerow(["Month", "Sales"]) #is to write it a row  and it's must be a list.
for num in range(len(list_of_month)): # In range, we must know the number of times we want to iterate.
    pen.writerow([list_of_month[num], total_month_sales[num]])  #slicing to get the items for each month and sales

transaction_to_csv.close()












            





