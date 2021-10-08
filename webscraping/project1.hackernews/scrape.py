import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# Select CSS Selectors, look for id on web
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

pprint.pprint(create_custom_hn(links, subtext))

