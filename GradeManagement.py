import csv

#fields = ['Name', 'Grade']

#file1 = open("gradefile.txt", "r")
class Student: 
    def __init__(self, name, grade): 
        self.name = []
        self.grade = []

    def setGrade(self, grade): 
        self.grade.append(grade)
    
    def setName(self, name): 
        self.name.append(name)
    
    def removeGrade(self, grade): 
        self.grade.remove(grade)
    
    def displayGrades(self): 
        for name in self.name: 
            print("Name: " + name + ", Grades: " + str(self.grade))
    
    def writeToFile(self, filename):
        file = open(filename, 'w')
        for name in self.name: 
            file.writelines("Name: " + name + ", Grades: " + str(self.grade) + "\n")
        file.close()
    

Student1 =  Student([],[])
Student1.setName("Ishika")
Student1.setGrade(80)
Student1.setGrade(98)
Student1.displayGrades()
Student1.writeToFile("gradefile.txt")

Student2 =  Student([],[])
Student2.setName("Potter")
Student2.setGrade(30)
Student2.setGrade(50)
Student2.displayGrades()
Student2.writeToFile("gradefile.txt")


