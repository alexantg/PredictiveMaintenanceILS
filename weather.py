import urllib.request as urllib2

airport = "ENBO"
url = ""

#YYYYMMDDHHMMSS
start = "20220223000000"
end = "20220224000000"

fname = ""
filename = fname.join([airport,start]) 


def buildUrl():
    urlDone = url.join(["http://www.ogimet.com/cgi-bin/getmetar?icao=", airport, "&begin=", start, "&end=", end, ""])
    return urlDone

urllib2.urlretrieve(buildUrl(),  filename)
