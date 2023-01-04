# workbook_practice5.py

import pandas as pd
import openpyxl
from xlsxwriter import Workbook

workbook = Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet('test1')
wrap_it = workbook.add_format({'text_wrap': True})

l = [['aaa\nddd', '3333\n7777'], ['bbb'], ['ccc']]
n = [['aaa\nddd', '3333\n7777'], 'bbb', 'ccc']

m = ['xxx\nyyy', 'z', 'a', 'b']
p = ['ppp\nqqq', 'r', 's', 't']


# This works to change a dataframe into a series of lists that can be read to an excel sheet

mp = pd.DataFrame([m, p], index=['A', 'B'], columns=['1', '2', '3', '4'])



print(mp.loc[['A']])
print(type(mp.loc[['A']]))
mplist = mp.values.tolist()
print("mplist: ", mplist)
print("mplist type: ", type(mplist))
'''
print(mplist[0])
#print(mp[m])
#print(mp.loc[0])
'''

col=0
row=1
i = 0

# This works. Writes from a list of lists to an excel
''''''
worksheet.write_row(row, col, mplist[i], wrap_it)
row += 1
i += 1
worksheet.write_row(row, col, mplist[i], wrap_it)
workbook.close()


# s = '\n'.join(l)

# Set dataframe
'''
df = pd.DataFrame([['Load data', 'Ryan', s]], 
     index=['script 1'], columns=['Summary', 'Reporter', 'Description'])
     '''
# This works, writes from lists
'''
worksheet.write_row(row,col, m, wrap_it)
row += 1
worksheet.write_row(row, col, p, wrap_it)
workbook.close()
'''
'''
#Write from dataframe
worksheet.write_row(row, col, m, wrap_it)
workbook.close()
  '''  