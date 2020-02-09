import os
from urllib.parse import unquote
import scrapper2

dira = (os.listdir("/home/vladootz/Documents/urbanpedia/das_defs"))
#dirb = (unquote(os.listdir("/home/vladootz/Documents/urbanpedia/das_defs")))


def _path():
    # count=0
    for a in dira:
        unquote(a, encoding='utf-8')
        scrapper2.scrap(a)
        # count +=1
        # print(count)

_path()