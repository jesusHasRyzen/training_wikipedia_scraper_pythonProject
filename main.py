# it works
import base64

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from base64 import decodebytes
from PIL import Image
from io import BytesIO
# in the form of a string which will be added to the given url
# used to look up quite honestly anything on wikipedia
main = Flask(__name__)


uname = ""
images = ""

if __name__ == '__main__':
    # webSite.debug = True
    main.run()

@main.route('/')
def instructions():
    return render_template('index.html')




@main.route('/loggedIN', methods = ['post'])
def instructions2():
    pws = request.form["psw"]
    urlEncrypt = 'https://realpython-example-app2.herokuapp.com/?username='+pws
    # returnFromRequest = requests.get(urlEncrypt)
    # encryptPW = decode_to_string(returnFromRequest)
    pws = requests.get(urlEncrypt).content
    uname = request.form["uname"]

    urlImages = 'https://team-anything-microservice.herokuapp.com/get_images'
    images = requests.get(urlImages).content
    byte_array = bytes(images)
    images_decoded = base64.decodebytes(byte_array)
    # images_decoded = BytesIO(images_decoded)



    return render_template("loggedIn.html", name = uname, images = images_decoded, pws = pws)

# @main.route('/getImages')
# def instructions3():
#     urlImages = 'https://team-anything-microservice.herokuapp.com/get_images'
#
#     # returnFromRequest = requests.get(urlEncrypt)
#     # encryptPW = decode_to_string(returnFromRequest)
#     return requests.get(urlImages).content

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
            str2 = getLinktoImage(bs4classTemp)
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
    # 	print(item['src'])
    firstImage = images[3]
    return firstImage
def getAllImagesFromUrl(htmlParseData):
    # gets all links in html that are tagged images
    images = htmlParseData.find_all("img")
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


