from collapse import Collapse


class Aboriginal(Collapse):
    def __init__(self, code):
        super(Aboriginal, self).__init__(code)
        self.this = Aboriginal
        self.content_id = "INGPContent"

    def get_aboriginal_data(self):
            tables = self.this.get_tables(self, self.content_id)
            table_data = {}
            for table in tables:
                table_data.update(self.this.get_table_data(self, table))

            return table_data
