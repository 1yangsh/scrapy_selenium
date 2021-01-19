from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\Users\\Seunghyeon Yang\\Downloads\\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(path)


# selenium을 이용한 구글 검색 테스트
'''
driver.get("https://www.google.com")
search_box = driver.find_element_by_name("q")  # 검색창의 name이 q
search_box.send_keys("아마존 웹 서비스")       # q에 cloud computing의 키를 넘김
search_box.submit()                            # 엔터키와 동일한 작업
'''


# facebook login
'''
driver.get("https://www.facebook.com")
print(driver.title)

elem_email = driver.find_element_by_id("email")
elem_email.send_keys("[페이스북 아이디]")
elem_pass = driver.find_element_by_id("pass")
elem_pass.send_keys("[페이스북 패스워드]")

elem_pass.send_keys(Keys.RETURN)
'''


# github login
'''
driver.get("https://www.github.com/login")
print(driver.title)

elem_email = driver.find_element_by_id("login_field")
elem_email.send_keys("[github id]")
elem_pass = driver.find_element_by_id("password")
elem_pass.send_keys("[github password]")

elem_pass.send_keys(Keys.RETURN)
'''


# facebook 자기 프로필, 친구목록 확인
driver.get("https://www.facebook.com")
print(driver.title)

elem_email = driver.find_element_by_id("email")
elem_email.send_keys("[id]")
elem_pass = driver.find_element_by_id("pass")
elem_pass.send_keys("[password]")
elem_pass.send_keys(Keys.RETURN)

# 프로필
profile_a = driver.find_element_by_xpath(
    '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')
print("Profile A => ", profile_a.get_attribute('href'))

# 친구목록
friends_a = driver.find_element_by_xpath(
    '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a')
print("Friends A => ", friends_a.get_attribute('href'))

# driver.get(profile_a.get_attribute('href'))   # 프로필 링크
driver.get(friends_a.get_attribute('href'))     # 친구목록 링크
