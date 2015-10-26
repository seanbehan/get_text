from readability import readability
from bs4 import BeautifulSoup
from requests import get

def text(url):
    page = get(url).text
    doc = readability.Document(page).summary()
    text = BeautifulSoup(doc).get_text()
    return text.strip()
