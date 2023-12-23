from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
for i in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={i}&filter=", headers=headers)
    if response.ok:


        content = response.text
        soup = BeautifulSoup(content,'html.parser')
        all_title = soup.findAll("span", attrs={"class": "title"})
        for title in all_title:
            title_string = title.string
            if "/" not in title_string:
                print(title.string)

    else:
        print("请求失败")