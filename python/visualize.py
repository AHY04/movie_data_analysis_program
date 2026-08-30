import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

conn = mysql.connector.connect(
    host="localhost",
    user="YOUR_USER_NAME",
    password="YOUR_PASSWORD",
    database="tmdb"
)

# 장르별 평균 평점
query_genre_rating = """
SELECT g.name AS genre, round(AVG(m.rating),2) AS avg_rating
FROM movies m JOIN movie_genres mg ON m.movie_id=mg.movie_id JOIN genres g ON g.genre_id=mg.genre_id
GROUP BY g.name
ORDER BY avg_rating DESC
"""

df_genre_rating = pd.read_sql(query_genre_rating, conn)

plt.figure(figsize=(10,6))
plt.bar(df_genre_rating["genre"], df_genre_rating["avg_rating"])
plt.title("장르별 평균 평점")
plt.xlabel("장르")
plt.ylabel("평균 평점")
plt.xticks(rotation=45)
plt.ylim(0,10)
plt.tight_layout()
plt.savefig("docs/genre_avg_rating.png")
plt.close()


# 감독별 영화 제작량 TOP10
query_director = """
SELECT d.name AS director, COUNT(DISTINCT md.movie_id) AS movie_count
FROM directors d JOIN movie_directors md ON d.director_id=md.director_id
GROUP BY d.director_id
ORDER BY movie_count desc
LIMIT 10
"""

df_director = pd.read_sql(query_director, conn)

plt.figure(figsize=(10,6))
plt.barh(df_director["director"], df_director["movie_count"])
plt.title("감독별 영화 제작량 TOP10")
plt.xlabel("영화 수")
plt.ylabel("감독")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("docs/director_movie_count.png")
plt.close()


# 장르별 영화 비율
query_genre_count = """
SELECT g.name AS genre, COUNT(DISTINCT mg.movie_id) AS movie_count, round(COUNT(DISTINCT mg.movie_id) * 100 / (SELECT COUNT(movie_id) FROM movies),2) AS percentage
FROM movie_genres mg JOIN genres g ON g.genre_id=mg.genre_id
GROUP BY g.genre_id
ORDER BY percentage desc
"""

df_genre_count = pd.read_sql(query_genre_count, conn)

plt.figure(figsize=(8,8))
plt.pie(df_genre_count["movie_count"], labels=df_genre_count["genre"], autopct="%1.1f%%", startangle=140)
plt.title("장르별 영화 수 비율")
plt.tight_layout()
plt.savefig("docs/genre_distribution.png")
plt.close()


# 영화 평점 TOP10
query_movie_rating = """
SELECT title, rating, vote_count
FROM movies
WHERE vote_count >= 100
ORDER BY rating desc
LIMIT 10
"""

df_movie_rating = pd.read_sql(query_movie_rating, conn)

plt.figure(figsize=(10,6))
plt.barh(df_movie_rating["title"], df_movie_rating["rating"])
plt.title("영화 평점 TOP10")
plt.xlabel("평점")
plt.ylabel("영화")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("docs/movie_rating.png")
plt.close()


# 감독별 평균 영화 평점 TOP10
query_director_rating = """
SELECT d.name AS director, AVG(m.rating) AS avg_rating, COUNT(DISTINCT md.movie_id) AS movie_count
FROM directors d JOIN movie_directors md ON d.director_id=md.director_id JOIN movies m ON m.movie_id=md.movie_id
GROUP BY d.director_id
ORDER BY avg_rating DESC
LIMIT 10
"""

df_director_rating = pd.read_sql(query_director_rating, conn)

plt.figure(figsize=(10,6))
plt.barh(df_director_rating["director"], df_director_rating["avg_rating"])
plt.title("감독별 평균 영화 평점 TOP10")
plt.xlabel("평균 평점")
plt.ylabel("감독")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("docs/director_avg_rating.png")
plt.close()

conn.close()

print("시각화 완료")
