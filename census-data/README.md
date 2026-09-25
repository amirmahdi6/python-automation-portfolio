# Census Data

A Python project that reads population data from an Excel spreadsheet and organizes it by state and county.

## Chapter

Chapter 13 - Working with Excel Spreadsheets

## What This Project Does

The script reads census data from an Excel workbook, processes the rows, and calculates the total population and number of census tracts for each county.

The processed data is then saved as a Python file.

## Files

* `E1_readcensusExcel.py` - Reads and processes the Excel data
* `censuspopdata.xlsx` - Input Excel workbook
* `census2010.py` - Generated Python data file containing the processed results

## Technologies

* Python
* `openpyxl`
* Excel
* Dictionaries
* File handling

## How to Run

Install the required package:

```bash
pip install openpyxl
```

Make sure `censuspopdata.xlsx` is in the same folder as the Python script.

Then run:

```bash
python E1_readcensusExcel.py
```

The script will process the workbook and generate `census2010.py`.
