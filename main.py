import requests
from bs4 import BeautifulSoup
from flask import Flask, request
# server side post request method to be used to recieve data
# in the form of a string which will be added to the given url
# used to look up quite honestly anything on wikipedia
main = Flask(__name__)

@main.route('/')
def instructions():
    return "Hi"

@main.route("/" , method=['POST'])
def _returnUrlofImage():
    wikiUrl = convertStr2Url(request.form['input'])
    parseDataFromWiki = getParseDatafromUrl(wikiUrl)
    htmltagImage = getAllImagesFromUrl(parseDataFromWiki)
    doesExist = testIfImagesExist(htmltagImage)
    if doesExist:
        return getLinktoImage(htmltagImage)
    return "does not exist"


def convertStr2Url(inputString):
    # create url with added string at the end
    wikiUrl = "https://en.wikipedia.org/wiki/" + inputString
    return wikiUrl
def getParseDatafromUrl(url):
    # here we get the websites url
    page = requests.get(wikiUrl)
    # display status code to make sure it worked or if it crashed
    print(page.status_code)
    # scrape webpage
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
def getAllImagesFromUrl(htmlParseData):
    # gets all links in html that are tagged images
    images = soup.find_all("img")
    # goes thru the images link saved and gets the source the images
    # for loop to go thru all the list saved.
    # for item in images:
    # 	print(item['src'])
    firstImage = images[3]
    # convert the class bs4.element.tag into a string
    stringOfhtmlTag = str(firstImage)
    return stringOfhtmlTag
def testIfImagesExist(link):
    # look to see if a image link even exist else return string with no image
    if "src" not in stringOfhtmlTag:
        print("no image")
        return False
    return True
def getLinktoImage(firstLink):
    # get the link information of link leading to the image associated with input
    firstImageStr = str(firstImage.get("src"))
    # if link does not include https:, then include it to make it a complete link
    firstImageStr = "https:" + firstImageStr
    # display the output below
    return firstImageStr

# get request and add string to end of url
inputString = "jesus"


