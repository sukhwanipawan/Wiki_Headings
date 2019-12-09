import requests                               
import bs4
var = requests.get('https://stepapp.ai/')
cont1 = bs4.BeautifulSoup(var.text, 'lxml')
count2 = cont1.select('title')
print(count2)
