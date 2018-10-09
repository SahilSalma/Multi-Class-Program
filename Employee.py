#Name: Sahil Salma
#Student Number: 201733334

from Person import Person #imports Class Person

class Employee(Person):
    #constructor with parameters for the Person and Employee attributes
    def __init__(self, name = "", address = "", DOB = "", employeeNumber = 0,\
                 dateOfHire = ""):
        super().__init__(name, address, DOB)
        self._employeeNumber = employeeNumber
        self._dateOfHire = dateOfHire
    #accessor Methods
    def getEmployeeNumber (self):
        return self._employeeNumber
    def getDateOfHire (self):
        return self._dateOfHire
    #Mutator Methods 
    def setEmployeeNumber (self,employeeNumber):
        self._employeeNumber = employeeNumber
    def setDateOfHire (self,dateOfHire):
        self._dateOfHire = dateOfHire
    #__repr__ method
    def __repr__(self):
        return self._name + ", born on " + self._DOB + \
               ", has address " + self._address + ", employee number " +\
               self._employeeNumber + ", and was hire on " + self._dateOfHire
