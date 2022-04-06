import urllib.request as urlRequest

airport = "ENBO"
url = ""

#YYYYMMDDHHMMSS
start = "20220132155000"
end = "20220132155000"
extension = ".csv"

fname = ""
filename = fname.join([airport,start,extension]) 


def buildUrl():
    urlDone = url.join(["http://www.ogimet.com/cgi-bin/getmetar?icao=", airport, "&begin=", start, "&end=", end, ""])
    return urlDone

urlRequest.urlretrieve(buildUrl(),  filename)
