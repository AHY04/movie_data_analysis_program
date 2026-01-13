SELECT d.name AS director, COUNT(DISTINCT md.movie_id) AS movie_count
FROM directors d JOIN movie_directors md ON d.director_id=md.director_id
GROUP BY d.director_id
ORDER BY movie_count desc
LIMIT 10