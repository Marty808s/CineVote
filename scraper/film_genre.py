import pandas as pd
import os

CSV_PATH = "./csv/"
CSV_FILE_NAME = "filmGenre.csv"

if __name__ == "__main__":
    film = pd.read_csv("../csv/initFilms.csv")
    genre = pd.read_csv("../csv/initGenres.csv")
    
    # Převedeme string reprezentaci seznamu na skutečný seznam
    film['genres'] = film['genres'].apply(eval)

    filmGenre = {}

    # DODĚLAT KVULI FK
    for f_id, f in enumerate(film):
        for genre in f['genres']:
            if genre:
                for g_id, g in enumerate(genre):
                    if genre in g:
                        filmGenre["MOVIE NAME"] = f["name_cz"]
                        filmGenre["fk_film"] = f_id
                        filmGenre["fk_genre"] = g_id
                else:
                    continue

    print(filmGenre)
    dataFrame = pd.DataFrame(filmGenre, columns=["fk_film", "fk_genre"])


    # Uložíme do CSV
    #genres_df.to_csv(os.path.join(CSV_PATH, CSV_FILE_NAME), index=False, encoding='utf-8-sig')