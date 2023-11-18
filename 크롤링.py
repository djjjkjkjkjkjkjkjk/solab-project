from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 셀레니움 웹 드라이버 설정
driver = webdriver.Chrome('chromedriver.exe')  # 스크립트 파일과 같은 디렉토리에 있을 경우


# 네이버 쇼핑 페이지 열기
driver.get('https://shopping.naver.com/')

# 상품 검색어 입력
search_box = driver.find_element_by_css_selector('#autocompleteWrapper input[type="search"]')
search_term = "검색할 상품명"
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

# 검색 결과에서 상품 정보 추출
products = driver.find_elements_by_css_selector('ul[class*="search_list"] li')

for product in products:
    product_name = product.find_element_by_css_selector('a[class*="basicList_link"]').text
    price = product.find_element_by_css_selector('span[class*="price_num"]').text
    review_count = product.find_element_by_css_selector('a[class*="basicList_etc"]').text

    print("상품명:", product_name)
    print("가격:", price)
    print("리뷰 수:", review_count)
    print("-----------------------")

# 셀레니움 종료
driver.quit()
