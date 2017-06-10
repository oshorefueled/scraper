import requests as request
from bs4 import BeautifulSoup, SoupStrainer


class Scrape:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        html = request.get(self.url)
        return html.content

    @staticmethod
    def get_soup(html, strain=None):
        if strain is None:
            print "strain is not passed"
            soup = BeautifulSoup(html, 'html.parser')
        else:
            soup = BeautifulSoup(html, 'html.parser', parse_only=strain)
        return soup

    @staticmethod
    def strain_by_id(element_id):
        soup_strainer = SoupStrainer(id=element_id)
        return soup_strainer












