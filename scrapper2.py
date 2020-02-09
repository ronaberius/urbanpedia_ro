from bs4 import BeautifulSoup
import json
import re
# import script crawl1 din . 
# import crawl1
from urllib.parse import unquote, unquote_plus

def scrap(a):
    try:
        with open(f"/home/vladootz/Documents/urbanpedia/das_defs/{a}/index.html", "r") as f:
            contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        part1 = (soup.find('h1', attrs={ "class" : "definition"}))
        part2 = (soup.find('div', attrs={ "class" : "detailDefinition"}))
        part3 = (soup.find('div', attrs={ "class" : "detailExample"}))

        cuv1 = (BeautifulSoup(str(part1), 'lxml').get_text())
        # print(cuv)
        cuv2 = (BeautifulSoup(str(part2), 'lxml').get_text())
        # print(cuv2)
        cuv3 = (BeautifulSoup(str(part3), 'lxml').get_text())
        # print(cuv3)

        cuv4 = ' '.join(cuv1.split())
        cuv5 = ' '.join(cuv2.split())
        cuv6 = ' '.join(cuv3.split())

        # m = {'cuvant' : cuv4, 'definitie' : cuv5, 'exemplu' : cuv6}
        # n = json.dumps(m)
        # o = json.loads(n)
        # print(o['cuvant'], o['definitie'], o['exemplu'])

        if cuv4 == 'None':
            data = {
                'cuvant': "n-avem",
                'definitie': "n-avem",
                'exemplu': "n-avem"
                }
        else:
            data = {
                'cuvant': cuv4,
                'definitie': cuv5,
                'exemplu': cuv6
                }

        app_json = json.dumps(data, ensure_ascii=False).encode('utf8')
        # print(app_json.decode())
        with open(f'/home/vladootz/Documents/urbanpedia/json/{unquote_plus(a)}.json', 'w') as outfile:
            outfile.write(app_json.decode())
    except FileNotFoundError:
        data = {
                'cuvant': "n-avem",
                'definitie': "n-avem",
                'exemplu': "n-avem"
                }

        not_app_json = json.dumps(data, ensure_ascii=False).encode('utf8')

        with open(f'/home/vladootz/Documents/urbanpedia/json/{unquote_plus(a)}.json', 'w') as outfile:
            outfile.write(not_app_json.decode())