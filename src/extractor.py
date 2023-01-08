import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def extract_text(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

def extract_poetry(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    lines = []
    for div in soup.find_all('div', {'class': 'content-right'}):
        for p in div.find_all('p'):
            line = p.text.replace(u'\xa0', u' ').replace(u'\u200c', u'').strip()
            if line:
                lines.append(line)

    return lines

def extract_links(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    urls = []
    for div in soup.find_all('div', {'class': 'suchi_patra_area'}):
        for li in div.find_all('li'):
            ref = li.a['href']
            urls.append(url + ref[len(ref) - ref[::-1].index('/') - 1:])
    return urls
