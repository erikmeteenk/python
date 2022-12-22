use imdb;
SELECT m.title,g.name as genre
from movies as m
join movie_genre as mg on m.id = mg.movie_id
join genres as g on g.id = mg.genre_id
