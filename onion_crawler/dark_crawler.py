import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Configure /posts....
def selenium_crawler():
    binary = FirefoxBinary("*path to your firefox binary*")
    driver = webdriver.Firefox(firefox_binary = binary)

    starting_node = "*your url*"
    found_nodes = []
    p = re.compile('\S+onion')

    # 
    # for post in posts:
    #   nodes = p.findall(post)
    #   found_nodes.append(nodes)

def soup_crawler():
    session = requests.session()
    session.proxies["http"] = "socks5h://localhost:9050"
    session.proxies["https"] = "socks5h://localhost:9050"

    # Choose a online link
    url = "http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion/"
    response = session.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # title of the webpage
    print("Page title: ", soup.title.string)

    # get all the links on tha webpage
    print("Links on the page: ")
    for link in soup.find_all("a"):
        if link.get("href").startswith("/"):
            print(url + link.get("href"))
        else:
            print(link.get("href"))

    # extract text from the webpage
    print(soup.get_text())

if __name__ == '__main__':
    soup_crawler()
