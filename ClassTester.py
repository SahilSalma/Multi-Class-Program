from Person import Person    #imports Class Person
from Employee import Employee#imports Class Employee
from Doctor import Doctor    #imports Class Doctor
from Staff import Staff      #imports Class Staff
from Patient import Patient  #imports Class Patient
objectData = [] #empty list
objectList = [] #empty list
inf = open("ClassData.txt", "r") #opens and reads Class Data.txt 
for line in inf:    #gets each line in inf
    parts = line.split(":") #splits line with collons
    objectData.append(parts)#adds the list of line split to objectData list
for i in range (len(objectData)): #loop to make objects
    objectList.append("Object%d"%(i+1)) #makes as many objects as no of list in objectData
#loop checks the class of data and assigns values to its attributes
#accodingly from text file, also prints the attributes of the class with their values
for i in range (len(objectData)):
    if objectData[i][0] == "Person":
        print (objectList[i], " has attributes as given: \n")
        objectList[i] = Person()
        objectList[i].setName (objectData[i][1])
        objectList[i].setAddress (objectData[i][2])
        objectList[i].setDOB (objectData[i][3])
        print ("Name: %s"%(objectList[i].getName()))
        print ("Address: %s"%(objectList[i].getAddress ()))
        print ("DOB: %s\n"%(objectList[i].getDOB ()))
    elif objectData[i][0] == "Employee":
        print (objectList[i], " has attributes as given: \n")
        objectList[i]= Employee()
        objectList[i].setName (objectData[i][1])
        objectList[i].setAddress (objectData[i][2])
        objectList[i].setDOB (objectData[i][3])
        objectList[i].setEmployeeNumber (objectData[i][4])
        objectList[i].setDateOfHire (objectData[i][5])
        print ("Name: %s"%(objectList[i].getName()))
        print ("Address: %s"%(objectList[i].getAddress ()))
        print ("DOB: %s"%(objectList[i].getDOB ()))
        print ("Employee Number: %s"%(objectList[i].getEmployeeNumber ()))
        print ("Date Of Hire: %s\n"%(objectList[i].getDateOfHire ()))
    elif objectData[i][0] == "Doctor":
        print (objectList[i], " has attributes as given: \n")
        objectList[i] = Doctor()
        objectList[i].setName (objectData[i][1])
        objectList[i].setAddress (objectData[i][2])
        objectList[i].setDOB (objectData[i][3])
        objectList[i].setEmployeeNumber (objectData[i][4])
        objectList[i].setDateOfHire (objectData[i][5])
        objectList[i].setAnnualSalary (objectData[i][6])
        objectList[i].setSpecialty (objectData[i][7])
        objectList[i].setNumberOfPatients (objectData[i][8])
        print ("Name: %s"%(objectList[i].getName()))
        print ("Address: %s"%(objectList[i].getAddress ()))
        print ("DOB: %s"%(objectList[i].getDOB ()))
        print ("Employee Number: %s"%(objectList[i].getEmployeeNumber ()))
        print ("Date Of Hire: %s"%(objectList[i].getDateOfHire ()))
        print ("Annual Salary: %s"%(objectList[i].getAnnualSalary ()))
        print ("Specialty: %s"%(objectList[i].getSpecialty ()))
        print ("Number of Patients: %s\n"%(objectList[i].getNumberOfPatients ()))
    elif objectData[i][0] == "Staff":
        print (objectList[i], " has attributes as given: \n")
        objectList[i] = Staff()
        objectList[i].setName (objectData[i][1])
        objectList[i].setAddress (objectData[i][2])
        objectList[i].setDOB (objectData[i][3])
        objectList[i].setEmployeeNumber (objectData[i][4])
        objectList[i].setDateOfHire (objectData[i][5])
        objectList[i].setDepartment (objectData [i][6])
        objectList[i].setJobTitle (objectData [i][7])
        objectList[i].setHourlySalary (objectData [i][8])
        objectList[i].setStatus (objectData [i][9])
        print ("Name: %s"%(objectList[i].getName()))
        print ("Address: %s"%(objectList[i].getAddress ()))
        print ("DOB: %s"%(objectList[i].getDOB ()))
        print ("Employee Number: %s"%(objectList[i].getEmployeeNumber ()))
        print ("Date Of Hire: %s"%(objectList[i].getDateOfHire ()))
        print ("Department: %s"%(objectList[i].getDepartment ()))
        print ("Job Title: %s"%(objectList[i].getJobTitle ()))
        print ("Hourly Salary: %s"%(objectList[i].getHourlySalary ()))
        print ("Status: %s\n"%(objectList[i].getStatus ()))
    elif objectData[i][0] == "Patient":
        print (objectList[i], " has attributes as given: \n")
        objectList[i] = Patient()
        objectList[i].setName (objectData[i][1])
        objectList[i].setAddress (objectData[i][2])
        objectList[i].setDOB (objectData[i][3])
        objectList[i].setMCP (objectData[i][4])
        objectList[i].setDateOfAdmission (objectData[i][5])
        objectList[i].setHospital (objectData[i][6])
        objectList[i].setDoctorName (objectData[i][7])
        objectList[i].setRoomNumber (objectData[i][8])
        print ("Name: %s"%(objectList[i].getName()))
        print ("Address: %s"%(objectList[i].getAddress ()))
        print ("DOB: %s"%(objectList[i].getDOB ()))
        print ("MCP: %s"%(objectList[i].getMCP ()))
        print ("Date Of Admission: %s"%(objectList[i].getDateOfAdmission ()))
        print ("Hospital: %s"%(objectList[i].getHospital ()))
        print ("Doctor Name: %s"%(objectList[i].getDoctorName ()))
        print ("Room Number: %s\n"%(objectList[i].getRoomNumber ()))
total = 0 #initializes total
for i in range (len(objectList)): #loop to compute total salary
    #checks if selected values is part of class Doctors
    if isinstance(objectList[i],Doctor)== True:
        total = total + int(objectList[i].getAnnualSalary()) #if true total = ...
    #checks if selected values is part of class Staff
    elif isinstance(objectList[i],Staff)== True:
        #calculates total according to full or part time
        if objectList[i].getStatus() == "Part-Time":
            total = total + (20*int(objectList[i].getHourlySalary())*52)
        elif objectList[i].getStatus() == "Full-Time":
            total = total + (40*int(objectList[i].getHourlySalary())*52)
#prints strings
print ("Total annual pay for all employees: $%d\n"%total)
print ("Name and Specialty of Doctors who earn more than $200000 per year\n")
#loop to compute name and specialty of doctor who earn more than 200000
for j in range (len(objectList)): 
    #checks if selected values is part of class Doctors
    if isinstance(objectList[j],Doctor)== True: 
        if int(objectList[j].getAnnualSalary())>200000:
            print ("Name: %s"%(objectList[j].getName()))
            print ("Specialty: %s"%(objectList[j].getSpecialty()))
            print ()
hospitalName = input ("Input hospital name: ") #user input for hospitalName
doctorName = input("Input name of doctor: ") #user input for doctorName
#prints given strings
print ()
print ("Printing the Names and MCP number of patients with given hospital and doctor\n")
#loop to check and computes patients with given hospital and doctor
for k in range (len(objectList)):
    #checks if selected values is part of class Patient
    if isinstance(objectList[k],Patient)== True:
        if  objectList[k].getHospital()== hospitalName and \
            objectList[k].getDoctorName() == doctorName:
            print ("Name: %s"%(objectList[k].getName()))
            print ("MCP number: %s"%(objectList[k].getMCP()))
            print ()
#prints given string
print ("Name, Job Tital, and employee Number of all staff in Pediatrics department\n")
#loop checks and computes name, job title, and employee number of staff in pediatrics
for l in range (len(objectList)):
    #checks if selected values is part of class Staff
    if isinstance(objectList[l],Staff)== True:
        if objectList[l].getDepartment()=="Pediatrics":
            print("Name: %s"%(objectList[l].getName()))
            print("Job Title: %s"%(objectList[l].getJobTitle()))
            print("Employee Number: %s"%(objectList[l].getEmployeeNumber()))
            print()




























