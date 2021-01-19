import requests

# Function to save html data
def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)

# Url that contains language data in FL
url = 'https://en.wikipedia.org/wiki/Demographics_of_Florida#Languages'

# Grab data at that url and save the text
r = requests.get(url)
html = r.text

# write the contents into a file
outF = open("languageHTML.txt", "w")
outF.write(html)
outF.close()
