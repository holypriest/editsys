from datetime import *

def str_to_date(datestring):
    '''Receives a date formatted string and return a date object'''
    return datetime.strptime(datestring, '%Y-%m-%d').date()
