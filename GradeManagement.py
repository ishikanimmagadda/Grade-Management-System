import csv

class Student: 
    def __init__(self, name, grade): 
        self.name = name
        self.grade = {}

    def setGrade(self, key, value): 
        self.grade[key] = value
    
    def setName(self, name): 
        self.name = name
    
    def removeGrade(self, key): 
        if key in self.grade: 
            del self.grade[key]
    
    def displayGrades(self): 
        print("Name: " + self.name + ", Grades: " + str(self.grade))
    
    def writeToFile(self, filename):
        file = open(filename, 'a')
        file.writelines("Name: " + self.name + ", Grades: " + str(self.grade) + "\n")
        file.close()
    
    def readFile(self, filename): 
        file = open(filename, 'r')
        content = file.readlines()
        print ("Readlines: " + str(content))
        file.close()
        

    
    
#for every new run overwrites old info from file 
file = open("gradefile.txt", 'w')

#declaring class variable 
Student1 =  Student("Ishika",{})
Student1.setName("Ishika")

#user input grade
Student1.key = input("Enter the Subject: ")
Student1.value = input("Enter a Grade: ")
Student1.setGrade(Student1.key, Student1.value)

Student1.setGrade("Math",90)
Student1.displayGrades()

#testing remove 
Student1.removeGrade(Student1.key)
Student1.displayGrades()

#writing grades excluding removed grade
Student1.writeToFile("gradefile.txt")

Student1.readFile("gradefile.txt")




Student2 =  Student("Potter",{})
Student2.setName("Potter")

#user input grades 
Student2.key = input("Enter the Subject: ")
Student2.value = input("Enter a Grade: ")
Student2.setGrade(Student2.key, Student2.value)

Student2.setGrade("Science", 87)
Student2.displayGrades()

#removing Science 
Student2.removeGrade(key = "Science")
Student2.displayGrades()

Student2.writeToFile("gradefile.txt")

Student2.readFile("gradefile.txt")


