import requests #requests: Lets you send HTTP requests (like a browser requesting a web page).
from bs4 import BeautifulSoup #`BeautifulSoup: Lets you parse and search the HTML structure easily.
import time

print("Put some skills that you want to filter out:")
familiar_skills = input('> ')
print(f"filtering your search based on {familiar_skills}......")

def find_jobs():
    url= "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation="
    response = requests.get(url).text # Send a GET request to the specified URL.

    soup = BeautifulSoup(response,'lxml')

    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        posting = job.find('span',class_='sim-posted').span.text
        if 'today' in posting :
            company_name =job.find('h3',class_='joblist-comp-name').text
            skills = job.find('div',class_='more-skills-sections').text
            more_info = job.header.h2.a['href']

            if familiar_skills.lower() in skills.lower():
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"company name: {company_name.strip()} \n")
                    f.write(f"More info: {more_info.strip()} \n")
                    f.write(f"skills required: {skills.strip()} \n")
                print(f"file saved: {index}")

if __name__ == "__main__":#Only run the code inside this block if this file is being run directly (not imported as a module)
    while True:
        find_jobs()
        time_wait = 10
        print(f"wait for {time_wait} minutes.....")
        time.sleep(time_wait * 60)#seconds