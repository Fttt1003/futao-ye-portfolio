import numpy as np


class Recommendation:
    # user_ratings应该要是私有的？
    def __init__(self, users_num, movies_num):
        self.users_ratings = np.array([
            [0]  # 用户1(管理员)
        ])  # 初始化一个二维数组，记录用户观看（评分后的电影）
        self.users_viewed = []  # 记录用户标记喜欢的电影
        self.users_num = users_num
        self.movies_num = movies_num
        # 根据电影评分初始化相似度表
        self.movies_similarity = None

    @staticmethod
    # 余弦公式计算电影之间的相似度
    def cosine_similarity(a, b):
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)  # a的模长
        norm_b = np.linalg.norm(b)
        if norm_a and norm_b:
            return dot_product / (norm_a * norm_b)
        else:
            return 0

    @staticmethod
    def refresh(top_n, recommend_movies):
        preferred, fallback = recommend_movies
        preferred_count = min(top_n, len(preferred))
        fallback_count = min(top_n - preferred_count, len(fallback))
        return (
            np.random.choice(preferred, preferred_count, replace=False).tolist()
            + np.random.choice(fallback, fallback_count, replace=False).tolist()
        )

    def update_user(self, user_rating):
        self.users_num += 1
        new_row = user_rating
        # 将新的评分行添加到二维数组中
        self.users_ratings = np.append(self.users_ratings, [new_row], axis=0)  # 在np中多添加一行
        self.users_viewed.append([])
        self.compute_similarity(0)

    def update_movie(self, initial=False):
        self.movies_num += 1
        new_row = np.zeros(self.users_num)
        new_column = new_row.reshape(-1, 1)
        self.users_ratings = np.append(self.users_ratings, new_column, axis=1)  # 电影更新后，user的电影数增加1
        if not initial:
            self.movies_similarity = np.append(self.movies_similarity, new_column, axis=1)  # 电影更新后，movie_similarity发生变化
            new_row = np.zeros(self.movies_num)
            self.movies_similarity = np.append(self.movies_similarity, new_row, axis=0)

    def update_rating(self, user_id, movie_id, rating):
        self.users_ratings[user_id][movie_id] = rating
        self.compute_similarity(movie_id)

    def compute_similarity(self, start):
        end = self.movies_num
        if self.movies_similarity is None or start == 0:
            self.movies_similarity = np.zeros((end, end))
            for i in range(self.movies_num):
                for j in range(i, self.movies_num):  # 只用计算上三角矩阵
                    similarity = self.cosine_similarity(self.users_ratings[:, i], self.users_ratings[:, j])
                    self.movies_similarity[i][j] = similarity
                    self.movies_similarity[j][i] = similarity
        # 更新特定列和行的电影相似度
        else:  # 用户对某部电影评分了
            for i in range(self.movies_num):
                similarity = self.cosine_similarity(self.users_ratings[:, i], self.users_ratings[:, start])  # 两个列
                self.movies_similarity[i][start] = similarity
                self.movies_similarity[start][i] = similarity

    def compute_pseudo_scores(self, user_id):
        user_ratings = self.users_ratings[user_id]
        pseudo_scores_list = np.zeros(self.movies_num)
        for movie_id, rating in enumerate(user_ratings):
            if rating > 0:  # 根据用户已评分的电影推断别的电影的“伪评分”
                pseudo_scores_list += rating * self.movies_similarity[movie_id]  # 这一加就是整个列表相加，省去了麻烦的遍历
        return pseudo_scores_list

    def recommend(self, user_id):
        user_pseudo_scores_list = self.compute_pseudo_scores(user_id)
        movies = np.arange(1, self.movies_num)
        unseen = movies[(self.users_ratings[user_id, movies] == 0)
                        & ~np.isin(movies, self.users_viewed[user_id - 1])]
        preferred = user_pseudo_scores_list[unseen] > 1
        return unseen[preferred], unseen[~preferred]
