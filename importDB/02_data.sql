-- FILMY
COPY films(id, name_cz, name_en, release_year) 
FROM '/tmp/initFilms.csv' DELIMITER ',' CSV HEADER;