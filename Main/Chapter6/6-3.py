# https://remoteok.com/ 해당 페이지에가서 flutter, python, golang의
# 검색후 일치하는 일자리를 스크래핑
# 가능한 사람은 class 형태로 변경하기 객체지향형 코드로 변경해서만들기

import requests
from bs4 import BeautifulSoup

keyword = ["flutter","python","golang"]

r = requests.get("https://remoteok.com/?search=flutter")
print(r)
print(r.status_code)
print(r.content)