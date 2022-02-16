import urllib.request as urllib2

airport = "ENGM"
url = ""

#YYYYMMDDHHMMSS
start = "20220201000000"
end = "20220202000000"

fname = ""
filename = fname.join([airport,start]) 


def buildUrl():
    urlDone = url.join(["http://www.ogimet.com/cgi-bin/getmetar?icao=", airport, "&begin=", start, "&end=", end, ""])
    return urlDone

urllib2.urlretrieve(buildUrl(),  filename)