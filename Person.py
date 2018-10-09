#Name: Sahil Salma
#Student Number: 201733334

class Person: #new class Person
    #constructor with parameters for each attribute
    def __init__(self,name = "",address = "", DOB = ""):
        self._name = name
        self._address = address
        self._DOB = DOB
    #accessor Methods
    def getName (self):
        return self._name
    def getAddress (self):
        return self._address
    def getDOB (self):
        return self._DOB
    #Mutator Methods 
    def setName (self,name):
        self._name = name
    def setAddress (self,address):
        self._address = address
    def setDOB (self,DOB):
        self._DOB = DOB
    #__repr__ method
    def __repr__(self):
        return self._name + ", born on " + self._DOB + \
               ", and has address " + self._address
    
