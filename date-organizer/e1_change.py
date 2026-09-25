import shutil
import os
import re
datePattern = re.compile(r'''^(.*?)   
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
''', re.VERBOSE)
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo is None:
        continue
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)
    euroFilename = f'{before}{day}-{month}-{year}{after}'
    print(f'Renaming {amerFilename} -> {euroFilename}')
    shutil.move(amerFilename, euroFilename)