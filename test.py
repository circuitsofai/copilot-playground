# write recursive function to crawl the web

import urllib2
import re

def getLinks(url):
    html_page = urllib2.urlopen(url)
    html_text = html_page.read()
    regex = '<a href="(.*?)">'
    pattern = re.compile(regex)
    links = re.findall(pattern, html_text)
    return links

def crawlWeb(url, maxPages):
    pagesToVisit = [url]
    numberVisited = 0
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        try:
            print(numberVisited, "Visiting:", url)
            links = getLinks(url)
            for link in links:
                if link not in pagesToVisit:
                    pagesToVisit.append(link)
        except:
            print("Could not open:", url)
    print("Finished!")

crawlWeb("http://www.google.com", 10)

# Path: test.py
# write recursive function to crawl the web

import urllib2
import re

def getLinks(url):
    html_page = urllib2.urlopen(url)
    html_text = html_page.read()
    regex = '<a href="(.*?)">'
    pattern = re.compile(regex)
    links = re.findall(pattern, html_text)
    return links

def crawlWeb(url, maxPages):

    pagesToVisit = [url]
    numberVisited = 0
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        try:
            print(numberVisited, "Visiting:", url)
            links = getLinks(url)
            for link in links:
                if link not in pagesToVisit:
                    pagesToVisit.append(link)
        except:
            print("Could not open:", url)
    print("Finished!")

crawlWeb("http://www.google.com", 10)
