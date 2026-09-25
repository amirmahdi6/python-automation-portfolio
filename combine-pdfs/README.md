# Combine PDFs

A Python script that combines PDF files into a single PDF.

## Chapter

Chapter 15 - Working with PDF and Word Documents

## What This Project Does

This script finds PDF files in the current folder, sorts them by filename, and combines their pages into a single PDF file.

The script skips the first page of each input PDF and adds the remaining pages to the output PDF.

## Files

* `combinePdfs.py` - Main Python script
* `01.pdf` - Example input PDF
* `02.pdf` - Example input PDF

## Output

The script creates:

* `allminutes.pdf` - Combined PDF output

## Technologies

* Python
* `PyPDF2`
* File handling
* PDF manipulation

## How to Run

Install the required package:

```bash
pip install PyPDF2
```

Then run:

```bash
python combinePdfs.py
```

Make sure the PDF files are in the same folder as the Python script.
