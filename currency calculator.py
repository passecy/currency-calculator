# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import time


url = "https://www.doviz.com/"
response = requests.get(url)
araba = response.content
soup = BeautifulSoup(araba, "html.parser")
liste1 = []
liste2 = []
liste3 = []
liste4 = []
for x in soup.find_all("span", {"class": "name"}):
    liste1.append(x.text)
for y in soup.find_all("span", {"class": "value"}):
    liste2.append(y.text)
for i in liste2:
    i = i.strip("$")

    liste3.append(i)
for i in liste3:
    i = i.replace(",", ".")
    liste4.append(i)


def program4():
    print("""
        1-Altın
        2-Dolar
        3-Euro
        4-Sterlin
        """)
    while True:
        
        a = int(input("Hesaplamak istediğiniz kuru seçiniz:"))
        print("""                         """)
        b = int(input(liste1[a-1]+" miktarını giriniz:"))
        print("""                                 """)
        deger = b*float(liste4[a-1])
        print(b, liste1[a-1], "=", deger, "Türk Lirası")
        print("""                                  """)
        time.sleep(2)


program4()
