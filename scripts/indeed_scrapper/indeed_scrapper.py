'''
Scrapper to scrap JOBS data from INDEED .com
'''
import urllib.request
from bs4 import BeautifulSoup
import time

file = open('indeed_jobs_data.csv', 'w', encoding="utf-8")
file.write('Company, Position, Salary, Location, JOB_LINK, Description\n')
MAX_RESULTS = 100000
START_FROM = 0
KEYWORD =  "cloud"
for start in range(START_FROM, MAX_RESULTS, 10):
    print(start)
    URL = f"https://www.indeed.com/jobs?q={KEYWORD}&start={start}"
    soup = BeautifulSoup(urllib.request.urlopen(URL).read(), 'html.parser')
    time.sleep(2)  #ensuring at least 1 second between page grabs
    results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})
    for x in results:
        company = x.find('span', attrs={"class":"company"})
        if company:
            company = company.text.strip()
            # replace commas with hyphen
            company = company.replace(',', '-')

        location = x.find('span', attrs={"class":"location"})
        if location:
            location = location.text.strip()
            # replace commas with hyphen
            location = location.replace(',', '-')
            

        position = x.find('a', attrs={'data-tn-element': "jobTitle"})
        if position:
            position = position.text.strip()
            # replace commas with hyphen
            position = position.replace(',', '-')
            

        JOB_LINK = x.find('a', attrs={'data-tn-element': "jobTitle"})
        if JOB_LINK:
            JOB_LINK = JOB_LINK['href']
            # replace commas with hyphen
            JOB_LINK = JOB_LINK.replace(',', '')
            JOB_LINK = "https://www.indeed.com" + JOB_LINK
            

        salary = x.find('span', attrs={"class", "salaryText"})
        if salary:
            salary = salary.text.strip()
            salary = salary.replace(',', '')
            
        else:
            salary = "No Salary Info" 
                   

        summary = x.find('div', attrs={"class", "summary"})
        if summary:
            summary = summary.text.strip()
            summary = summary.replace(',', '').replace('\n', '. ')
            
        else:
            summary = "No description"
            print("No description")
        if position:
            file.write(company + ', ' + position + ', ' + salary + ', ' + location + ', ' + JOB_LINK + ', ' + summary +'\n')
    print ('----------')
file.close()