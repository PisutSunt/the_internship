import urllib.request as URLRequest
from bs4 import BeautifulSoup

def item41() :
    url = 'https://theinternship.io/'
    matchCaption, matchImage = ExtractData(url)
    captionList = getCaption(matchCaption)
    imageList = getImgSource(matchImage)
    return getCompany(captionList, imageList)
    
def printCompany(company) :
    for itr in company :
        print(itr[1])

def ExtractData(url) :
    rawData = URLRequest.urlopen(url)
    page = BeautifulSoup(rawData, 'html.parser')
    matchCaption = page.findAll('span', attrs={'class': 'list-company'})
    matchImage = page.findAll('img', attrs={'class': 'center-logos'})
    return matchCaption, matchImage

def getCaption(matchCaption) :
    captionList = []
    for cap in matchCaption :
        captionList.append(str(cap))
    return captionList

def getImgSource(matchImage) :
    imageList = []
    for img in matchImage :
        imageList.append(str(img['src']))
    return imageList

def sortCompany(e) :
    return len(e[0])

def getCompany(captionList, imageList) :
    company =[]
    for i in range(len(captionList)) :
        company.append([captionList[i], imageList[i]])
    company.sort(key=sortCompany)
    return company

printCompany(item41())