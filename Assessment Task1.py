
calc = lambda x,y,z: z(x,y)
multiply = lambda x,y: x*y
divide = lambda x,y: x/y
allStudents = []
allCourses = []
end = 1
def setLim (x):
    while (True):
        if (x >= 0 and x<= 4):
            return x
        print("input must be between 0 to 4 inclusive")
        x = int(input("Enter proper units: "))
            
def checkUniqueID(x,y):
    for z in range(len(y)):
        if (x == allCourses[z].ID):
            return False
    return True
def checkUniqueCode(x,y):
    for z in range(len(y)):
        if (x == allCourses[z].code):
            return False
    return True

def setID(ID):
    while(True):
        if (len(str(ID)) is 8 and checkUniqueID(ID,allStudents)):
            return ID
        print("ID should be unique and have 8 characters")
        ID = int(input("Enter proper ID: "))
            
def checkName (name):
    while(True):
        if (isinstance(name,str)):
            return name
        print("Name is invalid")
        name = input("Enter valid name: ")

class Student:
    def __init__(self, name, ID):
        self.name = checkName(name)
        self.ID = setID(ID)
        self.course = []
        self.grades = {}
    def editName (self,name):
        self.name = checkName(name)
            
    def enroll (self,Course):
        self.course.append(Course)
        self.grades.setdefault(Course,0.0)
        
    def drop (self,Course):
        self.course.remove(Course)
        self.grades.pop(Course)

    def setGrade (self,Course,grade):
        self.grades[Course] = setLim(grade)
    
    def viewReport (self):
        print("\nReportCard")
        print("Name: " + self.name)
        print("ID: " + str(self.ID))
        y = 0
        z = 0
        for x in range(len(self.course)):
            print(str(self.course[x].code) + ":" + str(self.grades[self.course[x]]))
            y += calc(self.course[x].unit,self.grades[self.course[x]],multiply)
            z += self.course[x].unit
        print("GPA: " + str(calc(y,z,divide)))
           
def setCode (code):
    while(True):
        if (len(code) is 7 and checkUniqueCode(code,allCourses)):
            return code
        print("code must be 7 characters and unique")
        code = input("Enter proper Course code: ")
            
class Course:
    def __init__(self,code,unit):
        self.code = setCode(code)
        self.unit = setLim(unit)
        
    def enroll(self,Student):
        self.students.append(Student)

    def drop(self,Student):
        self.students.remove(Student)
        
    def editCode(self,code):
        self.code = setCode(code)
        
    def editUnit(self,unit):
        self.unit = setLim(unit)
        
def studentMenu ():
    while(True):
        found = 1
        for x in allStudents:
            print("\nName: " + x.name+ " ID: " + str(x.ID))
        print("\n Student Menu")
        print(" 1: create a student")
        if(len(allStudents) is not 0):
            print(" 2: edit a student's name")
            print(" 3: delete a student")
        print(" 0: return to Mainmenu")
        x = int(input("Option : "))
        if (x == 1):
            y = input("Enter the name of student: ")
            z = int(input("Enter the student's ID# "))
            allStudents.append(Student(y,z))
        elif (x == 2):
            z = input("Enter the current name of student: ")
            for y in range (len(allStudents)):
                if z == allStudents[y].name:
                    found = 0
                    allStudents[y].editName(input("Enter the new name of student: "))
            if (found == 1):
                print(z + " is not a student here\n")
        elif (x == 3):
            z = input("Enter the name of student: ")
            for y in range (len(allStudents)):
                if z == allStudents[y].name:
                    found = 0
                    allStudents.pop(y)
            if (found == 1):
                print(z + " is not a student here\n")
        else:
            break
    Mainmenu()
    
def courseMenu ():
    while(True):
        for x in allCourses:
            print("\nCode: "+ x.code+" Units: " + str(x.unit))
        found = 1
        print("\n Course Menu")
        print(" 1: create a course")
        if(len(allCourses) is not 0):
            print(" 2: edit a course's code")
            print(" 3: edit a course's unit")
            print(" 4: delete a course")
        print(" 0: return to Mainmenu")
        x = int(input("Option : "))
        if (x == 1):
            y = input("Enter the course code: ")
            z = int(input("Enter the units of course: "))
            allCourses.append(Course(y,z))
        elif (x == 2):
            z = input("Enter the current course code: ")
            for y in range (len(allCourses)):
                if z == allCourses[y].code:
                    found = 0
                    allCourses[y].editCode(input("Enter the new course code: "))
            if (found == 1):
                print(z + " is not a course here\n")
        elif (x == 3):
            z = input("Enter the current course code: ")
            for y in range (len(allCourses)):
                if z == allCourses[y].code:
                    found = 0
                    allCourses[y].editUnit(input("Enter the new course units: "))
            if (found == 1):
                print(z + " is not a course here\n")
        elif (x == 4):
            z = input("Enter the course code: ")
            for y in range (len(allCourses)):
                if z == allCourses[y].code:
                    found = 0
                    allCourses.pop(y)
            if (found == 1):
               print(z + " is not a course here\n")
        else:
            break
    Mainmenu()
    
def enrollmentMenu ():
    while (True):
        print("\nCourses: ")
        for x in allCourses:
            print("Code: "+ x.code+" Units: " + str(x.unit))
        print("\nStudents: ")
        for x in allStudents:
            print("Name: " + x.name+ " ID: " + str(x.ID))
        found = 1
        x = int(input("\n Enrollment Menu \n 1: enroll a student in a course \n 2: drop a student in a course \n 3: set a student's grade in a course \n 4: view a student's report card \n 0: return to Mainmenu \nOption : "))
        if (x == 1):
            y = input("Enter the course code: ")
            for w in range (len(allCourses)):
                #pokemon
                if (y == allCourses[w].code):
                  found = 0
                  z = int(input("Enter the ID of student: "))
                  for v in range (len(allStudents)):
                      if (z == allStudents[v].ID):
                          found = 0
                          allStudents[v].enroll(allCourses[w])
            if(found):
                print("Student/Course doesn't exist")
        elif (x == 2):
            y = input("Enter the course code: ")
            for w in range (len(allCourses)):
                #pokemon
                if (y == allCourses[w].code):
                  found = 0
                  z = int(input("Enter the ID of student: "))
                  for v in range (len(allStudents)):
                      if (z == allStudents[v].ID):
                          found =0
                          allStudents[v].drop(allCourses[w])
            if(found):
                print("Student/Course doesn't exist")
        elif (x == 3):
            
            z = int(input("Enter the ID of student: "))
            for v in range (len(allStudents)):
                if (z == allStudents[v].ID):
                    found = 0
                    if (len(allStudents[v].course)==0):
                        print("This student has no courses")
                        break
                    y = input("Enter the course code: ")
                    for w in range (len(allCourses)):
                #pokemon
                        if (y == allCourses[w].code):
                            found = 0
                            allStudents[v].setGrade(allCourses[w],float(input("Enter the grade of "+allStudents[v].name +": ")))
            if(found):
                print("Student/Course doesn't exist")
        elif (x ==4):
            y = int(input("Enter the ID of student: "))
            for z in range(len(allStudents)):
                if (y == allStudents[z].ID):
                    found = 0
                    if (len(allStudents[z].course)==0):
                        print("This student has no courses")
                        break
                    allStudents[z].viewReport()
            if(found):
                print("Student/Course doesn't exist")
        else:
            break
    Mainmenu()        
                 
def Mainmenu ():
    print("Enrollment System\n")
    print(" 1: Student Menu")
    print(" 2: Course Menu")
    if (len(allCourses) is not 0 and len(allStudents) is not 0):
        print(" 3: Enrollment Menu")
    x = int(input("Option : "))
    if (x == 1):
        studentMenu()
    elif (x == 2):
        courseMenu()
    elif (x == 3):
        enrollmentMenu()
    else:
        return 0
    
while (end):
    end = Mainmenu()

    
