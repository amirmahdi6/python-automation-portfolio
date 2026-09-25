# Generate Invitations

A Python script that generates personalized invitation letters in a Word document.

## Chapter

Chapter 15 - Working with PDF and Word Documents

## What This Project Does

The script reads guest names from a text file and creates a Word document containing a separate invitation for each guest.

Each invitation is placed on a new page.

## Files

* `generateInvitations.py` - Main Python script
* `guests.txt` - Text file containing guest names

## Output

The script creates:

* `invitations.docx` - Generated Word invitation document

## Technologies

* Python
* `python-docx`
* Word document generation
* Text file handling

## How to Run

Install the required package:

```bash
pip install python-docx
```

Then run:

```bash
python generateInvitations.py
```

Make sure `guests.txt` is in the same folder as the Python script.
