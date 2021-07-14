import requests
from bs4 import BeautifulSoup

with requests.Session() as s:
    r = s.get("https://news.v.daum.net/v/20210713112417105")
    # print(r.text)

    # 도착한 내용을 파싱
    # ① BeautifulSoup 객체 생성
    soup = BeautifulSoup(r.text,"html.parser")
    # print(soup)
    # print(soup.head) # head 태그 가져오기
    print()
    # print(soup.body) # body 태그 가져오기
    print("title:{}".format(soup.title))
    print("title:{}".format(soup.title.name))
    print("title:{}".format(soup.title.string)) #태그 문자열 안의 문자를 가져올 수 있음
    print("title:{}".format(soup.title.get_text())) #태그 문자열 안의 문자를 가져올 수 있음