import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = "https://www.amazon.in/s?k=Samsung+Galaxy+Buds3+Pro+Wireless"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
products = soup.select('div[data-component-type="s-search-result"]')
