import ast
import numpy as np

from Dataset import MovieMindProDB
from BackEnd.Recommendation_system import Recommendation


class MovieMindSystem:
    def __init__(self):
        self._users = []  # 储存一个个用户对象
        self._movies = []  # 储存一个个电影对象
        self._users_name = {}  # 储存用户名与用户加入顺序的一一对应关系
        self.movies_id = []
        self.users_num = 1
        self.movies_num = 1
        self.recommender = Recommendation(self.users_num, self.movies_num)

    # 根据一个唯一的用户名返回一个唯一的用户id，这个想法好像有点蠢
    @staticmethod
    def get_user_id(user_name):
        return MovieMindProDB.get_user_rating(user_name)

    @staticmethod
    def get_movie_name(movie_id):
        return MovieMindProDB.get_movie_name_of_movie_id(movie_id)

    # # 每增加一个用户就要更新用户表（用户id、用户数量）、用户评分表(面向对象样式的）
    # def create_user(self, user):
    #     user_name = user.get_user_name()
    #     user.set_id(self.users_num)  # 提高安全性，这里是不是可以考虑用随机的？这样子用户名的映射表就不是一一对应的顺序关系了
    #     # user.set_id(random.randint(10000, 99999))  # 这样子会重复，并且到时候找user_ratings不好找，还是不要那么安全吧
    #     self.users_num += 1
    #     self._users.append(user)
    #     self._users_name[user_name] = user.get_id()
    #     self.recommender.update_user()

    # 创建对象，面向数据库版
    def create_user(self, user_account, password, user_name, gender, viewlist, dislike, user_rating=None):
        self.users_num += 1
        MovieMindProDB.add_user(user_account=user_account, user_name=user_name, password=password, gender=gender)
        if type(user_rating) is str:
            user_rating = ast.literal_eval(user_rating)
            user_rating = np.array(user_rating)
        elif user_rating is None:
            user_rating = np.zeros(self.movies_num)
        self.recommender.update_user(user_rating)

    # # 每添加一部电影就要再次计算推荐器的电影相似度、电影表(面向对象形式的）
    # def add_movie(self, movie):
    #     movie_name = movie.get_movie_name()
    #     movie_gender = movie.get_movie_gender()
    #     movie_introduction = movie.get_movie_introduction()
    #     movie = Movie(movie_name, movie_gender, movie_introduction)
    #     movie.set_id(self.movies_num)
    #     self.movies_num += 1
    #     self._movies.append(movie)
    #     self.recommender.update_movie()

    # 面向数据库的
    def add_movie(self, movie_id, movie_name, genre, duration, release_time, introduction, director, main_actor,
                  image_path, movie_url, if_initial=False):
        self.movies_num += 1
        MovieMindProDB.add_movie(movie_id, movie_name, genre, duration, release_time, introduction, director,
                                 main_actor, image_path, movie_url)
        self.recommender.update_movie(initial=if_initial)

    def update_movie_rating(self, user_id, movie_id, rating):
        self.recommender.update_rating(user_id, movie_id, rating)

    def recommend_for_user(self, user_id, top_n):
        recommend_movies = self.recommender.recommend(user_id)
        final_recommend_movies = self.recommender.refresh(top_n, recommend_movies)
        return final_recommend_movies
