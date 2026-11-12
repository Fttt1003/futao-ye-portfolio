import json
import sqlite3
from hashlib import pbkdf2_hmac
from hmac import compare_digest
from pathlib import Path
from secrets import token_hex

dbname = Path(__file__).with_name("MovieMind.db")


def create_and_initial_database():
    # 创建一个 SQLite 连接
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 创建table: movies
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='movies'")
    movies_exists = cur.fetchone()

    if not movies_exists:
        sql_create_movies = '''CREATE TABLE movies
                               (movie_id INTEGER,
                                movie_name TEXT,
                                genre TEXT,
                                movie_duration TEXT,
                                release_time TEXT,
                                introduction TEXT,
                                director TEXT,
                                starring_role TEXT,
                                image_path TEXT,
                                movie_url TEXT);'''

        cur.execute(sql_create_movies)
    else:
        print("Table 'movies' already exists.")

    # 创建table: users

    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    users_exists = cur.fetchone()

    if not users_exists:
        sql_create_users = '''CREATE TABLE users
                              (user_id INTEGER PRIMARY KEY,
                               user_account TEXT UNIQUE,
                               password TEXT,
                               user_name TEXT,
                               gender TEXT,
                               viewed_list TEXT,
                               user_rating TEXT,
                               dislike_movies TEXT,
                               favourite_movies TEXT,
                               favourite_genre TEXT);'''

        cur.execute(sql_create_users)
    else:
        print("Table 'users' already exists.")

    # 创建table: interaction
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='interaction'")
    interaction_exists = cur.fetchone()

    if not interaction_exists:
        sql_create_interaction = '''CREATE TABLE interaction
                                       (user_id INTEGER,
                                        movie_id INTEGER,
                                        value INTEGER);'''
        cur.execute(sql_create_interaction)
    else:
        print("Table 'interaction' already exists.")

    # 创建table: personalurl
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='personalurl'")
    personalurl_exists = cur.fetchone()

    if not personalurl_exists:
        sql_create_favourite = '''CREATE TABLE personalurl
                                           (personal_movie_id INTEGER PRIMARY KEY,
                                            user_id INTEGER,
                                            personal_movie_name TEXT,
                                            personal_movie_url TEXT,
                                            UNIQUE (user_id, personal_movie_name));'''
        cur.execute(sql_create_favourite)
    else:
        print("Table 'personalurl' already exists.")
    conn.commit()
    conn.close()

# users相关
def get_user_data_of_id(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute(
        "SELECT user_id, user_account, user_name, gender, viewed_list, user_rating, "
        "dislike_movies, favourite_movies, favourite_genre FROM users WHERE user_id=?",
        (user_id,),
    )
    temp = cur.fetchone()  # 使用fetchone()获取单个结果
    conn.close()

    if temp:
        # 将元组转换为列表
        user_data = list(temp)
        return user_data
    else:
        return None  # 如果没有找到用户，返回None

def password_digest(password, salt):
    return pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 600_000).hex()


def add_user(user_account, user_name, password, gender):
    salt = token_hex(16)
    stored_password = f"{salt}:{password_digest(password, salt)}"
    conn = sqlite3.connect(dbname)
    conn.execute(
        "INSERT INTO users (user_account, password, user_name, gender, viewed_list, user_rating, "
        "dislike_movies, favourite_movies, favourite_genre) VALUES (?, ?, ?, ?, '', '', '', '', '') "
        "ON CONFLICT(user_account) DO NOTHING",
        (user_account, stored_password, user_name, gender),
    )
    conn.commit()
    conn.close()


def login(user_account, password):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        # 检查账号是否存在以及密码是否正确
        cur.execute("SELECT password FROM users WHERE user_account = ?", (user_account,))
        user = cur.fetchone()

        if user:
            # 用户存在，验证密码
            salt, digest = user[0].split(":", 1)
            if compare_digest(digest, password_digest(password, salt)):
                return "Login successful."
            else:
                return "Login failed. Incorrect password."
        else:
            return "Login failed. Account does not exist."
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        # 不管登录成功与否，都关闭数据库连接
        conn.close()
def get_user_id_of_user_account(user_account):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE user_account = ?", (user_account,))
    result = cur.fetchone()
    conn.close()
    return result[0]
def insert_viewedlist(user_id, movie_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    movie_id_str = str(movie_id)  # 确保movie_id是字符串类型
    # 查询当前用户的viewed_list
    cur.execute("SELECT viewed_list FROM users WHERE user_id = ?", (user_id,))
    viewed_list_data = cur.fetchone()

    if viewed_list_data:
        viewed_list = viewed_list_data[0]  # 直接使用字符串
        # 检查movie_id是否已经存在
        if movie_id_str in viewed_list.split(','):
            print(f"Movie ID '{movie_id_str}' is already in the viewed list.")
        else:
            # 如果viewed_list不为空，则在末尾添加movie_id，否则直接设置为movie_id
            if viewed_list:  # 如果viewed_list不为空
                viewed_list += ',' + movie_id_str  # 添加新movie_id
            else:
                viewed_list = movie_id_str  # 如果为空，直接设置为movie_id
            # 更新viewed_list
            cur.execute("UPDATE users SET viewed_list = ? WHERE user_id = ?", (viewed_list, user_id))
            print(f"Movie ID '{movie_id_str}' has been added to the viewed list.")
    else:
        viewed_list = movie_id_str  # 如果viewed_list为空，则直接设置为movie_id
        # 更新viewed_list
        cur.execute("UPDATE users SET viewed_list = ? WHERE user_id = ?", (viewed_list, user_id))
        print(f"Movie ID '{movie_id_str}' has been added to the viewed list.")

    conn.commit()
    conn.close()

def insert_favourite_genre(user_id, genre):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    # 查询当前用户的favourite_genre
    cur.execute("SELECT favourite_genre FROM users WHERE user_id = ?", (user_id,))
    favourite_genre_data = cur.fetchone()

    if favourite_genre_data:
        favourite_genre = favourite_genre_data[0]  # 直接使用字符串
        if genre in favourite_genre.split(','):  # 检查genre是否已经存在
            print(f"Genre '{genre}' is already in the favourite genre list.")
        else:
            # 确保不在新添加的genre前添加逗号
            if favourite_genre:  # 如果favourite_genre不为空
                favourite_genre += ',' + genre  # 添加新genre
            else:
                favourite_genre = genre  # 如果为空，直接设置为genre
    else:
        favourite_genre = genre  # 直接设置genre，不添加逗号
        # 更新favourite_genre
        cur.execute("UPDATE users SET favourite_genre = ? WHERE user_id = ?", (favourite_genre, user_id))
        print(f"Genre '{genre}' has been set as the favourite genre.")

    # 更新favourite_genre
    cur.execute("UPDATE users SET favourite_genre = ? WHERE user_id = ?", (favourite_genre, user_id))
    print(f"Genre '{genre}' has been added to the favourite genre list.")

    conn.commit()
    conn.close()

def get_favourite_genre(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 查询用户的收藏电影类型列表
    cur.execute("SELECT favourite_genre FROM users WHERE user_id = ?", (user_id,))
    favourite_genre_data = cur.fetchone()

    conn.close()

    if favourite_genre_data:
        # 将字符串转换为列表
        favourite_genre_list = favourite_genre_data[0].split(',')
        # 过滤掉空字符串
        favourite_genre_list = [genre for genre in favourite_genre_list if genre]
        return favourite_genre_list
    else:
        # 如果用户没有收藏电影类型，返回空列表
        return []

def get_viewedlist(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 查询用户的观影列表
    cur.execute("SELECT viewed_list FROM users WHERE user_id = ?", (user_id,))
    viewed_list_data = cur.fetchone()

    conn.close()

    if viewed_list_data:
        # 将字符串转换为列表
        viewed_list = viewed_list_data[0].split(',')
        # 过滤掉空字符串，并转换为整数列表
        viewed_list = [int(movie_id) for movie_id in viewed_list if movie_id]
        return viewed_list
    else:
        # 如果用户没有观影记录，返回空列表
        return []

def insert_favourite_movie(user_id, movie_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    movie_id = str(movie_id)
    # 查询当前用户的favourite_movies
    cur.execute("SELECT favourite_movies FROM users WHERE user_id = ?", (user_id,))
    favourite_movies_data = cur.fetchone()

    if favourite_movies_data:
        favourite_movies = favourite_movies_data[0]  # 直接使用字符串
        if movie_id in favourite_movies.split(','):  # 检查movie_id是否已经存在
            print(f"Movie ID '{movie_id}' is already in the favourite movies list.")
        else:
            # 确保不在新添加的movie_id前添加逗号
            if favourite_movies:  # 如果favourite_movies不为空
                favourite_movies += ',' + movie_id  # 添加新movie_id
            else:
                favourite_movies = movie_id  # 如果为空，直接设置为movie_id
    else:
        favourite_movies = movie_id  # 直接设置movie_id，不添加逗号
        # 更新favourite_movies
        cur.execute("UPDATE users SET favourite_movies = ? WHERE user_id = ?", (favourite_movies, user_id))
        print(f"Movie ID '{movie_id}' has been set as the favourite movie.")

    # 更新favourite_movies
    cur.execute("UPDATE users SET favourite_movies = ? WHERE user_id = ?", (favourite_movies, user_id))
    print(f"Movie ID '{movie_id}' has been added to the favourite movies list.")

    conn.commit()
    conn.close()


def get_favourite_movies(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 查询用户的收藏电影列表
    cur.execute("SELECT favourite_movies FROM users WHERE user_id = ?", (user_id,))
    favourite_movies_data = cur.fetchone()

    conn.close()

    if favourite_movies_data:
        # 将字符串转换为列表
        favourite_movies_list = favourite_movies_data[0].split(',')
        # 过滤掉空字符串，并转换为整数列表
        favourite_movies_list = [int(movie_id) for movie_id in favourite_movies_list if movie_id]
        return favourite_movies_list
    else:
        # 如果用户没有收藏电影，返回空列表
        return []


def delete_favourite_movie(user_id, movie_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    movie_id = str(movie_id)
    # 查询当前用户的favourite_movies
    cur.execute("SELECT favourite_movies FROM users WHERE user_id = ?", (user_id,))
    favourite_movies_data = cur.fetchone()

    if favourite_movies_data:
        favourite_movies = favourite_movies_data[0]  # 直接使用字符串
        # 检查movie_id是否已经存在
        if movie_id in favourite_movies.split(','):
            # 移除movie_id
            favourite_movies_list = favourite_movies.split(',')
            # 过滤掉movie_id
            favourite_movies_list = [mid for mid in favourite_movies_list if mid != movie_id]
            # 重新组合字符串
            favourite_movies = ','.join(favourite_movies_list)
            # 更新favourite_movies
            cur.execute("UPDATE users SET favourite_movies = ? WHERE user_id = ?", (favourite_movies, user_id))
            print(f"Movie ID '{movie_id}' has been removed from the favourite movies list.")
        else:
            print(f"Movie ID '{movie_id}' is not in the favourite movies list.")
    else:
        print(f"No favourite movies list found for user ID {user_id}.")

    conn.commit()
    conn.close()


def insert_dislike_movie(user_id, movie_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    movie_id = str(movie_id)
    # 查询当前用户的dislike_movies
    cur.execute("SELECT dislike_movies FROM users WHERE user_id = ?", (user_id,))
    dislike_movies_data = cur.fetchone()

    if dislike_movies_data:
        dislike_movies = dislike_movies_data[0]  # 直接使用字符串
        if movie_id in dislike_movies.split(','):  # 检查movie_id是否已经存在
            print(f"Movie ID '{movie_id}' is already in the dislike movies list.")
        else:
            # 确保不在新添加的movie_id前添加逗号
            if dislike_movies:  # 如果dislike_movies不为空
                dislike_movies += ',' + movie_id  # 添加新movie_id
            else:
                dislike_movies = movie_id  # 如果为空，直接设置为movie_id
    else:
        dislike_movies = movie_id  # 直接设置movie_id，不添加逗号
        # 更新dislike_movies
        cur.execute("UPDATE users SET dislike_movies = ? WHERE user_id = ?", (dislike_movies, user_id))
        print(f"Movie ID '{movie_id}' has been set as the disliked movie.")

    # 更新dislike_movies
    cur.execute("UPDATE users SET dislike_movies = ? WHERE user_id = ?", (dislike_movies, user_id))
    print(f"Movie ID '{movie_id}' has been added to the dislike movies list.")

    conn.commit()
    conn.close()

def return_users():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute("select user_id from users")
    temp = cur.fetchall()
    result = []
    for i in range(len(temp)):
        result.append(temp[i][0])
    conn.commit()
    conn.close()
    return result

def update_user_rating(user_id, user_rating):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    user_rating = str(user_rating)
    # 直接使用传入的 user_rating 字符串更新用户评分
    cur.execute("UPDATE users SET user_rating = ? WHERE user_id = ?", (user_rating, user_id))

    print(f"User ID {user_id}'s rating has been updated.")

    conn.commit()
    conn.close()

def get_user_rating(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 获取电影总数，假设有一个函数get_movies_num()返回电影的总数
    total_movies = get_movies_num()

    # 初始化一个列表，用于存储每部电影的交互值，初始值为None
    user_ratings = [None] * total_movies

    # 查询用户的交互记录
    cur.execute("SELECT movie_id, value FROM interaction WHERE user_id = ?", (user_id,))
    interactions = cur.fetchall()

    # 将交互值填充到user_ratings列表中
    for movie_id, value in interactions:
        user_ratings[movie_id] = value  # 假设movie_id是从0开始的索引

    conn.close()
    return user_ratings



# personalurl相关方法

def add_personal_movie_url(user_id, personal_movie_name, personal_movie_url):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 检查个人电影 URL 是否已存在
    cur.execute("SELECT personal_movie_url FROM personalurl WHERE user_id = ? AND personal_movie_name = ?", (user_id, personal_movie_name))
    existing_url = cur.fetchone()

    if existing_url:
        print(f"Personal movie URL for '{personal_movie_name}' already exists for user ID {user_id}.")
    else:
        # 插入新的个人电影 URL
        cur.execute("INSERT INTO personalurl (user_id, personal_movie_name, personal_movie_url) VALUES (?, ?, ?)",
                    (user_id, personal_movie_name, personal_movie_url))
        print(f"Personal movie URL for '{personal_movie_name}' has been added for user ID {user_id}.")

    conn.commit()
    conn.close()



def get_personal_movies_url(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 查询用户的个人电影 URL
    cur.execute("SELECT personal_movie_name, personal_movie_url FROM personalurl WHERE user_id = ?", (user_id,))
    personal_movies_urls = cur.fetchall()

    conn.close()

    # 将结果转换为列表形式，每个元素是一个包含电影名称和 URL 的列表
    personal_movies_list = [[name, url] for name, url in personal_movies_urls]

    return personal_movies_list


def get_personal_movie_id_from_movie_name(user_id, movie_name):
    conn = sqlite3.connect(dbname)
    row = conn.execute(
        "SELECT personal_movie_id FROM personalurl WHERE user_id = ? AND personal_movie_name = ?",
        (user_id, movie_name),
    ).fetchone()
    conn.close()
    return row[0] if row else None


def get_personal_movie_url(user_id, personal_movie_id):
    conn = sqlite3.connect(dbname)
    row = conn.execute(
        "SELECT personal_movie_url FROM personalurl WHERE user_id = ? AND personal_movie_id = ?",
        (user_id, personal_movie_id),
    ).fetchone()
    conn.close()
    return row[0] if row else None


def delete_personal_movie(user_id, personal_movie_name):
    conn = sqlite3.connect(dbname)
    conn.execute(
        "DELETE FROM personalurl WHERE user_id = ? AND personal_movie_name = ?",
        (user_id, personal_movie_name),
    )
    conn.commit()
    conn.close()


# interaction相关方法
def insert_interaction(user_id, movie_id, value):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    # 检查记录是否存在
    cur.execute("SELECT 1 FROM interaction WHERE movie_id = ? AND user_id = ?", (movie_id, user_id))
    if cur.fetchone():
        # 如果记录存在，更新value值
        update_text = '''UPDATE interaction SET value = ? WHERE movie_id = ? AND user_id = ?;'''
        cur.execute(update_text, (value, movie_id, user_id))
    else:
        # 如果记录不存在，插入新记录
        insert_text = '''INSERT INTO interaction (user_id, movie_id, value) VALUES (?, ?, ?);'''
        cur.execute(insert_text, (user_id, movie_id, value))
    conn.commit()
    conn.close()

def get_sub_interaction_of_user_id(user_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    get_sub_interaction_from_user_text = '''SELECT * FROM interaction WHERE user_id = ?;'''
    cur.execute(get_sub_interaction_from_user_text, (user_id,))
    sub_inter_from_user = [list(cur) for cur in list(cur.fetchall())]

    conn.commit()
    conn.close()
    return sub_inter_from_user

def get_all_interactions_of_users():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 编写 SQL 查询语句，选择所有不同的 userAccount
    sql_query = '''SELECT DISTINCT user_id FROM interaction;'''

    # 执行 SQL 查询语句
    cur.execute(sql_query)

    # 获取查询结果
    allUserIds = cur.fetchall()

    # 初始化 allInteraction 列表
    allInteraction = []

    # 遍历所有 movieId，获取每个 movieId 的交互值
    for user_id in allUserIds:
        userIdInteraction = get_sub_interaction_of_user_id(user_id[0])
        allInteraction.append(userIdInteraction)

    conn.close()
    return allInteraction


# movie相关方法
def add_movie(movie_id, movie_name, genre, movie_duration, release_time,
              introduction, director, starring_role, image_path, movie_url):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute("SELECT EXISTS(SELECT movie_id FROM movies WHERE movie_id = ?)", (movie_id,))
    movie_exist = cur.fetchone()

    if movie_exist[0] == 1:
        print(f"movie {movie_id} exist")
    else:
        cur.execute("insert into movies (movie_id, movie_name, genre, movie_duration, release_time,"
                    "introduction, director, starring_role, image_path, movie_url) "
                    "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (movie_id, movie_name, genre,
                                                              movie_duration,release_time,
                                                              introduction, director, starring_role,
                                                              image_path, movie_url))


    conn.commit()
    conn.close()
    users = return_users()
    for i in range(len(users)):
        insert_interaction(users[i], movie_id, 1)


def get_data_of_movie_id(movie_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * from movies where movie_id = ?", (movie_id,))
    temp = cur.fetchone()  # 使用fetchone()获取单个结果
    conn.close()

    if temp:
        # 将元组转换为列表
        user_data = list(temp)
        return user_data
    else:
        return None  # 如果没有找到用户，返回None

def get_movie_name_of_movie_id(movie_id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT movie_name from movies where movie_id = ?", (movie_id,))
    temp = cur.fetchone()  # 使用fetchone()获取单个结果
    conn.close()

    return temp[0]
def get_movies_num():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute("SELECT * from movies")
    movies_num = len(list(cur.fetchall()))
    conn.close()
    return movies_num

def search_movie_of_keyword(keyword):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 使用LIKE语句在多个字段中搜索关键词
    cur.execute("""
        SELECT movie_id
        FROM movies
        WHERE movie_name LIKE ? OR introduction LIKE ? OR starring_role LIKE ? OR director LIKE ?
    """, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))

    # 获取所有匹配的电影ID
    movie_ids = cur.fetchall()

    # 将结果转换为列表形式，每个元素是一个电影的ID
    movie_id_list = [id[0] for id in movie_ids]

    conn.close()
    return movie_id_list
