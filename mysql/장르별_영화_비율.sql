SELECT g.name AS genre, COUNT(DISTINCT mg.movie_id) AS movie_count, round(COUNT(DISTINCT mg.movie_id) * 100 / (SELECT COUNT(movie_id) FROM movies),2) AS percentage
FROM movie_genres mg JOIN genres g ON g.genre_id=mg.genre_id
GROUP BY g.genre_id
ORDER BY percentage desc