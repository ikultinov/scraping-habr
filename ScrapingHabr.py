import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    "Cookie": "_ym_uid=1628700934741435443; hl=ru; _ga=GA1.2.1601255211.1647950829; fl=ru; _ym_d=1665734570; habr_web_home_feed=/all/; _ym_isad=1; _gid=GA1.2.1756392303.1665844740",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
    "If-None-Match": "W/'37433-+qZyNZhUgblOQJv5vdmtE4BN6w'",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "sec-ch-ua-mobile": "?0"}

base_url = "https://habr.com"
url = base_url + "/ru/all/"

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
    date = article.find("time").attrs["title"]
    title = article.find(class_="tm-article-snippet__title-link").find("span")
    preview = article.find(class_="tm-article-snippet")
    preview_lower = preview.text.lower()
    for word in KEYWORDS:
        if word in preview_lower:
            print(f'<{date}> - <{title.text}> - <{base_url + href}>.')
