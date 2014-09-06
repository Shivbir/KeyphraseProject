'''
Created on Sep 5, 2014

@author: randall
'''

class Document:
    '''
    classdocs
    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        f = open(fileName)
        raw = f.read()