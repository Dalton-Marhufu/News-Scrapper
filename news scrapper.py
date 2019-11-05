import requests
from bs4 import BeautifulSoup
import ezgmail

url = "https://ewn.co.za/"
responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'html.parser')
news = soup.find('h4')

#To view output in console
for news in soup.find_all("h4"):
    print(news.text) 

#Loop through news headlines and create a txt file
with open('mynews.txt', 'w') as f:
    for news in soup.find_all("h4"):
       f.write((news.text + '\n'))
       
#create an email attachment and send
ezgmail.send('daltonmarhufu@gmail.com', 'Todays-News!', 'Beep bop this is a bot giving news', ['mynews.txt'])
