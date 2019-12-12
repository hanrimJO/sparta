from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import datetime

# mongo db
client = MongoClient('localhost', 27017)
db = client.genie

# today = str(datetime.date.today()).replace('-', '')
# print(today)

date = input('크롤링 하고싶은 날짜는?, ex) 20191210 ')


def genie(today):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+today, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # print(soup)

    songs = soup.select('table.list-wrap > tbody > tr')

    # recursive = 재귀, 하부태그로 들어가지 않는다.
    for song in songs:
        rank = song.select_one('td.number').find(text=True, recursive=False).strip()
        title = song.select_one('td.info > .title').text.lstrip()
        artist = song.select_one('td.info > .artist').text.lstrip()
        print(rank, title, artist)

        # doc = {
        #     'rank': int(rank),
        #     'title': title,
        #     'artist': artist
        # }
        #
        # db.chart.insert_one(doc)


genie(date)

