from bs4 import BeautifulSoup
import requests
from lxml import etree
from lxml import html
import urllib
from urllib.request import Request
import time
import lxml

def lotto():
    

    url = 'https://www.estrazionedellotto.it/'

    req = requests.get(url)
    bs = BeautifulSoup(req.text,"html.parser")
  
    
    re = Request(url, headers={'User-Agent':'Mozzilla/5.0'})

    response = urllib.request.urlopen(re)

    dom = html.fromstring(req.content)
    for x in range(1,3):
    
        dat = dom.xpath('//*[@class="tabellaLotto"]/div/span'+'['+str(x)+']')
        print(dat[0].text)
    print("attendere....")
    time.sleep(4)
    for x in range(1,7):
    
    
        uno = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[1]/td'+'['+str(x)+']')
        print(uno[0].text, end=" - ")
    for x in range(1,7):    
        due = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[2]/td'+'['+str(x)+']')
        print(due[0].text, end="- ")
    for x in range(1,7):
        tre = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[3]/td'+'['+str(x)+']')
        print(tre[0].text, end=" - ")
    for x in range(1,7):
        quattro = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[4]/td'+'['+str(x)+']')
        print(quattro[0].text, end=" - ")

    for x in range(1,7):
    
    
        cinque = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[1]/td'+'['+str(x)+']')
        print(cinque[0].text, end=" - ")
    for x in range(1,7):    
        sei = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[2]/td'+'['+str(x)+']')
        print(sei[0].text, end=" - ")
    for x in range(1,7):
        sette = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[3]/td'+'['+str(x)+']')
        print(sette[0].text, end=" - ")
    for x in range(1,7):
        otto = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[4]/td'+'['+str(x)+']')
        print(otto[0].text, end=" - ")

    for x in range(1,7):
    
    
        nove = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[1]/td'+'['+str(x)+']')
        print(nove[0].text, end=" - ")
    for x in range(1,7):    
        dieci = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[2]/td'+'['+str(x)+']')
        print(dieci[0].text, end=" - ")
    for x in range(1,7):
        undici = dom.xpath('//*[@class="tabellaEstrazioni"]/tbody/tr[3]/td'+'['+str(x)+']')
        print(undici[0].text, end=" - ")

#for x in range(1,8):
    print(" ")
    print(" ")
    lista = []
    txt = dom.xpath('//*[@class="sezione-commenti"]//*/text()')

    time.sleep(4)
    for x in txt:
    
    
        print(x)


    
def enalotto():
    url = 'https://www.estrazionedellotto.it/superenalotto/'
    req = requests.get(url)
    bs = BeautifulSoup(req.text,"html.parser")
  
    
    re = Request(url, headers={'User-Agent':'Mozzilla/5.0'})

    response = urllib.request.urlopen(re)

    dom = html.fromstring(req.content)
    for x in range(1,3):
        
        s = dom.xpath('//div[@class="tabellaSE"]/div/span['+str(x)+']')
        print(s[0].text)

    for x in range(1,9):
        
        en = dom.xpath('//table[@class="tabellaEstrazioniSE"]/tbody[1]/tr/td['+str(x)+']')    
        print(en[0].text, end=" ")
    r = dom.xpath('//div[@class="middle-section"]/div[2]/text()')
    print(r)


def comandi():
    print("\nScelta risultati del lotto e enalotto")
    select = input("Digita lotto o enalotto: ")
    time.sleep(4)
    print("attendere...")
    if select == "lotto":
        lotto()
        
    elif select == "enalotto":
        enalotto()
    main()

def main():
    time.sleep(2)
    comandi()
    
main()
