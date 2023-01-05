## Concatenates a CSV file ready to be uploaded to Jira
import csv
file = open("user_stories.csv")

## Testing the commit process

## Grab intake file

## Grab config file 

## Create output file

## read intake column headers

## If config cell = intake column, then add these three(intake column, 2 spaces, intake cell contents) 
# to Dictionary at intake column(?) index

## Write in full spreadsheet, group and concat all dictionary entries based on config cell 

## read 

## read intake column contents

## concatenate related cell contents per config file
# Separate by a new row
# Start contents with header row name (i.e. "Who", "What")

'''
for i in intake_column
2 spaces, i, 
'''

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
        rows.append(row)
rows

file.close()
