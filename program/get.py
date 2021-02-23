import requests
from lxml import etree
import pickle
url = 'https://app.memrise.com/course/272286/new-general-service-list-101/%d/'
results = {}
def get_words(url):
    results=[]
    page = requests.get(url)
    d = etree.HTML(page.text)
    words = d.xpath('//div[@class="thing text-text"]')
    for i in words:
        x = i.xpath('.//div[@class="text"]/text()')
        print(x)
        results.append(x)
    return results

for i in range(1, 29):
    print('Trying '+url%i)
    results[i] = get_words(url%i)
    print('%d Succeed!!!'%i)


with open('data', 'wb') as f:
    pickle.dump(results, f)