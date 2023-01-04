from xlsxwriter import Workbook

# Create an new Excel file and add a worksheet.

workbook = Workbook('wrap_text2.xlsx')

worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.

worksheet.set_column('A:A', 20)

# Add a cell format with text wrap on.

cell_format = workbook.add_format({'text_wrap': True})

# Write a wrapped string to a cell.

worksheet.write('A1', "Line 1\n\nLine 2\n\nLine 3", cell_format)

workbook.close()