
import openpyxl
import os

# Open the Excel file
wb = openpyxl.load_workbook('sales.xlsx')
sheet = wb.active

# Store sales values
sales = []

# Loop through every row
for rowNum in range(2, sheet.max_row + 1):
    quantity = sheet.cell(row=rowNum, column=2).value
    price = sheet.cell(row=rowNum, column=3).value

    # Calculate total sales for each product
    total = quantity * price
    sales.append(total)

# Calculate statistics
totalSales = sum(sales)
highestSales = max(sales)
lowestSales = min(sales)
averageSales = totalSales / len(sales)

# Create the report workbook
reportWb = openpyxl.Workbook()
reportSheet = reportWb.active
reportSheet.title = 'Sales Report'

# Write report data
reportSheet['A1'] = 'Metric'
reportSheet['B1'] = 'Value'

reportSheet['A2'] = 'Total Sales'
reportSheet['B2'] = totalSales

reportSheet['A3'] = 'Highest Sales'
reportSheet['B3'] = highestSales

reportSheet['A4'] = 'Lowest Sales'
reportSheet['B4'] = lowestSales

reportSheet['A5'] = 'Average Sales'
reportSheet['B5'] = averageSales

# Save the report
reportWb.save('sales_report.xlsx')

print('Sales report created successfully!')
