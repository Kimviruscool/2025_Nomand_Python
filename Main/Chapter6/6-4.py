#main.py

#console 사용해서 python 사용
# 콘솔 cmd 사용후
#cd C:\Users\0000\Desktop\2025_Nomand_Python\Main\Chapter6 파일로이동
#python 6-4.py (프로그래밍언어 이름.py) 하면 내부에 저장된 코드 실행됨

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

#time 모듈 시간 추가
p = sync_playwright().start()
print("P success")


browser = p.chromium.launch(headless=False) #p.chromiun#크롬으로 .launch()#초기화

page = browser.new_page() # 새로운 브라우저 생성

page.goto("https://www.wanted.co.kr/") # .goto("주소") 페이지 주소 열기

time.sleep(5) #.sleep(초)

page.click("button.Aside_searchButton__Ib5Dn.Aside_isNotMobileDevice__ko_mZ") #검색버튼 .button.css(class명)

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter") #검색에 검색어 추가

time.sleep(5)

page.keyboard.down("Enter") #키보드 누르기 enter기능

time.sleep(5)

page.click("a#search_tab_position")

time.sleep(5)

for i in range(4) :
    page.keyboard.down("End")
    time.sleep(5)

time.sleep(5)

content = page.content()

p.stop() #멈추기

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

jobs_db=[]

for job in jobs:
    link = job.find("a")["href"]
    title = job.find("strong" , class_="JobCard_title___kfvj").text
    company_name1 = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu")
    company_name = company_name1.text if company_name1 else "None Company name"
    job = {
        "title":title,
        "company_name" : company_name,
        "link" : link
    }
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))

# page.screenshot(path="screenshot.png") #png타입으로 저장 page를 찍어옴

#headless mode 컴퓨터에서 브라우저를 호출만 하는것 #headless=True를 하면 코드내에서 진행 False 로하면 브라우저를 직접 키고 이후 스크린샷을찍은후에 자동종료
