import urllib.request as urlRequest

airport = "ENBO"
url = ""

#YYYYMMDDHHMMSS
start = "20220223000000"
end = "20220224000000"
extension = ".csv"

fname = ""
filename = fname.join([airport,start,extension]) 


def buildUrl():
    urlDone = url.join(["http://www.ogimet.com/cgi-bin/getmetar?icao=", airport, "&begin=", start, "&end=", end, ""])
    return urlDone

urlRequest.urlretrieve(buildUrl(),  filename)
