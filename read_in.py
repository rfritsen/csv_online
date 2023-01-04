#read_in.py

import pandas as pd
import openpyxl
from xlsxwriter import Workbook
'''
workbook = Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet('test1')
wrap_it = workbook.add_format({'text_wrap': True})
'''

df1 = pd.read_excel('book2.xlsx')

desc_df = df1.iloc[:,[1,2]] 
print("desc_df: ", desc_df)

iter_list = []
print("iterlist type: ", type(iter_list))
'''
#iterrows practice
for index, col in desc_df.iterrows():
    print("iterrows practice: ", "col0", col[0], "col1",col[1])
'''
#iterrows aggregate


#If I can't pick the columns, can I at least pull them out, aggregate, and put them back in?

#This works. Append each rows to a list
for i in desc_df.index:
    iter_list.append(desc_df['B'][i])
'''
#Experiments and terminal readouts
print("iter_list: ", iter_list)
print( "iter_list type: ", type(iter_list))
for i in df1.index:
    print("df1: ", df1)
for i in df1.index:
'''
 

#Append rows to list, List to String, Join Strings

desc_df = df1.iloc[:,[1,2]] 
print("desc_df: ", desc_df)
desc_list = desc_df.values.tolist()
desc_str = '\n\n'.join([str(elem) for elem in desc_list])   

'''
for index in desc_df.iterrows():
    #agg = '\n\n'.join([str(elem) for elem in desc_df])
    iter_list.append()
print("iter_list agg: ", iter_list)
'''
'''
for index, col in desc_df.iterrows():
    print(".iterrows: ", col[0])
'''
#iterrows to str
'''
'\n\n'.join([str(elem) for elem in desc_list])
'''

desc_list = desc_df.values.tolist()

print("desc_list type: ", type(desc_list))

print("desc_df type: ", type(desc_df))


#desc_df = '\n\n'.join(df1.iloc[:,[1,2]])

#Desc_str should be a list of strings
desc_str = '\n\n'.join([str(elem) for elem in desc_list])
 
print("listToStr Type: ", type(desc_str), "desc_str: ", desc_str)
print("desc_str type: ", type(desc_str))
print("desc_str item type: ", type(desc_str[0]))

full_df = pd.DataFrame([['Summary', 'Ryan', desc_str]], 
     index=['script 1'], columns=['Summary', 'Reporter', 'Description'])

'''
for i in df1.index:
#for i in df1:
    print("agg_list constructor", ','.join(df1))
'''

#dfj = ','.join(df1)

print("df1 Values", df1.values[0])
print("desc_list", desc_list)
#print("agg_list", agg_list)


#Convert read excel data to a dataframe
'''
mp = pd.DataFrame(dataframe1, index=['A', 'B'], columns=['Summary', 'Description'])
mplist = mp.values.tolist()
print(mplist)
print(mplist[0])
#print(mp[m])
#print(mp.loc[0])
 '''

#
# print(df1)