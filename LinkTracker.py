from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
from collections import deque
import time

class ScraperBlockedError(Exception):
    pass

def process_url(url, base_url, path, new_urls, processed_urls):
    print(f"Processing {url}")
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        # Verify if the web site to the scraper
        if "Access Denied" in response.text:
            raise ScraperBlockedError("The scraper have been blocked by the web site.")
    except requests.exceptions.RequestException as e:
        print(f"Error when making request: {e}")
        return
    except ScraperBlockedError as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")

    for anchor in soup.find_all("a"):
        link = anchor.get("href", '')
        if link.startswith(('/', 'http', 'https')):
            full_url = urljoin(base_url, link)


            # Verifies that the scraper stays in the same domain and does not jump to another domain. The scraper keeps always in the same domain.
            if urlparse (full_url).netloc == urlparse(url).netloc:
                if full_url not in new_urls and full_url not in processed_urls:
                   new_urls.append(full_url)

    time.sleep(1)  # Adding a delay of a 1 second to avoid issues scraping the web and generate a overflow request

def main():
    start_time = time.time()

    url = input("Enter the URL to crawl: ")
    new_urls = deque([url])
    processed_urls = set()

    try:
        while new_urls:
            current_url = new_urls.popleft()
            processed_urls.add(current_url)
            parts = urlparse(current_url)
            base_url = f"{parts.scheme}://{parts.netloc}"
            path = current_url[:current_url.rfind('/') + 1] if '/' in parts.path else current_url

            process_url(current_url, base_url, path, new_urls, processed_urls)

    except ScraperBlockedError as e:
        print(f"El scraper have been blocked: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds") # If the loop hangs this will cause a forced exit

if __name__ == "__main__":
    main()
