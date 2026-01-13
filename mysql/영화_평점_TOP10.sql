SELECT title, rating, vote_count
FROM movies
WHERE vote_count >= 100
ORDER BY rating desc
LIMIT 10