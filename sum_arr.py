# print("summ of sub array")
# arr=[1,2,3,4]
# total=0
#
# for i in range(len(arr)):
#     left=i+1
#     right=len(arr)-i
#     total=total+arr[i]*left*right
# print(total)
# # for i in range(len(arr)):
# #     sum=0
# #     for j in range(i,len(arr)):
# #         print(arr[j],end=" ")
# #         sum+=arr[j]
# #         total+=sum
# # print(total)
#
nu=[1,2,2,3,3,4,4,5]
num=set(nu)
print(num)

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 2, 3}
d = {"name": "Uday", "age": 21}

print(len(a))
print(len(b))
print(len(c))
print(len(d))

nums = {10, 20, 30}

print(nums.pop())

print(nums)



from abc import ABC, abstractmethod
# Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):

        pass
# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")
# Child Class
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")
# Creating Objects
d = Dog()
c = Cat()

d.sound()
c.sound()




from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")
car = Car()
bike = Bike()

car.start()
bike.start()



class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
    def show_marks(self):
        print("Marks:", self.marks)

s = Student("Uday Kumar", 95)
s.show_name()
s.show_marks()

name="uday"
n=22
print(name+str(n))
