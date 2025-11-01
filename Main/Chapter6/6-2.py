#pagination scraping
import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url) :

    print(f"Scraping {url}...")

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs").find_all("li", class_="new-listing-container feature")

    for job in jobs:
        title = job.find("h3", class_="new-listing__header__title").text

        region_tag = job.find("p", class_="new-listing__company-headquarters")
        region = region_tag.text if region_tag else "NoneType"

        companies = job.find("p", class_="new-listing__company-name").text
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        job_data = {"title": title, "region": region, "companies": companies, "url": url}
        all_jobs.append(job_data)

def get_page(url):
    pass

def get_pages(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
    # len() 함수를 사용하여 몇개있는지 확인
    # print(buttons)
    return buttons

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages) :
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    # print(url)
    scrape_page(url)

print(len(all_jobs))