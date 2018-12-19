import bs4
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

my_url = 'https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10'
#opening up connection, grabbing the page 
uClient = uReq(my_url)
#stores content to a variable
page_html = uClient.read()
#closes connection
uClient.close()

#creating  soup 
page_soup = soup(page_html, "html.parser")
#grabs jobTitles

containers =  page_soup.findAll('div',{'class':'row'})

filename = "indeedlist.csv"
f = open(filename, "w")
headers = "job_title, company, location, days_ago\n"

f.write(headers)

for a  in containers: 
   job_title = a.find('h2').text
   company = a.find('span').text
   location = a.find('span', {'class':'location'}).text
   days_ago = a.find('span', {'class':'date'}).text

   print("job_title: " + job_title)
   print("company: " + company)
   print("location: " + location)
   print("days_ago: " + days_ago)
   
f.write(job_title.replace("," , "|") + ',' + company.replace(",", "|") + ','  + location.replace(",", "|") + ',' + days_ago.replace(",", "|") + '\n')

f.close()



