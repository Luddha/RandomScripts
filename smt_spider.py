import requests
import lxml
import re
import sys
from bs4 import BeautifulSoup


class Demon():
    def __init__(self, name):
        self.img = ""
        self.name = name
        self.stats = []
        self.spells = []
        self.url = "http://megamitensei.wikia.com/wiki/" + self.name

    def download_img(self,path):
        img_resp = requests.get(self.img)
        with open(path, 'wb') as f:
            f.write(img_resp.content)
    
    def get_info(self):
        resp = requests.get(self.url)
        soup = BeautifulSoup(resp.text, 'lxml')
        pattern = r'.*https:\/\/.*' + self.name + r'SMT.*'

        for a in soup.find_all('a'):
            try:
                if (re.match(pattern, a['href'])):
                    self.img = a['href']
                    break
            except:
                pass


def main():
    name = sys.argv[1]
    path = sys.argv[2]

    d = Demon(name)
    print("[*] Downloading img now...")
    d.get_info()
    d.download_img(path)
    print("[*] Done")


if __name__ == '__main__':
    main()

