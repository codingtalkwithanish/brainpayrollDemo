# import requests
# from bs4 import BeautifulSoup

# target_url="https://www.brainpayroll.co.uk/"

# response=requests.get(target_url)

# if response.status_code==200:
#     soup=BeautifulSoup(response.content,'html.parser')
#     text=""
#     for paragraph in soup.find_all('p'):
#         text+=paragraph.get_text()

#     with open('website_text.txt','w') as text_file:
#         text_file.write(text)

#     print("Text extracted duccessfully")

# else:
#     print(f"Error:Failed to retrive website content.status code.{response.status_code}")


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

visited_urls = set()
base_url = "https://www.brainpayroll.co.uk/"

def extract_text_from_tags(soup, tags):
    text = ""
    for tag in tags:
        for element in soup.find_all(tag):
            text += element.get_text() + "\n"
    return text

def crawl_and_extract(url, tags):
    global visited_urls
    if url in visited_urls or not url.startswith(base_url):
        return ""
    visited_urls.add(url)
    time.sleep(1)  # To prevent overloading the server
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to retrieve content from {url}. Status code: {response.status_code}")
        return ""
    
    soup = BeautifulSoup(response.content, 'html.parser')
    text = extract_text_from_tags(soup, tags)
    
    for link in soup.find_all('a', href=True):
        full_url = urljoin(base_url, link['href'])
        text += crawl_and_extract(full_url, tags)
    
    return text

tags_to_extract = ['p', 'h1', 'h2', 'h3', 'a', 'li']
all_text = crawl_and_extract(base_url, tags_to_extract)

with open('website_text.txt', 'w') as text_file:
    text_file.write(all_text)

print("Text extracted successfully")
