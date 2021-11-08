import requests
from bs4 import BeautifulSoup
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# get request and add string to end of url
inputString = "CAT"
# create url with added string at the end
wikiUrl = "https://en.wikipedia.org/wiki/" + inputString
# here we get the websites url
page = requests.get(wikiUrl)

# display status code to make sure it worked or if it crashed
print(page.status_code)

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

#gets all links in html that are tagged images
images = soup.find_all("img")

#goes thru the images link saved and gets the source the images
#for loop to go thru all the list saved.
# for item in images:
# 	print(item['src'])
firstImage = images[3]
# convert the class bs4.element.tag into a string
stringOfhtmlTag = str(firstImage)
# look to see if a image link even exist else return string with no image
if "src" not in stringOfhtmlTag:
    print("no image")
# get the link information of link leading to the image associated with input
firstImageStr = str(firstImage.get("src"))
# if link does not include https:, then include it to make it a complete link
firstImageStr = "https:" + firstImageStr
# display the output below
print(firstImageStr)
