# Day 6 - Object Oriented Programming (OOP)

## Class
A class is a blueprint used to create objects.

Example:
class Student:
    pass

## Object
An object is an instance of a class.

Example:
s1 = Student()

## Constructor
A constructor (__init__) is a special method that runs automatically when an object is created.

Example:
def __init__(self, name):
    self.name = name

## Self Keyword
self refers to the current object of the class.

## Methods
Methods are functions defined inside a class.

Example:
def display(self):
    print(self.name)

## Inheritance
Inheritance allows one class to use properties and methods of another class.

Example:
class Animal:
    pass

class Dog(Animal):
    pass

## Benefits of OOP
- Code reusability
- Better organization
- Easy maintenance
- Real-world modeling
