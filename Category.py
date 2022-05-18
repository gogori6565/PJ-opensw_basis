## 과제/공지사항/성적/강의자료 카테고리 분류하기 - 속성값 이용##

#현재 3.14.1 selenium 버전 사용중
from selenium import webdriver
#타임 객체 선언
from time import sleep
import requests
from bs4 import BeautifulSoup as bs

##전역변수 선언##
login_stop=1 #로그인 예외처리 변수
category_index=0 #속성값 추출할 때 사용할 category의 index

#크롬 웹 드라이버 경로
driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')

#로그인 실패 예외처리 - 실패시 다시 로그인 / 성공시 넘어감
while(login_stop):
    try:
        #크롬으로 블랙보드 로그인 화면 접속
        url = "https://ecampus.chungbuk.ac.kr/"
        driver.get(url)

        #아이디와 비밀번호 입력(0.5초씩 기다리기) - 너무 빠르면 대형 사이트는 트래픽 공격으로 인식
        print('user_id : ')
        user_id = input()
        sleep(0.5)
        driver.find_element_by_name('uid').send_keys(user_id)

        print('user_pw : ')
        user_pw = input()
        sleep(0.5)
        driver.find_element_by_name('pswd').send_keys(user_pw)

        #Xpath
        driver.find_element_by_xpath('//*[@id="entry-login"]').click()

        #사이트 이동
        driver.get('https://ecampus.chungbuk.ac.kr/ultra/stream')

        #while반복 멈추기
        login_stop=0
    except:
        pass

#활동스트림 내용 담은 element 가져오기
sleep(8)
response=driver.find_element_by_xpath('//*[@id="body-content"]').get_attribute('innerHTML')

soup = bs(response, 'html.parser')

##제공예정##
upc_cours=soup.select('.js-upcomingStreamEntries.activity-group.columns.main-column>ul.activity-feed>li>div>div>div>div>div>a')
upc_title=soup.select('.js-upcomingStreamEntries.activity-group.columns.main-column>ul.activity-feed>li>div>div>div>div>div.name>ng-switch>a')

##오늘##
td_cours=soup.select('.js-todayStreamEntries.activity-group.columns.main-column>ul.activity-feed>li>div>div>div>div>div>a')
td_title=soup.select('.js-todayStreamEntries.activity-group.columns.main-column>ul.activity-feed>li>div>div>div>div>div.name>ng-switch>a')

##최근항목##
pre_cours=soup.select('.js-previousStreamEntries.activity-group.columns.main-column>ul.activity-feed>li>div>div>div>div>div>a')
pre_title=soup.select('.js-previousStreamEntries.activity-group.columns.main-column>ul.activity-feed>li>div>div>div>div>div.name>ng-switch>a')

##카테고리 구분##
category=soup.select('svg[class="MuiSvgIconroot-0-2-37 makeStylesdirectionalIcon-0-2-36 makeStylesstrokeIcon-0-2-35 MuiSvgIconcolorPrimary-0-2-38 MuiSvgIconfontSizeLarge-0-2-45"]')

#aria-label의 속성값만 추출
for icon in category:
    category[category_index]=icon['aria-label']
    category_index+=1

print('<제공예정>')
for i in range(0,len(upc_cours)):
    print(category[i])
print('\n<오늘>')
for i in range(len(upc_cours),len(upc_cours)+len(td_cours)):
    print(category[i])
print('\n<최근항목>')
for i in range(len(upc_cours)+len(td_cours),len(upc_cours)+len(td_cours)+10):
    print(category[i])
