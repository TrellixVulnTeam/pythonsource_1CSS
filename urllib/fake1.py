import urllib.request as request
from urllib.error import URLError
from fake_useragent import UserAgent

# url = "https://news.v.daum.net/v/20210712090550628"
url="https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=104&oid=011&aid=0003935183"
try :
    # 객체 생성
    userAgent=UserAgent()

    #header 생성
    headers ={
        'User-agent':userAgent.chrome
    }

    # host명과 User-agent 확인
    request_url=request.Request(url,headers=headers)
    response=request.urlopen(request_url).read().decode("utf-8")
except URLError as e:
    print(e)
else:
    print(response[:2000])
    print(request_url.header_items())
