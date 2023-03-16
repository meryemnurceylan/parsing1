from bs4 import BeautifulSoup
import requests

r = requests.get("https://ime.cbu.edu.tr/DuyuruArsiv/2")
soup = BeautifulSoup(r.text,'html.parser')

result = soup.find("div", attrs={"class":"card-body text-start"})
result1 = result.find_all("div", attrs={"class":"bg-dark text-light p-2 border"})

#ilan_sayisi = len(result1)
#ilan sayısı kadar veri alacağız

for i in result1:
    link_bas = "https://ime.cbu.edu.tr"
    link_son = i.a.get("href")
    link = link_bas+link_son
    print(link)

    r1 = requests.get(link)
    soup1 = BeautifulSoup(r1.text, 'html.parser')

    result2 = soup1.find("div", attrs={"class": "card-body"})
    result3 = result2.find_all("div", attrs={"class": "bg-info text-light p-2 border"})
    result4 = result2.find_all("div", attrs={"class": "justify-content-center mt-2"})

    for icerik_baslik in result3:
        print(icerik_baslik.get_text())
    for icerik in result4:
        print(icerik.get_text())

