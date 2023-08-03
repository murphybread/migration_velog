import requests
import json
from bs4 import BeautifulSoup


# 해당 URL에 GET 요청을 보냅니다.
url = (
    "https://velog.io/@mcbible/%EB%A6%AC%EB%88%85%EC%8A%A4-%EB%AA%85%EB%A0%B9%EC%96%B4"
)
response = requests.get(url)

# 응답을 받고 HTML을 파싱합니다.
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

# 원하는 정보의 위치와 태그를 확인하여 추출합니다.
# 예를 들어, 게시물의 본문 내용을 가져오고 싶다면, 해당 태그와 클래스를 확인해야 합니다.

content = soup.find("div", class_="atom-one")
print(content.text)


# 원하는 정보의 위치와 태그를 확인하여 추출합니다.
# 예를 들어, 각 포스트의 제목을 가져오고 싶다면, 해당 태그와 클래스를 확인해야 합니다.
# titles = soup.find_all("h3", class_="post-title")

# for title in titles:
#     print(title.text)
