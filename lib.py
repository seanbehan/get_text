from readability import Document
from bs4 import BeautifulSoup
from requests import get

def text(url):
    if 'http' not in url:
        url = 'http://' + url
    page = get(url).text
    doc = Document(page).summary()
    text = BeautifulSoup(doc).get_text()
    return text.strip()
