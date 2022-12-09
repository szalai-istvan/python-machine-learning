from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movies = soup.find_all(name="h3", class_="title")
titles = [movie.getText() for movie in movies]
titles = titles[::-1]