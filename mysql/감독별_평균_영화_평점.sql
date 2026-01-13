SELECT d.name AS director, AVG(m.rating) AS avg_rating, COUNT(DISTINCT md.movie_id) AS movie_count
FROM directors d JOIN movie_directors md ON d.director_id=md.director_id JOIN movies m ON m.movie_id=md.movie_id
GROUP BY d.director_id
ORDER BY avg_rating DESC
LIMIT 10