# in memory DB
from models import Student
s1 = Student(name="Satyam", age=23, course="AI/ML", email="satyam@gmail.com")
s2 = Student(name="Shivam", age=21, course="Data Science", email="shivam@gmail.com")
s3 = Student(name="Sundaram", age=20, course="Backend", email="sundaram165344@gmail.com")
s4 = Student(name="Gautam", age=19, course="AI/ML", email="gautam@gmail.com")
students = []
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)
professors = []
