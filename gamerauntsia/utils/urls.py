import urllib2
import json

def get_urljson(url):
    stream = []
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    stream = json.load(f)
    return stream