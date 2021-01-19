import requests
import csv

# URL of census API used
data_url = "https://api.census.gov/data/2018/pep/charagegroups?get=RACE,POP&for=state:12"

# Grab data
r = requests.get(data_url)

# Format in JSON
census_race = r.json()

# Look at unique values for race
chist = {}
print(census_race)
print(" ")
for row in census_race:
    k = row[0]
    chist[k] = row[1]
print(chist)

# ALter race data and store into dictionary
chist = {}
print(census_race)
print(" ")
for row in census_race:
    if row[0] == '0':
        row[0] = "All races"
    if row[0] == '1':
        row[0] = "White"
    if row[0] == '2':
        row[0] = "Black/African American"
    if row[0] == '3':
        row[0] = "Native American/Alaskan Native"
    if row[0] == '4':
        row[0] = "Asian"
    if row[0] == '5':
        row[0] = "Native Hawaiian/Pacific Islander"
    if row[0] == '6':
        row[0] = "Two or More Races"
    if row[0] == '7':
        row[0] = "White"
    if row[0] == '8':
        row[0] = "Black/African American"
    if row[0] == '9':
        row[0] = "Native American/Alaskan Native"
    if row[0] == '10':
        row[0] = "Asian"
    if row[0] == '11':
        row[0] = "Native Hawaiian/Pacific Islander"
    if row[0] != "RACE":
        k = row[0]
        if k in chist.keys():
            chist[k] += int(row[1])
        else:
            chist[k] = int(row[1])

# Write to CSV file
csv_file = "census_race.csv"
with open('census_race.csv', 'w') as f:
    for key in chist.keys():
        f.write("%s,%s\n"%(key,chist[key]))
