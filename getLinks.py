import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(30)
url = 'https://www.civcastusa.com/bids?page=500&timeInfo=0&isReversed=true&orderBy=BidDate'
driver.get(url)
time.sleep(3)
outerHTML = driver.execute_script("return document.documentElement.outerHTML")
html_soup = BeautifulSoup(outerHTML, 'html.parser')

total_pages = int(html_soup.find_all('li', class_='page-item')[3].text)
print(total_pages)
with open("list", "w") as list_file:
    for page_number in range(1,total_pages+1):
        url = 'https://www.civcastusa.com/bids?page='+str(page_number)+'&timeInfo=0&isReversed=true&orderBy=BidDate'
        driver.get(url)
        time.sleep(3)
        outerHTML = driver.execute_script("return document.documentElement.outerHTML")
        html_soup = BeautifulSoup(outerHTML, 'html.parser')
        for i in html_soup.find_all('div', class_='col-12 col-lg-6 d-flex flex-column'):
            list_file.write('https://www.civcastusa.com'+i.a["href"]+'\n')


# ccType = html_soup.find_all('div', class_='col-12')
# for i in html_soup.find_all('div', class_='col-12'):
# print (i.text)
# cc.append(i.text)

# print(cc)
# https://www.civcastusa.com/project/5cb7721abdb68fdc897d6f1c/summary
