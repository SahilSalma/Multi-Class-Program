#Name: Sahil Salma
#Student Number: 201733334

from Person import Person #imports Class Person

class Patient(Person):
    #constructor with parameters for the Person and Patient attributes
    def __init__(self,name = "",address = "", DOB = "", MCP = 0,\
                 dateOfAdmission = "", hospital = "", doctorName = "",\
                 roomNumber = 0):
        super().__init__(name, address, DOB)
        self._MCP = MCP
        self._dateOfAdmission = dateOfAdmission
        self._hospital = hospital
        self._doctorName = doctorName
        self._roomNumber = roomNumber
    #accessor Methods
    def getMCP (self):
        return self._MCP
    def getDateOfAdmission (self):
        return self._dateOfAdmission
    def getHospital (self):
        return self._hospital
    def getDoctorName (self):
        return self._doctorName
    def getRoomNumber (self):
        return self._roomNumber
    #Mutator Methods 
    def setMCP (self,MCP):
        self._MCP = MCP
    def setDateOfAdmission (self,dateOfAdmission):
        self._dateOfAdmission = dateOfAdmission
    def setHospital (self,hospital): 
        self._hospital = hospital
    def setDoctorName (self,doctorName):                             
        self._doctorName = doctorName
    def setRoomNumber (self,roomNumber):                          
        self._roomNumber = roomNumber
    #__repr__ method
    def __repr__(self):
        return self._name + ", born on " + self._DOB + \
               ", and has address " + self._address + ", MCP number " +\
               self._MCP + ", was admited to hospital " + self._hospital +\
               ", on " + self._dateOfAdmission + " in room number " +\
               self._roomNumber + " and is seen by " + self._doctorName
    
