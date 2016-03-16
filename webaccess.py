#C:\Documents\coding
#webaccess.py
#author: Yoast
#version: 1.01
#last accessed: 14/10/15
#Description: Program used to check whether a website can be accessed, so that it can be scraped.

from bs4 import BeautifulSoup
import requests

def menu():
    menuop = input("""
Welcome to the WebCrawler program. What would you like to perform?
1. Input new URL to txt file.
2. View all websites in txt file.
3. Check websites that can can be accessed or not.
4. Crawl a website.
   Choice: """)
    if menuop == "1":
        newUrl()

    elif menuop == "2":
        viewUrls()

    elif menuop == "3":
        webAccess()

    elif menuop == "4":
        spiderCrawl()

    else:
        print("No correct choice inputted, returning to main menu.")
        menu()

def viewUrls():
    topen = open("websites.txt", 'r')
    print(topen.readline




#Function used to see if the websites in a given .txt file
#are able to be accessed or not. Very basic currently.
def webAccess():
    topen = open("websites.txt", 'r')
    try: #In case of an error, using try and exception.
        print("Looking through URLs in .txt file. Will return back to the menu afterwards. \n")
        for x in topen.readlines(): #Goes through the lines in the .txt file and reads them.
            url = x.strip('\n')#Strips any whitespace from the file.
            req = requests.get(url)
            print(url, ": ", req.status_code)#Prints the URL next to the status code.
            topen.close()

        print("\n\n\nReturning to main menu.")
        menu()
            
            
    #Will print the exception error and then return to the main menu.            
    except Exception as e:
        print(e)
        menu()

#Function for the spider.
def spiderCrawl():
    try:
        url = input("Enter a website to extract the URL's from: ")
        r = requests.get("http://"+url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")#Parses the data

        for link in soup.find_all('a'):
            print(link.get('href'))#Gets the links that are inside the 'href' tag. 
            

        menu()

    except Exception as e:
        print(e)
        print("\n\n\Returning back to the menu.  ")
        menu()

    choice = input("Would you like to crawl another website or return to the menu? Type 1 to crawl, any other key to return to menu: ")

    if choice == 1:
        spiderCrawl()

    else:
        menu()

              

    


menu()
