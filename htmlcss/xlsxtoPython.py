import pandas as pd

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 300)

def readDataFromExcel():
        data = pd.read_excel(r'C:\Users\Intern\PycharmProjects\mysite\media\Datasheet.xlsx', sheet_name="Sheet1")

        data1 = list(data['ID'])
        data2 = list(data['Name'])
        data3 = list(data['DOB'])
        print(data1)
        return data1, data2, data3

