#jira_stories.py

import pandas as pd
import openpyxl
from xlsxwriter import Workbook

workbook = Workbook('jira_upload.xlsx')
worksheet = workbook.add_worksheet('sheet1')
wrap_it = workbook.add_format({'text_wrap': True})
row = 0
col = 1

#Read User Stories into database
pd.read_excel('LSS Manager Review_MBB User Stories.xlsx')
#Convert Headers from User Stories into Indexes
pd.read_excel()

#Combine Description fields into one list and separate by 

#Turn database into a list of lists. Each list is one row for the OUTPUT FILE
desc_list = desc_df.values.tolist()
#Turn list of lists into a list of list of strings
desc_str = '\n\n'.join([str(elem) for elem in desc_list])

#Write list of lists of strings to Excel
worksheet.write_row(row, col, mplist[i], wrap_it)
row += 1
i += 1
worksheet.write_row(row, col, mplist[i], wrap_it)
workbook.close()