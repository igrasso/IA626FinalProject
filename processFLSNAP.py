# File to process Florida SNAP data

#T his assignment used code from file: 2 - nested and table data.html
import csv
import operator

#load data
#load data
with open('snap_data.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

# Clean ethnicity column
i = 0
for row in data:
    if row['ethnicity'] == "asian":
        row['ethnicity'] = "Asian"
    if row['ethnicity'] == "black":
        row['ethnicity'] == "Black/African American"
    if row['ethnicity'] == "hispanic-black":
        row['ethnicity'] = "Black/African American"
    if row['ethnicity'] == "hispanic-white":
        row['ethnicity'] = "White"
    if row['ethnicity'] == "caucasian":
        row['ethnicity'] = "White"
    if row['ethnicity'] == "caucasion":
        row['ethnicity'] = "White"
    if row['ethnicity'] == "Native American and Alaskan Native":
        row['ethnicity'] = "Native American/Alaskan Native"
    if row['ethnicity'] == "Native American":
        row['ethnicity'] = "Native American/Alaskan Native"
    if row['ethnicity'] == "white":
        row['ethnicity'] = "White"
    if row['ethnicity'] == "African American":
        row['ethnicity'] = "Black/African American"
    if row['ethnicity'] == "black":
        row['ethnicity'] = "Black/African American"

# Create dictionary of frequency for race
ehist = {}
for row in data:
    k = row['ethnicity']
    if k in ehist.keys():
        ehist[k] += 1
    else:
        ehist[k] = 1
print(ehist)


# Create dictionary of primary language spoken
lhist = {}
for row in data:
    k = row['primary_language']
    if k in lhist.keys():
        lhist[k] += 1
    else:
        lhist[k] = 1
print(lhist)
