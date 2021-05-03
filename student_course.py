class Student:

  number_of_students = 0

  def __init__(self, name, age, phone_number, email):
    self.name = name
    self.age = age
    self.phone_number = phone_number
    self.email = email
    Student.number_of_students += 1

  def introduce(self):
    print(f"my name is {self.name}")

  def get_phoneNumber(self):
    return self.phone_number

  def set_phoneNumber(self, phoneNumber):
    self.phone_number = phoneNumber


class Course:

  total_courses_created = 0
  courses = []

  def __init__(self, name, courseTerm, maxSize):
    self.name = name
    self.courseTerm = courseTerm
    self.maxSize = maxSize  # max num of student that can be admitted to the course
    self.studentList = []
    Course.total_courses_created += 1
    Course.courses.append(self.name)

  def addStudent(self, student):
    self.studentList.append(student)

  def get_studentList(self):
    # want create an empty list
    my_List = []
    # loop over the studentList, create key value pair from the objetc in the list
    for student in self.studentList:
      my_obj = {}
      my_obj['name'] = student.name
      my_obj['age'] = student.age
      my_obj['phone_number'] = student.phone_number
      my_obj['email'] = student.email

      my_List.append(my_obj)
    # print(self.studentList[0].name)

    return my_List


studentA = Student("Tom", 25, "204-235-2125", "tom.jerry@gmail.com")
print(f"this is student A {studentA}")
print(Student.number_of_students)

studentB = Student("Jerry", 45, "205-235-2125", "jery.jerry@gmail.com")
print(Student.number_of_students)

courseA = Course("Chemistry 101", "Fall", 10)
print(Course.total_courses_created)
print(Course.courses)

courseB = Course("CSC 201", "Spring", 15)
print(Course.total_courses_created)
print(Course.courses)

courseA.addStudent(studentA)
courseA.addStudent(studentB)
courseB.addStudent(studentA)
courseB.addStudent(studentB)

sL = courseB.get_studentList()

print(len(sL))

