-- FILMY
COPY film(name_cz, name_en, release_year) 
FROM '/tmp/initFilms.csv' DELIMITER ',' CSV HEADER;

-- ŽÁNRY
COPY genre(name_cz, name_en) 
FROM '/tmp/initGenres.csv' DELIMITER ',' CSV HEADER;

-- FILM_GENRE
COPY film_genre(fk_film, fk_genre) 
FROM '/tmp/filmGenre.csv' DELIMITER ',' CSV HEADER;
