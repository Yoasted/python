from bs4 import BeautifulSoup
import requests
url = input("Enter a website to extract the URL's from: ")
r = requests.get("http://"+url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    #print(link.get('href'))
    print(soup.get_text()) #disabled so text wouldn't be obtained.
