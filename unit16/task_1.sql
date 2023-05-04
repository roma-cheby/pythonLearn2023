DROP TABLE IF EXISTS actors;
CREATE TABLE actors(
    act_id INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50),
    act_last_name VARCHAR(50),
    act_gender VARCHAR(1)
);

DROP TABLE IF EXISTS movie;
CREATE TABLE movie(
    mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_title VARCHAR(50)
);

DROP TABLE IF EXISTS director;
CREATE TABLE director(
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50),
    dir_last_name VARCHAR(50)
);

DROP TABLE IF EXISTS movie_cast;
CREATE TABLE movie_cast(
    act_id INTEGER REFERENCES actors(act_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE,
    role VARCHAR(50)
);

DROP TABLE IF EXISTS oscar_awarded;
CREATE TABLE oscar_awarded(
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS movie_direction;
CREATE TABLE movie_direction(
    dir_id INTEGER REFERENCES director(dir_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);