import requests
from bs4 import BeautifulSoup

class OxCrawler(object):

    def __init__(self, url):
        self.tags = ['cnpj', 'vprod', 'indtot', 'dhemi']
        self.invoice = requests.get(url)
        self.soup = BeautifulSoup(self.invoice.content, 'html.parser')

    def _pretty_date(self, date):
        date = date.split('T')
        return date[0] + ' ' + date[1].split('-')[0]

    def _pretty_cnpj(self, cnpj):
        pretty_cnpj = []
        for i in range(len(cnpj)):
            if i == 2 or i == 5:
                pretty_cnpj.append('.')
            elif i == 8:
                pretty_cnpj.append('/')
            elif i == 12:
                pretty_cnpj.append('-')
            pretty_cnpj.append(cnpj[i])
        return ''.join(pretty_cnpj)

    def get_cnpj(self):
        return self._pretty_cnpj(self.soup.find_all('cnpj')[0].get_text())

    def get_purchase_value(self):
        purchases_values = []
        for value in self.soup.find_all('vprod')[:-1]: # exclude last value
            purchases_values.append(value.get_text())
        return purchases_values

    def get_total_value(self):
        return self.soup.find_all('vprod')[-1].get_text() # get last value

    def get_items_total_amount(self):
        total_items = []
        for item in self.soup.find_all('indtot'):
            total_items.append(int(item.get_text()))
        return total_items

    def get_items_description(self):
        descriptions = []
        for item in self.soup.find_all('xprod'):
            descriptions.append(item.get_text())
        return descriptions

    def get_emission_date(self):
        return self._pretty_date(self.soup.find_all('dhemi')[0].get_text())
