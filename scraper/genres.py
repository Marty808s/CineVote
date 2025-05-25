import pandas as pd
import os

CSV_PATH = "./csv/"
CSV_FILE_NAME = "initGenres.csv"

if __name__ == "__main__":
    data = pd.read_csv("./csv/initFilms.csv")
    
    # Převedeme string reprezentaci seznamu na skutečný seznam
    data['genres'] = data['genres'].apply(eval)
    
    unique_genres_cz = data['genres'].explode().unique()
    
    genres_df = pd.DataFrame({
        'name_cz': unique_genres_cz,
        'name_en': [None] * len(unique_genres_cz)
    })
    
    print("DataFrame žánrů:")
    print(genres_df)
    
    # Uložíme do CSV
    genres_df.to_csv(os.path.join(CSV_PATH, CSV_FILE_NAME), index=False, encoding='utf-8-sig')

