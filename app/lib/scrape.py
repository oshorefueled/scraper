import requests as request
from bs4 import BeautifulSoup, SoupStrainer


class Scrape:
    def __init__(self, search_code):
        self.search_code = search_code
        self.url = Scrape.build_url(self)

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

    def build_url(self):
        base_url = "http://www.censusdata.abs.gov.au"
        child_url = "/census_services/getproduct/census/2011/quickstat/"+self.search_code+"?opendocument&navpos=220"
        url = base_url + child_url
        return url












