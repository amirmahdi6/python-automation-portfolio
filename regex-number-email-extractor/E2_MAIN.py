import re
import pyperclip
text=pyperclip.paste()
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)
phoneMatches=phoneRegex.findall(text)
phoneNumbers=[]
for groups in phoneMatches:
    phoneNum=groups[0]
    phoneNumbers.append(phoneNum)

# EMAIL

emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z.-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)
emailMatches=emailRegex.findall(text)
emailAddresses=[]
for groups in emailMatches:
    emailAddresses.append(groups[0])

matchs=[]
if phoneNumbers:
    matchs.append('Phone Numbers:')
    matchs.extend(phoneNumbers)
if emailAddresses:
    matchs.append('Email Addresses:')
    matchs.extend(emailAddresses)
if not matchs:
    matchs.append('No phone Number or email addresses found')

result='\n'.join(matchs)
pyperclip.copy(result)
print(result)