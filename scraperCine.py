import requests
from bs4 import BeautifulSoup
import sys

page = requests.get("https://www.todoshowcase.com/")
soup = BeautifulSoup(page.content, "html.parser")
flag = False

if len(sys.argv) == 2:
    print(soup.title.string+"\n")
else:
    print("Argumentos invalidos\n")
    print("Uso: python3 "+ sys.argv[0]+" nombre de la pelicula")
    sys.exit()

movieName = str(sys.argv[1])


movies = soup.find_all("div", {"class": "titulo-pelicula"})

for movie in movies:
    if movie.h2.a.text.strip() == movieName:
        flag = True
        break
    
if flag == True:
    print("El cine tiene tu pelicula")
else:
     print("Lo siento no pude encontrarla")