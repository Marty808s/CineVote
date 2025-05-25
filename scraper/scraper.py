import requests
import os
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.csfd.cz/zebricky/filmy/nejlepsi/"
FILM_PAGE_URL = "https://www.csfd.cz"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
FROM = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900] # to jsou záložky top 100 filmů
CSV_PATH = "./csv/"
CSV_FILE_NAME = "initFilms.csv"

def getLinksFromCurrentChartPage(url, header, from_pos=None):
  links = []
  if from_pos:
    url = url + f"?from={from_pos}"
  #full stránka
  response = requests.get(url, headers=header)
  #parser => DOM
  soup = BeautifulSoup(response.text, 'html.parser')
  #najdi mi figure
  figure = soup.find_all('figure', class_='article-img')

  for fig in figure:
    a = fig.find('a')
    if a:
      links.append(a['href'])

  print("Odkazy:", len(links), "|", "pořadí:", from_pos)
  return(links)


def scrapFilmPage(filmPage):
    response = requests.get(FILM_PAGE_URL + filmPage, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    film_info = soup.find("div", class_="film-info")

    if not film_info:
        return None

    film_data = {}

    #CZ title
    title_con = film_info.find("div", class_='film-header-name')
    if title_con:
        h1 = title_con.find("h1")
        film_data["name_cz"] = h1.get_text(strip=True) if h1 else None
    else:
        film_data["name_cz"] = None

    def get_title_by_flag(flag_title):
        img_tag = soup.find("img", class_="flag", title=flag_title)
        if img_tag:
            li = img_tag.find_parent("li")
            if li:
                title = li.get_text(strip=True).replace("(více)", "").replace("(méně)", "").strip()
                return title
        return None

    # EN title handler
    name_en = get_title_by_flag("USA")
    if not name_en:
        name_en = get_title_by_flag("Nový Zéland")
    if not name_en:
        name_en = get_title_by_flag("Velká Británie")
    if not name_en:
      name_en = get_title_by_flag("angličtina")
    if not name_en:
      name_en = get_title_by_flag("Austrálie")
    film_data["name_en"] = name_en

    # RELEASE year
    origin_con = film_info.find("div", class_="origin")
    if origin_con:
        span = origin_con.find("span")
        film_data["release_year"] = span.get_text(strip=(True)).replace(",", "") if span else None
    else:
        film_data["release_year"] = None

    # CATEGORIES
    genres_con = film_info.find("div", class_="genres")
    if genres_con:
        a_tags = genres_con.find_all("a")
        genres = [a.get_text(strip=True) for a in a_tags]
        film_data["genres"] = genres

    print(film_data)
    return film_data


def getChartLinks(charts):
  all_links = []

  for i in FROM:
    res = getLinksFromCurrentChartPage(BASE_URL, HEADERS, i)
    all_links.extend(res)
  return all_links


if __name__ == "__main__":
    res = getChartLinks(FROM)
    data = [scrapFilmPage(film) for film in res]
    dataFrame = pd.DataFrame(data, columns=["name_cz", "name_en", "release_year", "genres"])
    
    os.makedirs(CSV_PATH, exist_ok=True)
    dataFrame.to_csv(os.path.join(CSV_PATH, CSV_FILE_NAME), index=False, encoding='utf-8-sig')