#!/usr/bin/env python3
# Author ID: xli472 

class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)

    def addGrade(self, course, grade):
        self.courses[course] = grade
        self.grade = self.courses[course] 


    def displayGPA(self):
        try:      
            gpa = 0.0
            for course in self.courses.keys():
                gpa = gpa + self.courses[course]
            return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))
        except ZeroDivisionError:
            return 'GPA of student ' + self.name + ' is ' + '0.0'

    def displayCourses(self):
        pass_courses = []
        for course in self.courses:
            grade = self.courses[course]
            if grade != 0:       
                pass_courses.append(course) 
        return pass_courses  

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
