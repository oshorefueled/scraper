from collapse import Collapse


class Dwellings(Collapse):
    def __init__(self, code):
        super(Dwellings, self).__init__(code)
        self.this = Dwellings
        self.content_id = "dwellingContent"

    def get_dwellings_data(self):
            tables = self.this.get_tables(self, self.content_id)
            table_data = {}
            for table in tables:
                table_data.update(self.this.get_table_data(self, table))

            return table_data
