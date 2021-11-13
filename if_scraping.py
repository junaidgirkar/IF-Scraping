import requests, random, time
from bs4 import BeautifulSoup
import csv
all_companies = []

BASE_URL = "https://internshala.com/internships/work-from-home-electrical,electronics,embedded%20systems,engineering,event%20management,flutter%20development,front%20end%20development,full%20stack%20development,game%20development,graphic%20design,image%20processing,information%20technology,internet%20of%20things%20(iot),ios,java,javascript%20development,machine%20learning,marketing,mechanical,mechatronics,mobile%20app%20development-jobs-in-mumbai/stipend-6000"
page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'html.parser')
 
pages = int(soup.find(id="total_pages").text) # Find the total number of pages

for i in range(1, pages+1): # Looping through each page
    
    URL = BASE_URL + "/page-" + str(i)
 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    companies = soup.find_all(class_="company") # Finding the div tag with company
    stipends = soup.find_all(class_="stipend")  # Finding the div tag with stipend
    stipends_list = [stipend.text for stipend in stipends]  # Creating a list of stipends to save later

    i = 0   # Iterator for stipend_list
    for company in (companies): #Looping through the companies
        company_name = str(company.find(class_="heading_6 company_name").text)[26:-21]
        individual_stipend = stipends_list[i] #Getting the specific company's stipend
        i+=1  #Increment iterator
   

        
        print(company_name)
 
        job_profile = str(company.find(class_="heading_4_5 profile").text)[1:-1]
 
        all_companies.append([
            company_name,
            job_profile,
            individual_stipend
        ])  # Creating a list with all required details
    
    time.sleep(random.random());  # As the website is probablt throttled

# Saving data in csv format 
with open('ifcompanies_draft.csv', mode='a') as companies:
    company_writer = csv.writer(companies, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    header = ['Company Name',"Job Profile", "Stipend"]
    company_writer.writerow(header)
    for item in all_companies:
        company_writer.writerow(item)