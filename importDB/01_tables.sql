CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE

);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) UNIQUE,
    FOREIGN KEY (fk_role) REFERENCES roles(id)
);

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    name_cz VARCHAR(100) UNIQUE,
    name_en VARCHAR(100) UNIQUE,
    release_year INTEGER
);

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name_cz VARCHAR(100) UNIQUE,
    name_en VARCHAR(100) UNIQUE
);

CREATE TABLE film_category (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (fk_film) REFERENCES films(id),
    FOREIGN KEY (fk_category) REFERENCES category(id)
);

CREATE TABLE vote_values (
    id SERIAL PRIMARY KEY,
    value BOOLEAN NOT NULL
);

CREATE TABLE user_votes (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (fk_value) REFERENCES value(id),
    FOREIGN KEY (fk_user) REFERENCES user(id)
);

CREATE TABLE session (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (fk_creator) REFERENCES users(id),
    sess_code VARCHAR(64) UNIQUE NOT NULL,
    created_at DATE
);

CREATE TABLE session_user (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (fk_session) REFERENCES session(id),
    FOREIGN KEY (fk_user) REFERENCES user(id)

);

CREATE TABLE session_film (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (fk_session) REFERENCES session(id),
    FOREIGN KEY (fk_film) REFERENCES films(id)

);

CREATE TABLE session_votes (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (fk_session_film) REFERENCES session_film(id),
    FOREIGN KEY (fk_vote) REFERENCES user_votes(id)

);