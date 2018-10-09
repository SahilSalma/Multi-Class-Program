#Name: Sahil Salma
#Student Number: 201733334

from Employee import Employee #imports Class Employee

class Doctor(Employee):
    #constructor with parameters for the Person, Employee and Doctor attributes
    def __init__(self, name = "", address = "", DOB = "", employeeNumber = "", \
                 dateOfHire = "", annualSalary = "", specialty = "", \
                 numberOfPatients = ""):
        super().__init__(name, address, DOB, employeeNumber, dateOfHire)
        self._annualSalary = annualSalary
        self._specialty = specialty
        self._numberOfPatients = numberOfPatients
    #accessor Methods
    def getAnnualSalary (self):
        return self._annualSalary
    def getSpecialty (self):
        return self._specialty
    def getNumberOfPatients (self):
        return self._numberOfPatients
    #Mutator Methods
    def setAnnualSalary (self,annualSalary):
        self._annualSalary = annualSalary
    def setSpecialty (self,specialty):
        self._specialty = specialty
    def setNumberOfPatients (self,numberOfPatients):
        self._numberOfPatients = numberOfPatients
    #__repr__ method
    def __repr__(self):
        return self._name + ", born on " + self._DOB + \
               ", has address " + self._address + ", employee number " +\
               self._employeeNumber + " is a doctor with specialty " +\
               self._specialty + ", and was hire on " + self._dateOfHire +\
               " has annual salary $" + self._annualSalary + " and " +\
               self._numberOfPatients + " patients."

