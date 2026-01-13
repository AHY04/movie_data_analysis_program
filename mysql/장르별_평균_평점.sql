SELECT g.name AS genre, round(AVG(m.rating),2) AS avg_rating
FROM movies m JOIN movie_genres mg ON m.movie_id=mg.movie_id JOIN genres g ON g.genre_id=mg.genre_id
GROUP BY g.name
ORDER BY avg_rating DESC