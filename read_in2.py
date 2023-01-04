#read_in2.py

import pandas as pd
import openpyxl
from xlsxwriter import Workbook

#Append rows to list, List to String, Join Strings

df1 = pd.read_excel('book2.xlsx')

##Pull Out Description
#Subset of df for second and third columns
desc_df = df1.iloc[:,[1,2]] 
print("desc_df: ", desc_df)
#Rows to list
desc_list = desc_df.values.tolist()
print("desc_list:", desc_list)
#List to Str
desc_str = '\n\n'.join([str(elem) for elem in desc_list]) 
print("desc_str: ", desc_str)  
print("str type: ", type(desc_str))

## Put description back into dataframe? Or do it as a list?
## Write the dataframe into excel

df2 = pd.DataFrame([['Load data', 'Ryan', desc_list]], 
     index=['script 1'], columns=['Summary', 'Reporter', 'Description'])

print("df2: ", df2)

'''
# Write to excel for formatting with ExcelWriter Pandas
with pd.ExcelWriter('read_in2.xlsx', engine='xlsxwriter') as writer:
     df2.to_excel(writer, sheet_name='sheet1') # openpyxl
     '''

# Write to Excel for formatting with xlsxwriter

col=0
row=0
i = 0

workbook = Workbook('read_in2.xlsx')
worksheet = workbook.add_worksheet('sheet1')
wrap_it = workbook.add_format({'text_wrap': True})
'''
worksheet.write_row(row, col, desc_str[i], wrap_it)
row += 1
i += 1
worksheet.write_row(row, col, desc_str[i], wrap_it)
'''

worksheet.write_string(row, col, desc_list, wrap_it)
row += 1
i += 1
worksheet.write_string(row, col, desc_list, wrap_it)

workbook.close()