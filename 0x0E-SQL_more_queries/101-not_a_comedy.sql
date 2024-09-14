-- Lists all shows without genre Comedy in the db hbtn_0d_tvshows
-- uses a db to list all rows not linked to one row
SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT tv_shows.title
	FROM tv_shows
	JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC;
