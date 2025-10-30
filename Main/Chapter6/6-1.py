#Web Scraper
# beautifulsoup4 , request 사용

import requests
from bs4 import BeautifulSoup

# 스크래핑 할 주소 입력후 url 변수에 저장
url = "https://weworkremotely.com/"

#변수에 저장된 값 requests를 통해 가져온후 response에 저장
response = requests.get(url)

# response.status_code
# response.content

#Beautifulsoup을 통해 스크래핑한 코드 1차 가공
soup = BeautifulSoup(response.content, "html.parser")
# soup 변수에 BeautifulSoup을이용(사용할데이터, "데이터의 형태(ex : html,js등)")
# soup는 Html만으로 동작되는게 아니라 다른 format으로도 사용가능

#print(response.content) # response(주소의)의 content(정보,html코드)획득

#Beautifulsoup 많은 html코드를 가져가서 내부에서 검색을 가능하게 해주는 패키지사용
#Beautifulsoup은 Class

#notation [1:-1] 리스트 구조에서 [시작점 : 끝점]
#[0 ~ * : -1,0 ~ * ] 사용가능

jobs = soup.find("section", class_="jobs").find_all("li",class_="new-listing-container feature")
#html안에 원하는 데이터를 class_에 저장 그안에 존재하는 li의 모든 정보를 스크래핑 + class이름이 "new-listing-container feature" 가 포함된 list만
# print(jobs)

all_jobs = []

for job in jobs :
    title = job.find("h3", class_="new-listing__header__title").text
    region = job.find("p", class_="new-listing__company-headquarters").text
    companies = job.find("p", class_="new-listing__company-name").text
    # print(title,region,companies,"------\n")
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
    #next_sibling 한단계 패스
    job_data = {"title":title,"region":region,"companies":companies,"url":url}
    all_jobs.append(job_data)

print(all_jobs,"\n")

# 다른 버전
# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.content, "html.parser")
#
# jobs = soup.find("section", class_="jobs").find_all("li")[:-1]
#
# for job in jobs:
# title_tag = job.find("h4", class_="new-listing__header__title")
# company_tag = job.find("p", class_="new-listing__company-name")
# region_tags = job.find_all("p", class_="new-listing__categories__category")
#
# # None 체크 추가
# title = title_tag.text.strip() if title_tag else "N/A"
# company = company_tag.text.strip() if company_tag else "N/A"
# region = region_tags[-1].text.strip() if region_tags else "지역 정보 없음"
#
# print(f"{title} at {company} in {region}\n")