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


# 원하는 정보의 위치와 태그를 확인하여 추출합니다.
# 예를 들어, 게시물의 본문 내용을 가져오고 싶다면, 해당 태그와 위치를 확인해야 합니다.
divs = soup.find_all("div")
for i in range(10):
    content = divs[i]  # 인덱스는 실제 웹 페이지의 구조에 따라 달라질 수 있습니다.
    print(content.text)
    print("----------------------------------------")

# 원하는 정보의 위치와 태그를 확인하여 추출합니다.
# 예를 들어, 게시물의 본문 내용을 가져오고 싶다면, 해당 태그와 클래스를 확인해야 합니다.

content = soup.find("div", class_="atom-one")
print(content.text)

# HTML 내용에서 script 태그를 찾습니다.
scripts = soup.find_all("script")

# script 태그 중에서 원하는 정보가 포함된 태그를 찾습니다.
for script in scripts:
    if script.string and "window.__PRELOADED_STATE__" in script.string:
        # JSON 문자열을 추출합니다.
        json_str = script.string.split(" = ")[1].strip().rstrip(";")
        # JSON 문자열을 파싱하여 Python 딕셔너리로 변환합니다.
        data = json.loads(json_str)
        # 원하는 정보를 추출합니다.
        posts = data["velog"]["posts"]
        for post in posts.values():
            print("Title:", post["title"])
            print("Description:", post["short_description"])
            print()


# 원하는 정보의 위치와 태그를 확인하여 추출합니다.
# 예를 들어, 각 포스트의 제목을 가져오고 싶다면, 해당 태그와 클래스를 확인해야 합니다.
titles = soup.find_all("h3", class_="post-title")

for title in titles:
    print(title.text)
