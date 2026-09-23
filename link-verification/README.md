# Link Verification

A Python automation script that extracts links from a webpage and checks whether they are accessible.

## Features

* Extracts links from a webpage using BeautifulSoup.
* Converts relative URLs into absolute URLs.
* Checks only HTTP and HTTPS links.
* Removes duplicate URLs.
* Checks links using HTTP requests.
* Follows redirects.
* Reports working and broken links.
* Handles request errors and timeouts.

## Technologies

* Python
* Requests
* BeautifulSoup
* urllib.parse

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python link_verification.py
```

The script checks the links found on the configured webpage and displays their HTTP status.

Example:

```text
OK (200): https://example.com/
Broken (404): https://example.com/missing-page
```

## Project Structure

```text
link-verification/
├── link_verification.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Purpose

This project was built as a practical Python automation exercise to work with web scraping, HTTP requests, URL handling, and error handling.
