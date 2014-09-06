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
        self.raw = f.read()
    
    def setAbstract(self, abst):
        self.abstract = abst
    
    def setBody(self, body):
        self.body = body
    
    def getFrequency(self, word):
        return 666