from collapse import Collapse


class People(Collapse):
    def __init__(self, code):
        super(People, self).__init__(code)
        self.this = People
        self.content_id = "peopleContent"

    def get_people_subheadings(self):
        subheading_list = []
        people_content = self.this.get_content(self, "peopleContent")
        subheadings = people_content.find_all("h5")
        for subheading in subheadings:
            subheading_list.append(subheading.string)
        print subheading_list
        return []

    @staticmethod
    def get_table_group(table_row, group_class):
        return table_row.find(class_=group_class).string

    def get_people_data(self):
        tables = self.this.get_tables(self, self.content_id)
        table_data = {}
        for table in tables:
            table_data.update(self.this.get_table_data(self, table))

        return table_data
