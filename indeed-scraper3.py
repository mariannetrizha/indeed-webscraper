import bs4
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

my_url = 'https://www.indeed.com/jobs?q=IT+Manager&l=Camarillo%2C+CA&radius=25'
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

for container in containers: 
    a =	container.find('a',{'class':'turnstileLink'})
    print(a)

    print(.find('h2').text)

HOW TO PRINT JOB_TITLE


# f.write(job_title.replace("," , "|") + ',' + company.replace(",", "|") + ','  + location.replace(",", "|") + ',' + days_ago.replace(",", "|") + '\n')

f.close()



