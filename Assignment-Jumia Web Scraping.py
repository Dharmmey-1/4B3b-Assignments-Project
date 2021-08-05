import requests
from bs4 import BeautifulSoup
   
#URL Link
url = 'https://jumia.com.ng/smartphones/?page={pages}#catalog-listing'
phone_b = []
phone_s = []
old_p = []
new_p = []
rate = []

#scraping the brand, specs, old and new price and ratings of all smartphones from pages 1 to 50
for pages in range(1, 51):
    headers = requests.utils.default_headers()

    headers.update({"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"})
    my_response = requests.get(url, headers)

    soup = BeautifulSoup(my_response.text, features="lxml")

    initial_search = soup.find("div", attrs={"class": "-paxs row _no-g _4cl-3cm-shs"})

    further_search = soup.find_all("article", attrs={"class": "prd _fb col c-prd"})


    
    for phone_soup in further_search:
        # to filter out everything for phone brand
        phone_details = phone_soup.find("a")
        # Phone band
        try:
            # to get brand from the attributes
            phone_brand = phone_details["data-brand"]
            phone_b.append(phone_brand)
        except:
            phone_brand = None
            phone_b.append(phone_brand)
            pass

        try:
            phone_spec = phone_details["data-name"]
            phone_s.append(phone_spec)
        except:
            phone_spec = None
            phone_s.append(phone_spec)
            pass

        # Old price
        try:
            old_price_details = phone_soup.find("div", attrs={"class": "old"})
            old_price_raw = old_price_details.text
            # print(old_price_raw)
            if "," in old_price_raw:
                step_one = old_price_raw.lstrip("₦ ")
                step_two = step_one.split(",")
                step_three = "".join(step_two)
                old_price_final = int(step_three)
                old_p.append(old_price_final)
            else:
                step_one = old_price_raw.lstrip("₦ ")
                old_price_final = int(step_one)
                old_p.append(old_price_final)
            # print(old_price_final)
        except:
            old_price_final = None
            # old_p.append(old_price_final)
            pass

        # New price
        try:
            new_price_details = phone_soup.find("div", attrs={"class": "prc"})
            new_price_raw = new_price_details.text
            if "," in new_price_raw:
                step_one = new_price_raw.lstrip("₦ ")
                step_two = step_one.split(",")
                step_three = "".join(step_two)
                new_price_final = int(step_three)
                new_p.append(new_price_final)
            else:
                step_one = new_price_raw.lstrip("₦ ")
                new_price_final = int(step_one)
                new_p.append(new_price_final)
            # print(new_price_final)
        except:
            new_price_final = None
            # new_p.append(new_price_final)
            pass

        # ratings
        try:
            rating_details = phone_soup.find("div", attrs={"class": "stars _s"})
            ratings_raw = rating_details.text
            trans_one = ratings_raw.split(" ")
            trans_two = trans_one[0]
            rating_final = float(trans_two)
            rate.append(rating_final)
            # print(rate)
        except:
            rating_final = None
            # rate.append(rating_final)
            pass

 
#Writing all files to CSV
import xlwt
from tempfile import TemporaryFile

#Getting the book

book = xlwt.Workbook()

#adding the sheets to the book/excel 
sheet_one = book.add_sheet("SmartPhones")

# Writing the first sheet
# writing the headers
sheet_one.write(0, 0, "Phone Brand")
sheet_one.write(0, 1, "Specifications")
sheet_one.write(0, 2, "Old Price")
sheet_one.write(0, 3, "New Price")
sheet_one.write(0, 4, "Ratings")

# writing the rest of the data
for index, brand in enumerate(phone_b):
    sheet_one.write(index + 1, 0, brand)

for index, spec in enumerate(phone_s):
    sheet_one.write(index + 1, 1, spec)

for index, oldp in enumerate(old_p):
    sheet_one.write(index + 1, 2, oldp)

for index, newp in enumerate(new_p):
    sheet_one.write(index + 1, 3, newp)

for index, rating in enumerate(rate):
    sheet_one.write(index + 1, 4, rating)


# Specify filename and path
book_name = "C:/Users/HP/OneDrive/Documents/Data_Science/Jumia_phones.xls"

# saving the file
book.save(book_name)
book.save(TemporaryFile())


print("All done")



    # print(phone_brand)
    # print(phone_spec)
    # print(old_price_final)
    # print(new_price_final)
    # print(rating_final)