class Student:
    def __init__(self, name, age, phone_number, email):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def introduce(self):
        print(f"my name is {self.name}")

    def get_phoneNumber(self):
        return self.phone_number

    def set_phoneNumber(self, phoneNumber):
        self.phone_number = phoneNumber

class Course:
  def __init__(self, name, courseTerm, maxSize):
    self.name = name
    self.courseTerm = courseTerm
    self.maxSize = maxSize
    self.studentList = []

  def addStudent(self, student):
    self.studentList.append(student)

  def get_studentList(self):
    return self.studentList

studentA = Student("Tom", 25, "204-235-2125", "tom.jerry@gmail.com")
