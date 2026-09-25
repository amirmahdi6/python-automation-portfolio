# Excel to CSV

A Python script that converts Excel spreadsheets into CSV files.

## Chapter

Chapter 16 - Working with CSV Files and JSON Data

## What This Project Does

The script finds Excel `.xlsx` files in the current folder and converts each worksheet into a separate CSV file.

Each CSV file contains the data from one Excel worksheet.

## Files

* `excelToCsv.py` - Main Python script
* `example.xlsx` - Example Excel input file

## Output

For each worksheet, the script creates a CSV file.

For example:

* `example_Sheet1.csv`
* `example_Sheet2.csv`

## Technologies

* Python
* `openpyxl`
* `csv`
* File handling

## How to Run

Install the required package:

```bash id="p3h2n8"
pip install openpyxl
```

Then run:

```bash id="c7v4mz"
python excelToCsv.py
```

Make sure the Excel files are in the same folder as the Python script.
