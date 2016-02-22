from time import time
from datetime import datetime
import string

def time_slug():
    """ """
    return int(time())
    
def time_slug_long():
    """ """
    return int(time()*1000)

def time_slug_string():
    """ """
    return str(time_slug_long())

def date_from_timeslug(t):
    """ """    
    return datetime.fromtimestamp(float(t))    

