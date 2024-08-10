import requests
import sqlite3
from bs4 import BeautifulSoup

url = 'https://www.mof.gov.np/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

conn = sqlite3.connect('divisions.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS divisions (
    id INTEGER PRIMARY KEY,
    title TEXT,
    url TEXT
)
''')

links = soup.select('.footer-list li a')

for link in links:
    title = link.text.strip()  
    url = link['href']         

    cursor.execute('''
    INSERT INTO divisions (title, url)
    VALUES (?, ?)
    ''', (title, url))

conn.commit()

conn.close()

print("Data inserted into database successfully.")
