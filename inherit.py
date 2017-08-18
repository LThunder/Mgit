#Filename: inherit.py

class SchoolMember:
    '''Represent any school memeber.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialize SchoolMember:{0})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{0}"Age:"{1}"'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    '''Repressent a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialize Teacher:{0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''represents a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividay', 30, 30000)
s = Student('Swaroop', 25, 75)

print() #prints a blank line

members = [t,s]
for member in members:
    member.tell() #work for both Teacher and Students