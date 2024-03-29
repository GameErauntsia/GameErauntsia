import urllib.request as urllib2
import xmltodict
import json


def get_urljson(url):
    obj = {}
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req, timeout=1)
    try:
        obj = json.loads(f.read().decode())
    except:
        return None
    return obj


def get_urlxml(url):
    stream = []
    raw_data = urllib2.urlopen(url, timeout=1)
    data = raw_data.read()
    raw_data.close()
    stream = dict(xmltodict.parse(data))
    return stream
