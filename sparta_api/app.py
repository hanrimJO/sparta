from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.naver

app = Flask(__name__)  # , static_folder='static2') 괄호안 name 다음에 넣는다, __name__ 은 파일 이름인 app.py를 의미한다.


@app.route('/')  # url route를 말한다. ex) naver.com/news 슬래시 뒷부
def home():
    return render_template('index.html')


@app.route('/mypage')
def mypage():
    return 'this is mypage'


# ajax와 통신할 API POST method
# @app.route('/test', methods=['POST'])
# def test_post():
#     title_receive = request.form['title_give']  # 바디에 있는 정보를 받아올때 form을 사용
#     print(title_receive)
#     return jsonify(
#         {
#             'result': 'success',
#             'msg': '이 요청은 POST!'
#         }
#     )

@app.route('/test', methods=['POST'])
def test_post():
    rank_receive = request.form['rank_give']
    if rank_receive is not None:  # 예외처리
        rank_receive = int(rank_receive)
    else:
        rank_receive = 0

    star_receive = request.form['star_give']
    star_receive = float(star_receive)

    db.movies.update_one(
        {'rank': rank_receive},
        {'$set': {'star': star_receive}}
    )

    return jsonify(
        {
            'result': 'success'
        }
    )


@app.route('/new', methods=['POST'])
def new_movies():
    rank_receive = request.form['rank_give']
    title_receive = request.form['title_give']
    star_receive = request.form['star_give']

    rank_receive = int(rank_receive)
    star_receive = float(star_receive)

    print(rank_receive, title_receive, star_receive)

    db.movies.insert_one({'rank': rank_receive, 'title': title_receive, 'star': star_receive})

    return jsonify(
        {
            'result': 'success'
        }
    )




# ajax 와 통신할 API GET methods
# @app.route('/test', methods=['GET'])
# def test_get():
#     title_receive = request.args.get('title_give')  # url에서 가져올때 args.get을 사용한다.
#     print(title_receive)
#     gender = request.args.get('gender')
#     print(gender)
#     return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['GET'])
def test_get():
    rank_receive = request.args.get('rank_give')  # url에서 가져올때 args.get을 사용한다.
    rank_receive = int(rank_receive)
    movie_info = db.movies.find_one({'rank': rank_receive}, {'_id': 0})
    return jsonify(
        {
            'result': 'success',
            'info': movie_info
        }
    )


if __name__ == '__main__':  # 파이썬이 app.py를 실행 시킬
    app.run('0.0.0.0', port=5000, debug=True)
