import requests #pip3 install requests
from bs4 import BeautifulSoup #pip3 install bs4

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser") #makes sure that you use the appropriate parser for HTML content

results = soup.find(id="ResultsContainer") #contains all job elements / cards
job_elements = results.find_all("div", class_="card-content") #all div_card-content in ResultsContainer


for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    for link in job_element.find_all("a", class_="card-footer-item", href=True):
        if link.text.strip() == "Apply":
            print(link['href'])

    print()

