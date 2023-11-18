import requests
from bs4 import BeautifulSoup

# 웹 페이지에 접속하여 HTML 소스코드 가져오기
url = "https://example.com"  # 크롤링할 웹 페이지의 URL을 입력해주세요
response = requests.get(url)
html_content = response.text

# BeautifulSoup를 사용하여 데이터 추출
soup = BeautifulSoup(html_content, 'html.parser')

# 제목 추출
title = soup.find('h1').text

# 내용 추출
content = soup.find('div', class_='content').text

# 결과 출력
print("제목:", title)
print("내용:", content)