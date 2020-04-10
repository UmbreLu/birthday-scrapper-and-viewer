from bs4 import BeautifulSoup as bs
import requests
import json

month_dict = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
        }

data = dict()

main_url = 'https://www.famousbirthdays.com/profession/scientist.html'
req = requests.get(main_url)
soup = bs(req.text, 'html.parser')

links = []

for anchor in soup.find_all('a', class_='face person-item'):
    links.append(anchor.get('href'))


data = dict()

for link in links:
    try:
        req2 = requests.get(link)
        soup2 = bs(req2.text, 'html.parser')
        name = soup2.h1.next_element.strip()
        month = soup2.h6.next_sibling.next_sibling.span.string
        day = soup2.h6.next_sibling.next_sibling.contents[2].strip()
        year = soup2.h6.next_sibling.next_sibling.next_sibling.next_sibling.string
        month2 = month_dict[month]
        birthday = '/'.join([month2, day, year])
        data[name] = birthday
        print(name + ': ' + birthday)
    except:
        continue

with open('scientist_birthdaysz.json', 'w') as f:
    json.dump(data, f)
    
