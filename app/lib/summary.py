from constants import constants
from bs4 import BeautifulSoup, SoupStrainer
from scrape import Scrape
import requests as request


class Summary(Scrape):
    def __init__(self, url):
        self.summary_id = "tableSummaryHeader"
        Scrape.__init__(self, url)

    def get_summary_content(self):
        html = Scrape.get_html(self)
        strain = Scrape.strain_by_id(self.summary_id)
        soup = Scrape.get_soup(html, strain)
        return soup






