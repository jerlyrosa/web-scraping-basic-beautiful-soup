from bs4 import  BeautifulSoup
import requests


website ='https://realpython.github.io/fake-jobs/'


page = requests.get(website)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

jobs =[]

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    date_element = job_element.find("p", class_="is-small")

    jobs.append(f"\n{title_element.text.strip()},{date_element.text.strip()}")


str = ''.join(jobs)

with open(f'fake-jobs/jobs.csv', 'w') as file:
    file.write(str)
