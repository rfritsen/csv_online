#workbook_practice2.py

import pandas as pd
import openpyxl
from xlsxwriter import Workbook


l = ['aaa', 'bbb', 'ccc']
s = '\n'.join(l)

# Set dataframe
df = pd.DataFrame([['Load data', 'Ryan', s]], 
     index=['script 1'], columns=['Summary', 'Reporter', 'Description'])

# Set workbook and cell wrapping with xlsxwriter
'''
workbook = Workbook('wrap_text2.xlsx') # Create an new Excel file and add a worksheet.
worksheet = workbook.add_worksheet() 
worksheet.set_column('A:A', 20) # Widen the first column to make the text clearer.

cell_format = workbook.add_format({'text_wrap': True}) # Add a cell format with text wrap on.

worksheet.write('A1', "Line 1\n\nLine 2\n\nLine 3", cell_format)# Write a wrapped string to a cell.
workbook.close()
'''

# Write DF to Excel Pandas
with pd.ExcelWriter('concat_writer.xlsx', engine='xlsxwriter') as writer:
     df3.to_excel(writer, sheet_name='sheet3') # openpyxl

cell_format = workbook.add_format({'text_wrap': True}) # Add a cell format with text wrap on.

worksheet.write('A1', "Line 1\n\nLine 2\n\nLine 3", cell_format)# Write a wrapped string to a cell.
workbook.close()
