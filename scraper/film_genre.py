import pandas as pd
import os

CSV_PATH = "../csv/"
CSV_FILE_NAME = "filmGenre.csv"

if __name__ == "__main__":
    film = pd.read_csv("../csv/initFilms.csv")
    genre = pd.read_csv("../csv/initGenres.csv")
    
    # Převedeme string reprezentaci seznamu na skutečný seznam
    film['genres'] = film['genres'].apply(eval)

    # Create a list to store the film-genre relationships
    film_genre_relations = []


    for index, row in film.iterrows():
        film_id = index + 1
        film_name = row['name_cz']
        
        for genre_name in row['genres']:
            if genre_name:
                genre_row = genre[genre['name_cz'] == genre_name]
                if not genre_row.empty:
                    genre_id = genre_row.index[0] + 1
                    film_genre_relations.append({
                        "MOVIE NAME": film_name,
                        "fk_film": film_id,
                        "fk_genre": genre_id
                    })

    print(film_genre_relations)
    dataFrame = pd.DataFrame(film_genre_relations, columns=["MOVIE NAME", "fk_film", "fk_genre"])

    dataFrame.to_csv(os.path.join(CSV_PATH, CSV_FILE_NAME), index=False, encoding='utf-8-sig')