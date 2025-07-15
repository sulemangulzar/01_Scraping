from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')
table = soup.find_all('table')[1]

titles = table.find_all("th")
columns = [t.text.strip() for t in titles]

df = pd.DataFrame(columns=columns)

rows = table.find_all('tr')[1:] 

for row in rows:
    cells = row.find_all('td')
    if len(cells) == 0:
        continue

    data = [cell.text.strip() for cell in cells]
    if len(data) == len(columns):
        df.loc[len(df)] = data

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(df.to_string())


print(df.head())
