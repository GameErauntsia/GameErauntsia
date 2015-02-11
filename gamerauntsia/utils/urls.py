import urllib2
import xmltodict
import json

def get_urljson(url):
    stream = []
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    stream = json.load(f)
    return stream

def get_urlxml(url):
    stream = []
    raw_data = urllib2.urlopen(url)
    data = raw_data.read()
    raw_data.close()
    stream = xmltodict.parse(data)
    return stream