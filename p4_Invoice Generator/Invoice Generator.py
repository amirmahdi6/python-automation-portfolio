
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Open Excel file
wb = openpyxl.load_workbook('orders.xlsx')
sheet = wb.active

customer = sheet.cell(row=2, column=1).value

# Create PDF
pdf = canvas.Canvas('invoice.pdf', pagesize=letter)

# Write invoice title
pdf.setFont('Helvetica-Bold', 20)
pdf.drawString(50, 750, 'INVOICE')

pdf.setFont('Helvetica', 12)
pdf.drawString(50, 715, 'Customer: ' + str(customer))

# Write table headers
pdf.drawString(50, 675, 'Product')
pdf.drawString(250, 675, 'Qty')
pdf.drawString(320, 675, 'Price')
pdf.drawString(410, 675, 'Total')

rowY = 650
grandTotal = 0

# Read products
for rowNum in range(2, sheet.max_row + 1):
    product = sheet.cell(row=rowNum, column=2).value
    quantity = sheet.cell(row=rowNum, column=3).value
    price = sheet.cell(row=rowNum, column=4).value

    total = quantity * price
    grandTotal += total

    pdf.drawString(50, rowY, str(product))
    pdf.drawString(250, rowY, str(quantity))
    pdf.drawString(320, rowY, '$' + str(price))
    pdf.drawString(410, rowY, '$' + str(total))

    rowY -= 25

# Write grand total
pdf.setFont('Helvetica-Bold', 14)
pdf.drawString(320, rowY - 20, 'Grand Total: $' + str(grandTotal))

# Save PDF
pdf.save()

print('Invoice created successfully!')
