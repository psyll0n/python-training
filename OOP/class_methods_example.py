class MyClass:
    course = "Python for Everybody."

    def __init__(self, students):
        self.students = students

    def get_total_students(self):
        print(f"The total number of students is: {self.students}")

    def thing(self, param1="Thing"):
        print(param1)

    def add_students(self):
        self.students = self.students + 1
        print("New total is", self.students)


my_class = MyClass(100_000)

my_class.thing()
my_class.thing("Something else")

my_class.get_total_students()

print(my_class.students)
my_class.add_students()

print(my_class.students)
