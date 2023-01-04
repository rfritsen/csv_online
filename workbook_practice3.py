#workbook_practice3.py
'''not working'''
import pandas as pd
import openpyxl
from xlsxwriter import Workbook

workbook = Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet('test1')
wrap_it = workbook.add_format({'text_wrap': True})

l = ['aaa', 'bbb', 'ccc']
s = '\n'.join(l)

# Set dataframe
df = pd.DataFrame([['Load data', 'Ryan', s]], 
     index=['script 1'], columns=['Summary', 'Reporter', 'Description'])

t = {'A':'1', 'B':'2'}

# cell_format = workbook.add_format({'text_wrap': True}) # Add a cell format with text wrap on.


## Write dataframe with formatting tests
#1 - 
# worksheet.write('A1', "Line 1\n\nLine 2\n\nLine 3", wrap_it) #Works    # Writes an int
worksheet.write('A1', s, wrap_it) # Using s as data
#2 - worksheet.write('A1', s, cell_format) - Works
#3 - worksheet.write('A1', df, cell_format) - error
#4 - 
# worksheet.write('A1:B2', t, wrap_it)
#Experimental ExcelWriter code
#1 - won't write to write_data with openpyxl
#2 - won't write to write_data with xlsxwriter
#3 - Take out ExcelWriter function. Doesn't work
'''
with pd.ExcelWriter('write_data.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='sheet1')
    workbook.add_format({'text_wrap': True})
'''
#Working ExcelWriter code

with pd.ExcelWriter('concat_writer.xlsx', engine='openpyxl') as writer:
     df.to_excel(writer, sheet_name='sheet1')
     workbook.add_format({'text_wrap': True})





workbook.close()

