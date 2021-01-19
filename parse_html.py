
from bs4 import BeautifulSoup

# Read html file containing census info
inF = open("languageHTML.txt", "r")
data = inF.read()
inF.close()

# Isolate Languages in Florida
div1 = data.split("<caption><b>Top Languages in Florida</b>")
div2 = div1[1].split("</td></tr></tbody></table>")

# View each value in the table as individual strings
lines = div2[0].split("\n")
for line in lines:
        print(line)

# Use beautiful soup to parse html
soup = BeautifulSoup(div2[0], 'html.parser')

# Extract the lines containing td
lines = soup.find_all('td')

# create list called lang and populate with parsed data
lang = []
for line in lines:
    lang.append(line.get_text().replace("%\n","").replace(",",""))

# Clean data to match SNAP data and populate dictionary
i = 0
ldict = {}
for key in lang:
    if i%2 == 0:
        if (key != "English" and key != "Spanish"):
            key = "Other"
        if key in ldict.keys():
            ldict[key] += float(lang[i+1])
        else:
            ldict[key] = float(lang[i+1])
    i +=1

print(ldict)
# write into csv
csv_file = "census_language.csv"
with open('census_language.csv', 'w') as f:
    for key in ldict.keys():
        f.write("%s,%s\n"%(key,ldict[key]))
