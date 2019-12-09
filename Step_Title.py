import requests                               #Here we are importing package called 'requests' which will be used for requesting webpage
import bs4                                    #Here we are importing package called 'Beautiful Soup'
var = requests.get('https://stepapp.ai/')     #Requesting a webpage on wikipedia
cont1 = bs4.BeautifulSoup(var.text, 'lxml')   #This BeautifulSoup will take two parameters, first is object var.text and second is structure we want
count2 = cont1.select('title')                
print(count2)
