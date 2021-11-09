import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
# server side post request method to be used to recieve data
# in the form of a string which will be added to the given url
# used to look up quite honestly anything on wikipedia
main = Flask(__name__)

if __name__ == '__main__':
    # webSite.debug = True
    main.run()

@main.route('/')
def instructions():
    return render_template('index.html')

@main.route('/' , methods =['post'])
def returnUrlofImage():
    if request.method == 'POST':
        str2 = request.form.get("input")
        return type(str2)
        wikiUrl = convertStr2Url(request.form['input'])
        parseDataFromWiki = getParseDatafromUrl(wikiUrl)
        htmltagImage = getAllImagesFromUrl(parseDataFromWiki)
        doesExist = testIfImagesExist(htmltagImage)
        print("comes down to check if the image exist")
        return "post"
        if doesExist:
            return getLinktoImage(htmltagImage)
    print("makes it to the last return")
    return "does not exist"


def convertStr2Url(inputString):
    # create url with added string at the end
    wikiUrl = "https://en.wikipedia.org/wiki/" + inputString
    return wikiUrl
def getParseDatafromUrl(url):
    # here we get the websites url
    page = requests.get(url)
    # display status code to make sure it worked or if it crashed
    print(page.status_code)
    # scrape webpage
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
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
        print("no image")
        return False
    return True
def getLinktoImage(firstLink):
    # get the link information of link leading to the image associated with input
    firstImageStr = str(firstLink.get("src"))
    # if link does not include https:, then include it to make it a complete link
    firstImageStr = "https:" + firstImageStr
    # display the output below
    return firstImageStr

# get request and add string to end of url
inputString = "jesus"


