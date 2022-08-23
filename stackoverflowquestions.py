import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
for pergunta in html.select('.s-post-summary.js-post-summary'):
    titulo = pergunta.select_one('.s-post-summary--content-title')
    data = pergunta.select_one('.s-user-card--time')
    votos = pergunta.select_one('.s-post-summary--stats-item.s-post-summary--stats-item__emphasized')
    print('[',data.text, titulo.text, votos.text, ']', sep='\t')
