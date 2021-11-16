# it works
import base64

import logging
from http.client import HTTPConnection

log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)
HTTPConnection.set_debuglevel(1)
# to make a request in order to obtain data from wiki
import requests


#imported beautifulSoup to help parse the data getting passed when
# user makes request in json format
from bs4 import BeautifulSoup


#imported flask to work with the deploying the program online.
from flask import Flask, render_template, request
import json


main = Flask(__name__)


images = ""

if __name__ == '__main__':
    # webSite.debug = True
    main.run()


# call the initial page when opened on webpage
# will open with an image stating request, no buttons or any interaction
@main.route('/')
def instructions():
    return render_template('index.html')

# post requests takes in data in the form of json
# first it checks if the requests was made via post
# then gets the input and stores it in str2
# creates wikipedia url for the input
# gets data from the created url and parse the data with BeautifulSoup
# then obtains the img src from the parse data
@main.route('/' , methods =['post'])

def returnUrlofImage():
    str2 = "ME"
    if request.method == 'POST':
        request_data = request.get_json()
        str2 = request_data['input']
        wikiUrl = convertStr2Url(str2)
        parseDataFromWiki = getParseDatafromUrl(wikiUrl)
        htmltagImage = getAllImagesFromUrl(parseDataFromWiki)

        bs4classTemp = getImageData(parseDataFromWiki)
        doesExist = testIfImagesExist(htmltagImage)
        if doesExist:
            str2 = getLinktoImage(bs4classTemp, str2)
            return str2
    return "does not exist"


def convertStr2Url(inputString):
    # create url with added string at the end
    wikiUrl = "https://en.wikipedia.org/wiki/" + inputString
    return wikiUrl
def getParseDatafromUrl(url):
    # here we get the websites url
    page = requests.get(url)
    # scrape webpage
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
def getImageData(htmlParseData):
    # gets all links in html that are tagged images
    images = htmlParseData.find_all("img")
    # goes thru the images link saved and gets the source the images
    # for loop to go thru all the list saved.
    # for item in images:
    firstImage = images[3]
    return firstImage
def getAllImagesFromUrl(htmlParseData):
    # gets all links in html that are tagged images

    images = htmlParseData.find_all("img")
    # goes thru the images link saved and gets the source the images
    # for loop to go thru all the list saved.
    # for item in images:
    # 	print(item['src'])
    # firstImage = images[3]
    firstImage = images
    # convert the class bs4.element.tag into a string
    stringOfhtmlTag = str(firstImage)
    return stringOfhtmlTag
def testIfImagesExist(link):
    # look to see if a image link even exist else return string with no image
    if "src" not in link:
        return False
    return True
def getLinktoImage(firstLink):
    # get the link information of link leading to the image associated with input
    firstImageStr = firstLink.get("src")
    firstImageStr = str(firstImageStr)
    # if link does not include https:, then include it to make it a complete link
    firstImageStr = "https:" + firstImageStr
    # display the output below
    return firstImageStr


