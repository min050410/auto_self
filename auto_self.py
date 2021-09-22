from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
import pyautogui

# 크롬 드라이버 exe 파일의 위치를 입력
chromedriver = 'chromedriver.exe'


# 옵션 변경
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chromedriver, options=options)

# 변수설정
url = 'https://google.com'
sido = input("학교의 시 또는 도 입력 :")
schoolname = input("학교 이름을 입력하세요 :")
name = input("이름을 입력하세요 :")
birth = input("주민등록번호 앞자리를 입력하세요 :")
password = input("자가진단 비밀번호 입력: ")
level = schoolname[-4:]

# 중학교, 유치원, 특수학교 등
if(level[1] == "중" or level[3] == "중"):
    level = '중학교'
elif(level[1] == "유" or level == "어린이집"):
    level = '유치원'
elif(level[3] == "고"):
    level = '고등학교'
elif(level[3] == "초"):
    level = '초등학교'

# 시도, 학교 레벨 인덱스
sido_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
             '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
level_list = ['유치원', '초등학교', '중학교', '고등학교']
index_sido = str(sido_list.index(sido)+2)
index_level = str(level_list.index(level)+2)
# 시작
driver.get(url)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('자가진단')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()
driver.find_element_by_id("btnConfirm2").click()
driver.find_element_by_id("schul_name_input").click()

# 학교 검색 ( 부산광역시 고등학교 기준 )
# 시 도 검색
driver.find_element_by_id("sidolabel").click()
driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select/option["+index_sido+"]").click()
driver.find_element_by_id("crseScCode").click()
driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td/select/option["+index_level+"]").click()
driver.find_element_by_id("orgname").send_keys(schoolname)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
driver.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').send_keys(Keys.TAB, Keys.ENTER)

t.sleep(2)
driver.find_element_by_css_selector('.layerFullBtn').click()

# 개인정보 입력
driver.find_element_by_css_selector('#user_name_input').send_keys(name)
driver.find_element_by_css_selector('#birthday_input').send_keys(birth)
driver.find_element_by_css_selector('#btnConfirm').send_keys(Keys.ENTER)
t.sleep(5)
# 비밀번호

driver.find_element_by_xpath(
    "/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr/td/input[1]").click()
t.sleep(2)

list_password = list(password)
imgprefix = 'password/password_'
imgsuffix = '.PNG'
for i in list_password:
    if(i != '\0'):
        text = pyautogui.locateOnScreen(imgprefix+i+imgsuffix, confidence=0.9)
    center = pyautogui.center(text)
    pyautogui.click(center)
    # t.sleep(1)

# 확인버튼
driver.find_element_by_xpath(
    "/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/input").click()

t.sleep(2)
driver.find_element_by_css_selector(
    '.service01').send_keys(Keys.TAB * 3, Keys.ENTER)
t.sleep(2)
driver.find_element_by_id("survey_q1a1").click()
driver.find_element_by_id("survey_q2a1").click()
driver.find_element_by_id("survey_q3a1").click()
driver.find_element_by_id("btnConfirm").click()
# 끝
