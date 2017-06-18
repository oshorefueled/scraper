from scrape import Scrape


class Collapse(Scrape):
    def __init__(self, code):
        super(Collapse, self).__init__(code)
        self.this = Collapse
        self.strain_id = "tablesView"
        pass

    def get_collapse_content(self):
        html = super(Collapse, self).get_html()
        strain = super(Collapse, self).strain_by_id(self.strain_id)
        soup = Scrape.get_soup(html, strain)
        return soup

    def get_content(self, content_id):
        soup = self.this.get_collapse_content(self)
        content = soup.find(id=content_id)
        return content

    def get_collapse_headings(self):
        soup = Collapse.get_collapse_content(self)
        headings = soup.find_all(class_="heading")
        headings_list = []
        for heading in headings:
            headings_list.append(
                heading.find(class_="screenreaderonly").previous_element.span.next_sibling
            )
        return headings_list

    def get_tables(self, content_id):
        soup = self.this.get_content(self, content_id)
        tables = soup.find_all("table")
        return tables

    def get_table_data(self, table):
        table_headings = self.this.get_table_headings(table)
        table_group = table_headings[0]
        table_rows = table.tr.find_next_siblings("tr")
        inner_data = {"headings": [], "rows": []}

        for table_row in table_rows:
            table_row_list = self.this.get_table_row_data(table_row)
            inner_data["headings"] = table_headings
            inner_data["rows"].append(table_row_list)

        data = {table_group: inner_data}
        return data

    @staticmethod
    def get_table_headings(table):
        table_headings_list = []
        table_headings = table.find(class_="oddRow").find_all("th")
        for table_heading in table_headings:
            table_headings_list.append(table_heading.string)
        return table_headings_list

    @staticmethod
    def get_table_row_data(table_row_list):
        table_row_data = table_row_list.find_all("td")
        table_row_data_list = []
        for row_data in table_row_data:
            table_row_data_list.append(row_data.string)
        return table_row_data_list


