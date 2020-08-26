CREATE TABLE movies (
index int PRIMARY KEY,    
movie_name varchar(225),
movie_year  varchar(225),
star_rating int
);

INSERT INTO movies (index,movie_name,movie_year,star_rating)
    VALUES (1,'Alien','1976',5);