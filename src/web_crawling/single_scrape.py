import urllib.request
from bs4 import BeautifulSoup
import csv

urls = "https://www.verywellhealth.com/family-practice-physician-career-1736289"


def url_load(u):  # opens up index.html and then runs then appends html dat to htmlList
    f = urllib.request.urlopen(u)
    mf = f.read()
    h_soup = BeautifulSoup(mf, 'html.parser')
    return h_soup


data = url_load(urls)


def paragraph():
    for para in data.find_all('p'):

fin = all_links(a_list)




