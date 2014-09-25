from urlparse2 import urlparse
import urllib2
import json

def get_parsed_url(url):
    """ """
    if url:
        return urlparse(url)
    else:
        return url
    
def get_domain(url):

    hostname = get_parsed_url(url).hostname
    if hostname and hostname.startswith('www.'):
        hostname = hostname[4:]
    return hostname

def get_urljson(url):
    stream = []
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    stream = json.load(f)
    return stream