import urllib.request
from bs4 import BeautifulSoup
from html.parser import HTMLParser

urls = "https://www.barnesjewish.org/"
html_list = []
a_list = []


def url_load(u, hl):  # opens up index.html and then runs then appends html dat to htmlList
    f = urllib.request.urlopen(u)
    mf = f.read()
    h_soup = BeautifulSoup(mf, 'html.parser')
    list.append(hl, h_soup)
    return h_soup


data = url_load(urls, html_list)

# cleans up the url to only include root domain url
# ex. https://www.walter.com => walter.com


def domain(u):
    d = u
    if "https://www." in d:
        return u.replace('https://www.', '')
    elif 'http://www.' in d:
        return u.replace('http://www.', '')
    elif 'http://' in d:
        return u.replace('http://', '')
    elif 'https://' in d:
        return u.replace('https://', '')


dom = domain(urls)


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)




# 3. runs a check to see if the links in the page contain the domain
# and then add that to aList
# and then then adds then appends htmlList
def all_links(al, hl):
    for link in hl.find_all('p'):
        print(link)
        #if dom in link:
            #a = link.get('href')
            #list.append(al, a)
            #f = urllib.request.urlopen(link)
            #mf = f.read()
            #soup = BeautifulSoup(mf, 'html.parser')
            #list.append(hl, soup)


all_links(a_list, html_list[0])

print(dom)

print(a_list)



