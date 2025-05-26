import pandas as pd
import os

CSV_PATH = "../csv/"
CSV_SAVE_PATH = "../csv/.import/"
CSV_FILMS = "initFilms.csv"
CSV_FILM_GENRES = "filmGenre.csv"

if __name__ == "__main__":
    # GENRE
    films_genre_df = pd.read_csv(os.path.join(CSV_PATH, CSV_FILM_GENRES))
    if not films_genre_df.empty:
        df_film_genre_init = films_genre_df.drop(columns=['MOVIE NAME'])
        df_film_genre_init.to_csv(os.path.join(CSV_SAVE_PATH, CSV_FILM_GENRES), index=False, encoding='utf-8-sig')
    
    # FILM
    film_df = pd.read_csv(os.path.join(CSV_PATH, CSV_FILMS))
    if not film_df.empty:
        df_film_init = film_df.drop(columns=['genres'])
        df_film_init.to_csv(os.path.join(CSV_SAVE_PATH, CSV_FILMS), index=False, encoding='utf-8-sig')
    
    


    

