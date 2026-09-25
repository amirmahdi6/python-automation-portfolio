# textToSpreadsheet.py
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

filenames = ['file1.txt', 'file2.txt', 'file3.txt']

for colIdx, filename in enumerate(filenames, start=1):
    with open(filename) as f:
        lines = f.readlines()
    for rowIdx, line in enumerate(lines, start=1):
        sheet.cell(row=rowIdx, column=colIdx).value = line.strip()

wb.save('textToSheet.xlsx')