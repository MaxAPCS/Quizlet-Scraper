from bs4 import BeautifulSoup
from json import dump

term_list = {}

for i in BeautifulSoup(
            open("page.htm", "r", encoding="utf8")
                .read(),
            'html.parser'
        ).findAll('div', {'class': 'SetPageTerms-term'}):

    [a, b, *_] = i.findAll('span')
    term_list[a.text] = b.text.replace("\n", "")

with open('out.json', 'w') as f:
    dump(term_list, f)
