import requests
from bs4 import BeautifulSoup


url = "https://ewn.co.za/"
responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'html.parser')
news = soup.find('h4')

#for news in soup.find_all("h4"):
    #print(news.text) 

with open('mynews.txt', 'w') as f:
    for news in soup.find_all("h4"):
       f.write((news.text + '\n'))

       
emaail = 
