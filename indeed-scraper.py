import bs4
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

my_url = 'https://www.indeed.com/jobs?as_and=IT+Manager&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=Camarillo%2C+CA&fromage=any&limit=50&sort=&psf=advsrch'
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
    print(a.find('h2').text)

for a  in containers: 
    print(a.find('span').text)

for a  in containers:
	print(a.find('span', {'class':'location'}).text)

for a in containers:
	print(a.find('span', {'class':'date'}).text)


# f.write(job_title.replace("," , "|") + ',' + company.replace(",", "|") + ','  + location.replace(",", "|") + ',' + days_ago.replace(",", "|") + '\n')

f.close()



