# Invoice Generator

A Python automation project that reads order information from an Excel spreadsheet and generates invoice documents in PDF format.

## Features

- Reads order data from an Excel file.
- Processes customer and order information.
- Generates PDF invoices automatically.
- Reduces repetitive manual invoice creation.

## Technologies

- Python
- OpenPyXL
- ReportLab

## Project Files

- `Invoice Generator.py`: Main Python script.
- `orders.xlsx`: Input spreadsheet containing order information.

## Requirements

Install the required libraries:

```bash
pip install openpyxl reportlab
```

## How to Run

1. Make sure Python is installed.
2. Install the required libraries.
3. Place `orders.xlsx` in the same directory as the Python script.
4. Run:

```bash
python "Invoice Generator.py"
```

## Output

The script generates PDF invoice documents based on the data in the Excel spreadsheet.

## Purpose

This project demonstrates Excel data processing and automated PDF document generation using Python.