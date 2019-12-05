from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.naver

# sound = db.movies.find_one({'title': '사운드 오브 뮤직'}, {'_id': 0})

# print(sound['star'])

# 리스트화가 필요하다
# movies = list(db.movies.find({'star': sound['star']}))

# print(movies)
#
# for i in movies:
# db.movies.update_many(i, {'$set': {'star': 0}})

# print(movies)


# 영화 평점을 숫자형으로 바꾸기
# movies = db.movies.find()
#
# for movie in movies:
#     db.movies.update_one(
#         {'title': movie['title']},
#         {'$set': {'star': float(movie['star'])}}
#     )

# 조건부 조회
# gte = greater than equal => 이상
# gt  = greater than => 초과
# lte = less than equal => 이하
# lt = less than => 미만
new_movies = list(
    db.movies.find({'star': {'$gte': 9.45, '$lt': 9.7}})
)

print(new_movies)
print(len(new_movies))