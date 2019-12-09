from bs4 import BeautifulSoup                                   #Here we are importing package called 'bs4'
import requests                                                 #Here we are importing package called 'requests' which will be used for requesting webpage
reg1 = requests.get('https://en.wikipedia.org/wiki/Python')     #Requesting a webpage on wikipedia
reg2 = BeautifulSoup(reg1.text, 'lxml')                         #This BeautifulSoup will take two parameters, first is object reg1.text and second is structure we want
reg3 = reg2.select('.mw-headline')
for i in reg3:                                                  #looping through data to get headings which we need
    print(i.text)
