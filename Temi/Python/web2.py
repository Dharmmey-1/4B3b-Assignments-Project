import requests 
from bs4 import BeautifulSoup

# headers = requests.utils.default_headers()  #TO TRICK THE SITE WITH THE GOAL THAT IS IT IS  FROM GOOGLE CHROME BROWSER


# headers.update({"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"})

#DEFINE AN URL(THE WEBSITE WE WANT TO SCRAPE)
url = "https://www.jumia.com.ng/smartphones/?page={pages}#catalog-listing"


list_phone_brand = []
list_phone_spec = []
list_old_price = []
list_new_price = []
list_rating = []


for page in range(1, 51):   

    headers = requests.utils.default_headers()  #TO TRICK THE SITE WITH THE GOAL THAT IS IT IS  FROM GOOGLE CHROME BROWSER


    headers.update({"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"})

    my_response = requests.get(url, headers)

    #CREATING A VARIABLE
    sweet_soup = BeautifulSoup(my_response.content, features = "lxml")


    further_search = sweet_soup.find_all("article", attrs = {"class": "prd _fb col c-prd"})


    for phone_soup in further_search:
        phone_detail = phone_soup.find("a") #the a tag doesn't have classes
        # FOR PHONE BRAND
        try:
            phone_brand = phone_detail["data-brand"]
            list_phone_brand.append(phone_brand)
            
            
        except:
            phone_brand = None
            list_phone_brand.append(phone_brand)
        # phone_brand = phone_deatil["data-brand"]  #to get the samsung


        # FOR PHONE SPEC
        try:
            phone_spec = phone_detail["data-name"]
            list_phone_spec.append(phone_spec)
        except:
            phone_spec = None
            list_phone_spec.append(phone_spec)

        #FOR OLD PRICE
        #to  extract the ₦ and make it a int in old

        try:
            old_price_detail = phone_soup.find("div", attrs = {"class": "old"})
            old_price_raw = old_price_detail.text
            # print(old_price_raw)


            if "," in old_price_raw:
                step_one = old_price_raw.lstrip("₦ ")
                step_two = step_one.split(",")
                step_three = "".join(step_two)
                old_price_final= int(step_three)
                list_old_price.append(old_price_final)
        
            else:
                step_one = old_price_raw.lstrip("₦ ")
                old_price_final = int(step_one)
                list_old_price.append(old_price_final)
        except:
            old_price_final = None
            list_old_price.append(old_price_final)

        ## FOR NEW PRICE DETAIL
        #to  extract the ₦ and make it a int in price
        try:

            new_price_details = phone_soup.find("div", attrs = {"class": "prc"})
            new_price_raw = new_price_details.text
            if "," in new_price_raw:
                step_one = new_price_raw.lstrip("₦ ")
                step_two = step_one.split(",")
                step_three = "".join(step_two)
                new_price_final = int(step_three)
                list_new_price.append(new_price_final)
    
        

            else: 
                step_one = new_price_raw.lstrip("₦ ")
                new_price_final = int(step_one)
                list_new_price.append(new_price_final)

                # print(new_price_final)
        except:
            new_price_final = None
            list_new_price.append(new_price_final)

        
        #TO COLLECT THE DATA REVEIW DATA
        # To make the 4.3 a float
        try:

            rating_details =  phone_soup.find("div", attrs ={"class" : "stars _s"})
            ratings_raw = rating_details.text
            trans_one = ratings_raw.split(" ")
            trans_two = trans_one[0]
            rating_final = float(trans_two)
            list_rating.append(rating_final)
            

            # print(rating_final)
        except:
            rating_final = None
            list_rating.append(rating_final)
            

  

# print(list_phone_brand[-10:])






        # print(phone_brand)
        # print(phone_spec)
        # print(old_price_final)
        # print(new_price_final)
        # print(rating_final)





#To wite it to csv.
import csv


with open(r"/Users/mac/Documents/python-datascience/my-work/4B3b-Assignments-Project/Temi/FILES/Web1.csv", mode="w", newline="", encoding="utf-8") as f:
    pen = csv.writer(f)
    pen.writerow(["Phone Brand", "Phone Spec", "Old Price", "New Price", "Rating"])
    for num in range(len(list_phone_spec)):
        pen.writerow([list_phone_brand[num], list_phone_spec[num], list_old_price[num], list_new_price[num], list_rating[num]])