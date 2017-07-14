import pdb


class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initializing school member {} ".format(self.name))

    def tell(self):
        print("Name: {} \t Age: {}".format(self.name, self.age)),


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialing Teacher {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("salary :{:d}".format(self.salary))


class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initializing Marks :{}".format(self.marks))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks :{:d}".format(self.marks))

t = Teacher('Roudy', 35, 2000)
s = Student('Ramdev', 18, 45)

members = [t, s]
print()

for m in members:
    pdb.set_trace()
    m.tell()
