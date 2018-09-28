import requests
import re
import sys

def get_dank(url, max=-1):
    resp = requests.get()
    while (c < len(resp.text)):
        if (resp.text[c] == '<'):
            while (resp.text[c] != '>'):
                line.append(resp.text[c])
                c+=1

        line.append(resp.text[c])
        if (re.match(imgs_pattern, ''.join(line))):
            imgs.append(''.join(line))
            imgs_url = 'http:' + ''.join(line).split('"')[3]
            print(imgs_url)
            count += 1

            line = []
        else:
            line =[]
        c+=1