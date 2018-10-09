#Name: Sahil Salma
#Student Number: 201733334

from Employee import Employee #imports Class Employee

class Staff(Employee): #new class Staff with super class Employee
    #constructor with parameters for the Person, Employee and Staff attributes
    def __init__(self, name = "", address = "", DOB = "", employeeNumber = 0, \
                 dateOfHire = "", jobTitle = "", department = "", \
                 hourlySalary = 0, status = ""): 
        super().__init__(name, address, DOB, employeeNumber, dateOfHire)
        self._jobTitle = jobTitle 
        self._department = department
        self._hourlySalary = hourlySalary
        self._status = status
    #accessor Methods
    def getJobTitle (self):
        return self._jobTitle
    def getDepartment (self):
        return self._department
    def getHourlySalary (self):
        return self._hourlySalary
    def getStatus (self):
        return self._status
    #Mutator Methods 
    def setJobTitle (self,jobTitle):
        self._jobTitle = jobTitle
    def setDepartment (self,department):
        self._department = department
    def setHourlySalary (self,hourlySalary):
        self._hourlySalary = hourlySalary
    def setStatus (self,status):
        self._status = status
    #__repr__ method
    def __repr__(self):
        return self._name + ", born on " + self._DOB + \
               ", has address " + self._address + ", employee number " +\
               str(self._employeeNumber) + ", is a staff in department " +\
               self._department + ", with job title of " + self._jobTitle +\
               ", was hired on " + self._dateOfHire + " has hourly salary $" +\
               str(self._hourlySalary) + " and is a " + self._status + " employee."

