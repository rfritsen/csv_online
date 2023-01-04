#read_in3.py

import pandas as pd
import openpyxl
from xlsxwriter import Workbook

# importing pandas module
import pandas as pd
 
# importing csv from link
df1 = pd.read_excel('book2.xlsx')
print("df1:", df1)
'''
# making copy of team column
new = data["Team"].copy()
'''
b = df1["B"]
# concatenating team with name column
# overwriting name column

df1["A"]= df1["A"].str.cat(b, sep ="\n\n")
print("new df1:" , df1)
df2 = str(df1["A"])
print("df2", df2)

col=0
row=1
i = 0

workbook = Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet('test1')
wrap_it = workbook.add_format({'text_wrap': True})

worksheet.write(row, col, df2, wrap_it)
# row += 1
# i += 1
# worksheet.write(row, col, mplist[i], wrap_it)
workbook.close()

