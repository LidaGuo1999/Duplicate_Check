from bs4 import BeautifulSoup
import requests

def scraper(search_str):
    url_index = "https://www.baidu.com/s"
    search_str = search_str
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }
    reHtml = requests.get(url=url_index, params={'wd': search_str}, headers=headers)

    soup = BeautifulSoup(reHtml.text)
    abstracts = soup.find_all(class_='c-abstract')
    longest = ''
    for a in abstracts:
        ems = a.find_all('em')
        for e in ems:
            if len(e.text) > len(longest):
                longest = e.text
    return longest

