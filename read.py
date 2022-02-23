import requests
from bs4 import BeautifulSoup

user_list = ["taodong3221", "Amen33", "mozartiana", "kikiokikio", "TheTarr", "tyhll", "FragilityA",
        "meiyoumingzi", "Tanx", "cigarose", "tanzheng", "approachingu", "Junnne", "9pears",
        "ASTER0108", "kiwifallasleep", "chatang", "Chyzne", "Assassin1"]


def get_kudos_list(article_url):
    url = article_url
    base_url = "https://archiveofourown.org"
    data = requests.get(url)
    data.encoding = 'utf-8'
    soup = BeautifulSoup(data.text)
    h = soup.find(id="kudos")
    r = []
    for i in h.p:
        if " " not in i.text:
            r.append(i.text)
    if h.find(id="kudos_more_link"):
        more_data = requests.get(base_url+h.find(id="kudos_more_link").get('href')+"&page=2")
        more_data.encoding = 'utf-8'
        more_soup = BeautifulSoup(more_data.text)
        h = more_soup.find(id="kudos")
        for i in h.p:
            if " " not in i.text:
                r.append(i.text)
    ml = []
    for i in user_list:
        if i in r:
            ml.append(1)
        else:
            ml.append(0)
    return ml


k1 = get_kudos_list("https://archiveofourown.org/works/37062514")
# print(k1)
k2 = get_kudos_list("https://archiveofourown.org/works/34942288")
# print(k2)
k3 = get_kudos_list("https://archiveofourown.org/works/36565120")
# print(k3)
k4 = get_kudos_list("https://archiveofourown.org/works/35312842")
# print(k4)
k5 = get_kudos_list("https://archiveofourown.org/works/35082031")
# print(k5)

matrix = []
for i in range(len(user_list)):
    temp = k1[i] + k2[i] + k3[i] + k4[i] + k5[i]
    matrix.append(temp)
print(matrix)
