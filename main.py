from bs4 import BeautifulSoup
import requests


url = "http://www.ijreview.com/wp-admin/admin-ajax.php"
session = requests.Session()
page_size = 24

params = {
    'action': 'load_more',
    'numPosts': page_size,
    'category': '',
    'orderby': 'date',
    'time': ''
}

offset = 0
limit = 100
while offset < limit:
    params['offset'] = offset
    response = session.post(url, data=params)
    links = [a['href'] for a in BeautifulSoup(response.content).select('li > a')]
    for link in links:
        response = session.get(link)
        page = BeautifulSoup(response.content)
        title = page.find('title').text.strip()
        author = page.find('span', class_='author').text.strip()
        print {'link': link, 'title': title, 'author': author}

    offset += page_size