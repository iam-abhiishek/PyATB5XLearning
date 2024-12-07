class ExcelReader:

    @staticmethod
    def read_from_excel():
        print("reading from excel")

class ReadSQL:

    @staticmethod
    def read_sql():
        print("reading sql file")

class TC1:

    static_var = 25
    def readMyfile(self):
        ExcelReader.read_from_excel()
        ReadSQL.read_sql()
        print(TC1.static_var)

obj_ref = TC1()
obj_ref.readMyfile()