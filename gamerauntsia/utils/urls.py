import urllib
import xmltodict
import json

def get_urljson(url):
    stream = []
    req = urllib.Request(url)
    opener = urllib.build_opener()
    f = opener.open(req, timeout=1)
    try:
        stream = json.load(f)
    except:
        return None
    return stream

def get_urlxml(url):
    stream = []
    raw_data = urllib.urlopen(url, timeout=1)
    data = raw_data.read()
    raw_data.close()
    stream = dict(xmltodict.parse(data))
    return stream
