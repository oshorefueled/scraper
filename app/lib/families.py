from collapse import Collapse


class Families(Collapse):
    def __init__(self, code):
        super(Families, self).__init__(code)
        self.this = Families
        self.content_id = "familyContent"

    def get_families_data(self):
            tables = self.this.get_tables(self, self.content_id)
            table_data = {}
            for table in tables:
                table_data.update(self.this.get_table_data(self, table))

            return table_data
