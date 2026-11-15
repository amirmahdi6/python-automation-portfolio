# Website Data Collector

A Python web scraping project that collects quotes and related information from a website and saves the extracted data into an Excel spreadsheet.

## Features

- Sends HTTP requests to web pages.
- Extracts website data using BeautifulSoup.
- Collects quotes and related information.
- Saves collected data into an Excel file.
- Handles connection errors during data collection.

## Technologies

- Python
- Requests
- BeautifulSoup
- OpenPyXL

## Project Files

- `Website Data Collector.py`: Main Python script.
- `quotes.xlsx`: Excel file containing collected data.

## Requirements

Install the required libraries:

```bash
pip install requests beautifulsoup4 openpyxl
```

## How to Run

1. Make sure Python is installed.
2. Install the required libraries.
3. Run:

```bash
python "Website Data Collector.py"
```

4. The collected data will be saved in `quotes.xlsx`.

## Purpose

This project demonstrates basic web scraping, data extraction, and Excel file generation using Python.