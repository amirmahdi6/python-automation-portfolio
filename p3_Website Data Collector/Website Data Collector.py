import requests
import bs4
import openpyxl
import time

# Create Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Quotes'

# Create headers
sheet['A1'] = 'Quote'
sheet['B1'] = 'Author'
sheet['C1'] = 'Tags'

rowNum = 2

# Collect data from 3 pages
for pageNum in range(1, 4):

    url = 'https://quotes.toscrape.com/page/' + str(pageNum) + '/'

    print('Collecting page', pageNum)

    try:
        # Send HTTP request
        res = requests.get(url, timeout=20)
        res.raise_for_status()

        # Parse HTML
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find all quote containers
        quotes = soup.select('div.quote')

        for quote in quotes:

            # Get quote text
            text = quote.select_one('.text').text

            # Get author name
            author = quote.select_one('.author').text

            # Get all tags
            tags = quote.select('.tag')
            tagList = []

            for tag in tags:
                tagList.append(tag.text)

            # Save data in Excel
            sheet.cell(row=rowNum, column=1).value = text
            sheet.cell(row=rowNum, column=2).value = author
            sheet.cell(row=rowNum, column=3).value = ', '.join(tagList)

            rowNum += 1

        # Wait before requesting next page
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print('Connection error:', e)
        continue

# Save Excel file
wb.save('quotes.xlsx')

print('All pages collected successfully!')
print('Total quotes collected:', rowNum - 2)