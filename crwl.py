from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlparse
from collections import deque
import re


url = input("Enter the URL to crwl:")
new_urls = deque([url])
processed_urls = set()

while len(new_urls):
    url = new_urls.popleft()
    processed_urls.add(url)
    parts = urlparse(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    print("Processing %s" % url)
    try:
        response = requests.get(url)
    except:
        # ignore pages with errors
        continue
 
    soup = BeautifulSoup(response.text,"lxml")


    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        if not link in new_urls and not link in processed_urls:
            new_urls.append(link)
