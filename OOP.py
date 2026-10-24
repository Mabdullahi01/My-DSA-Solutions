"ENCAPSULATION"

class Car:
    def __init__(self):
        self.__speed = 0
        self.__fuel = 100

    def accelerate(self):
        if self.__fuel > 0:
            self.__speed += 10
            self.__fuel -= 5
            print(f"accelerating... Speed: {self.__speed} km/h, Fuel: {self.__fuel}%")
        else:
            print("Not enough fuel to accelerate!")

    def brake(self):
        if self.__speed > 0:
            self.__speed -= 10
            print(f"Braking...Speed: {self.__speed} km/h")
        else:
            print("The car is already stopped.")

    def get_speed(self):
        return self.__speed
    def get_fuel(self):
        return self.__fuel








'INHERITANCE'

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        print(f"The {self.engine} engine is starting...")

class Car(Vehicle):
    def __init__(self, engine, doors):
        #super().__init__(engine)
        # OR
        Vehicle.__init__(self, engine)
        self.doors = doors

    def honk(self):
        print("Car honk: Beep beep")

class Bike(Vehicle):
    def __init__(self, engine, type_of_handlebar):
        super().__init__(engine)
        self.type_of_handlebar = type_of_handlebar

    def ring_bell(self):
        print("Bike bell: Ring ring!")



"POLYMORPHISM"
class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

class Triangle:
    def draw(self):
        print("Drawing a triangle")

# Polymorphism in action
def render_shape(shape):
    shape.draw()








from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)




from abc import ABC, abstractmethod

# Encapsulation & Inheritance
class Animal(ABC):
    def __init__(self, name, age=0):
        self._name = name      # Encapsulated attributes with protected access
        self.__age = age  # Using a single underscore to indicate protected variables

    @abstractmethod  # This is what allows us to do polymorphism
    def sound(self):           # Abstract method, will be overridden in subclasses
        pass

    def info(self):
        return f"{self._name} is {self.__age} years old."
#
# # Inheritance
class Lion(Animal):
    def sound(self):
        return "Roar!"         # Polymorphism - specific implementation of sound for Lion

class Elephant(Animal):
    def sound(self):
        return "Trumpet!"      # Polymorphism - specific implementation of sound for Elephant

class Zoo:
    def __init__(self):
        self._animals = []     # Encapsulated list of animals

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
            print(f"{animal._name} has been added to the zoo.")
        else:
            print("Only animals can be added to the zoo.")

    def show_sounds(self):
        for animal in self._animals:
            print(f"{animal._name} says: {animal.sound()}")

# Demonstrating OOP Principles
zoo = Zoo()
leo = Lion("Leo")
dumbo = Elephant("Dumbo", 10)



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverseLinkedList(head: Node):
    if not head:
        return head

    prev = None
    next_node = head.next

    return prev
from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
















# Inheritance from corey shafer

# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
# class Developer(Employee):
#     raise_amt = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay) # Can also use Employee.__init__(self, first, last, pay)
#         self.prog_lang = prog_lang
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())
#
#
#
#
#
#
#
#
# dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
# dev_2 = Developer('Mohammed', 'Alchemy', 60000, 'java')
#
# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()


# print(dev_1.email)
# print(dev_2.prog_lang)

# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)

#print(isinstance(mgr_1, Developer))
#print(issubclass(Manager, Employee))





'SPECIAL/MAGIC METHODS'

# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     def __repr__(self):
#         return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
#
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)
#
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(self.fullname())
#
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Mohammed', 'Alchemy', 70000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(emp_1 + emp_2)

# print(len(emp_1))


'''Property Decorators'''

# class Employee:
#

#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Name Deleted!')
#         self.first = None
#         self.last = None
#
# emp_1 = Employee('John', 'Smith')
#
# emp_1.fullname = 'Mohammed Abdullahi'
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#
# del emp_1.fullname



'''OOP nother channel'''

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#
#         return value / len(self.students)
#
#
#
# s1 = Student('Tim', 19, 95)
# s2 = Student('Bill', 19, 85)
# s3 = Student('Jill', 19, 75)
#
# course = Course('Science', 2)
# course.add_student(s1)
# course.add_student(s2)
# #print(course.students[1].grade)
#
# print(course.get_average_grade())

'''Inheritance'''
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def speak(self):
#         print('Meow')
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
#
# class Dog(Pet):
#     def speak(self):
#         print('Bark')
#
# pet = Pet('Tim', 19)
# pet.show()
# cat = Cat('Bill', 37)
# cat.show()
# cat.speak()
# dog = Dog('Hill', 25)
# dog.show()
# dog.speak()


'''class attributes, class methods, static methods'''
'''class attributes'''
# class Person:
#     number_of_people = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.number_of_people += 1
#
# p1 = Person('tim')
# print(Person.number_of_people)
# p2 = Person('Dim')
# print(Person.number_of_people)

'''class methods'''
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('tim')
p2 = Person('Dim')
print(Person.number_of_people_())


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, pageweight):
        return cls(name, cls.TYPES[0], pageweight + 100)

    @classmethod
    def paperback(cls, name, pageweight):
        return cls(name, cls.TYPES[1], pageweight )

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Harry Potter", 1500)



























