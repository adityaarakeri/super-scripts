import pandas as pd
import openpyxl

wb = openpyxl.load_workbook('File.xlsx')

ws = wb['Sheet1']

df = pd.DataFrame(ws.values)

print("Data:")
print(df)