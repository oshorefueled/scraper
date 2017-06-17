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

    def get_collapse_headings(self):
        soup = Collapse.get_collapse_content(self)
        headings = soup.find_all(class_="heading")
        headings_list = []
        for heading in headings:
            headings_list.append(
                heading.find(class_="screenreaderonly").previous_element.span.next_sibling
            )
        return headings_list

    def get_people_content(self):
        soup = Collapse.get_collapse_content(self)
        content = soup.find(id="peopleContent")
        return content

    def get_people_subheadings(self):
        subheading_list = []
        people_content = Collapse.get_people_content(self)
        subheadings = people_content.find_all("h5")
        for subheading in subheadings:
            subheading_list.append(subheading.string)
        print subheading_list
        return []

    def get_people_tables(self):
        soup = self.this.get_people_content(self)
        tables = soup.find_all("table")
        return tables

    def get_people_table(self):
        table = Collapse.get_people_content(self).find("table")
        return table

    @staticmethod
    def get_table_headings(table):
        table_headings_list = []
        table_headings = table.find(class_="oddRow").find_all("th")
        for table_heading in table_headings:
            table_headings_list.append(table_heading.string)
        return table_headings_list

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
    def get_table_row_data(table_row_list):
        table_row_data = table_row_list.find_all("td")
        table_row_data_list = []
        for row_data in table_row_data:
            table_row_data_list.append(row_data.string)
        return table_row_data_list

    @staticmethod
    def get_table_group(table_row, group_class):
        return table_row.find(class_=group_class).string

    def get_people_data(self):
        tables = self.this.get_people_tables(self)
        table_data = []
        for table in tables:
            table_data.append(self.this.get_table_data(self, table))

        return table_data




