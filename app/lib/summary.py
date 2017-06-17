from constants import constants
from scrape import Scrape


class Summary(Scrape):
    def __init__(self, url):
        self.summary_id = "tableSummaryHeader"
        self.filter_class = "strongRow"
        self.table_class = "summaryTable"
        Scrape.__init__(self, url)

    # get only the summary of the website
    def get_summary_content(self):
        html = Scrape.get_html(self)
        strain = Scrape.strain_by_id(self.summary_id)
        soup = Scrape.get_soup(html, strain)
        return soup

    # find title of each group
    def find_group_names(self):
        soup = Summary.get_summary_content(self)
        group_names = soup.find_all(class_=self.filter_class)
        return group_names

    # get the title of each summary group
    def get_group_names(self):
        group_tags = Summary.find_group_names(self)
        group_names = []
        for i in group_tags:
            print i
            td = i.find_all("td")
            group_name = td[0].string
            group_value = td[1].string.replace(",", "")
            group_names.append([group_name, int(group_value)])
        return group_names

    @staticmethod
    def filter_by_class(class_name):
        return class_name != "strongRow"

    '''
    get all summary of groups
    :returns list
    '''
    def get_group_details(self):
        soup = Summary.get_summary_content(self)
        summary_tables = soup.find_all(class_="summaryTable")
        group_details = []
        for i in summary_tables:
            group_details.append(i.find_all("tr", class_=Summary.filter_by_class))
        return group_details

    def extract_group_details(self):
        pass

    def build_summary_data(self):
        headings = Summary.get_group_names(self)
        details = Summary.get_group_details(self)
        data = []

        for i in range(0, len(headings)):
            extracted_details = Summary.extract_details(details[i])
            data.append({"title": headings[i][0],
                         "value": headings[i][1],
                         "data": extracted_details
                         })
        return data

    @staticmethod
    def extract_details(detalis):
        data_list = []
        for i in detalis:
            title = i.find('td').string
            value = i.find(class_="summaryData").string
            data_list.append({"title": title, "value": value})
        return data_list
