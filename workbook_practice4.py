#workbook_practice4.py

import pandas as pd
import csv

dict1 = {"number of storage arrays": 45, "number of ports":2390}
l = ['aaa', 'bbb', 'ccc']
s = '\n'.join(l)

df = pd.DataFrame(data=dict1, index=[0])

df = (df.T)

print (df)

df.to_excel('dict1.xlsx')

with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in dict1.items():
        writer.writerow([key, value])