from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    # 예외처리 구문
    try:
        url_receive = request.form['url_give']
        comment_receive = request.form['comment_give']

        # url 스크래핑 html  meta 태그 파싱 og 태그 파싱 > mongodb에 저장 comment title desc image url 까지 저장
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        url_image = og_image['content']
        url_title = og_title['content']
        url_description = og_description['content']

        # print(og_image, og_title, og_description)

        article = {
            'title': url_title,
            'desc': url_description,
            'image': url_image,
            'url': url_receive,
            'comment': comment_receive
        }

        db.articles.insert_one(article)


    except Exception as e:
        print(e)
        return jsonify({"result": "fail"})

    return jsonify({"result": "success"})


@app.route('/post', methods=['GET'])
def list_articles():
    try:
        article_info = list(db.articles.find({}, {'_id': 0}))
    except Exception as e:
        print(e)
        return jsonify({
            'articles': [],
            'result': 'fail'
        })
    return jsonify({
        'result': 'success',
        'articles': article_info
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)  # 0.0.0.0은 모든 로컬 아이피 주소
