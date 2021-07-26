# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import pathlib
import pprint
import csv

desktop = pathlib.Path().home().joinpath("Desktop")
items = {}

for item in desktop.iterdir():
     suffix = item.suffix
     if suffix in items:
          items[suffix] += 1
     else:
          items[suffix] = 1
     
pprint.pprint(items)

with open('file_counts.csv', 'w') as csvfile:
     write_out = csvfile.write(str(items))
     # reader = csv.DictReader(csvfile, fieldnames=['Folder', 'app', 'Document', 'EXE', 'JPEG', 'MOV', 'MP4', 'PDF', 'PNG', 'SH', 'Excel'])
     # counts = list(reader)
     # print(counts)