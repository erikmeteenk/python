from imdb.sql import create_tables, person_db, reviewer_db, movie_db, genre_db 
from imdb.config import connection_detail as cd 




# create database => sql_details must not contain database name
if 'database' not in cd.sql_details:
    create_tables.create_tables_imdb(cd.sql_details)


# Insert, update, delete and Query => sql_details must contain database name
if 'database' in cd.sql_details:

        ## Test genres ##
    genre_db.insert_genre("test") 
    genre_db.insert_genres_from_json('imdb/data/genres.json') 
    genre_db.delete_genre_by_id(1) 
    genre_db.update_genre_by_id(2, "test2")
    print(genre_db.select_all_genres())    

    ## Test persons table ##
    count = person_db.insert_persons_from_json('imdb/data/persons.json')    
    print("insert {} persons in db".format(count))
    persons = person_db.select_all_persons()
    print(persons)


    ## Test Movies ##
    count = movie_db.insert_movies_from_json('imdb/data/movies.json')
    print("insert {} movies in db".format(count))
    movies = movie_db.select_all_movies()
    print(movies)

    ## Test Reviewers and Ratings
    reviewer_db.insert_reviewer('joel', 'j_van_eyken@hotmail.com',"The Good, the Bad and the Ugly", 7)
    reviewer_db.insert_reviewer('Veronique', 'veronique.mertens@gmail.com', "The Good, the Bad and the Ugly", 5)
    movies = movie_db.select_all_movies()
    print(movies)
    
    movie = movie_db.select_one_movie(9)
    print(movie)
