-- Tabulka rolí
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE
);

-- Tabulka uživatelů
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) UNIQUE,
    fk_roles INTEGER,
    FOREIGN KEY (fk_roles) REFERENCES roles(id)
);

-- Tabulka filmů
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    name_cz VARCHAR(100),
    name_en VARCHAR(100),
    release_year INTEGER
);

-- Kategorie filmů
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name_cz VARCHAR(100) UNIQUE,
    name_en VARCHAR(100) UNIQUE
);

-- Spojovací tabulka film - kategorie
CREATE TABLE film_categories (
    id SERIAL PRIMARY KEY,
    fk_film INTEGER,
    fk_category INTEGER,
    FOREIGN KEY (fk_film) REFERENCES films(id),
    FOREIGN KEY (fk_category) REFERENCES categories(id)
);

-- Hodnoty hlasování (např. ano/ne)
CREATE TABLE vote_values (
    id SERIAL PRIMARY KEY,
    value BOOLEAN NOT NULL
);

-- Hlasování uživatelů
CREATE TABLE users_votes (
    id SERIAL PRIMARY KEY,
    fk_value INTEGER,
    fk_user INTEGER,
    FOREIGN KEY (fk_value) REFERENCES vote_values(id),
    FOREIGN KEY (fk_user) REFERENCES users(id)
);

-- Sezení (např. jedno hlasování)
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    fk_creator INTEGER,
    sess_code VARCHAR(64) UNIQUE NOT NULL,
    created_at DATE,
    FOREIGN KEY (fk_creator) REFERENCES users(id)
);

-- Spojovací tabulka sezení - uživatelé
CREATE TABLE sessions_users (
    id SERIAL PRIMARY KEY,
    fk_session INTEGER,
    fk_user INTEGER,
    FOREIGN KEY (fk_session) REFERENCES sessions(id),
    FOREIGN KEY (fk_user) REFERENCES users(id)
);

-- Spojovací tabulka sezení - filmy
CREATE TABLE sessions_films (
    id SERIAL PRIMARY KEY,
    fk_session INTEGER,
    fk_film INTEGER,
    FOREIGN KEY (fk_session) REFERENCES sessions(id),
    FOREIGN KEY (fk_film) REFERENCES films(id)
);

-- Hlasování v rámci sezení a filmu
CREATE TABLE sessions_votes (
    id SERIAL PRIMARY KEY,
    fk_session_film INTEGER,
    fk_vote INTEGER,
    FOREIGN KEY (fk_session_film) REFERENCES sessions_films(id),
    FOREIGN KEY (fk_vote) REFERENCES users_votes(id)
);
