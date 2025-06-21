#old style -  procedural coding
a= 10 
b =20
sum = a+b

# print(f"proceduaral coding: {sum}")

#concept functions
def sum(a,b):
    print(f"addition using functions: {a+b}")
    
# sum(10,40)

# object oriented programming - code reusability & redundancy
#object is not created directly it is a created by using classes

class Car:  # blueprint they dont oocupy any space in the storage
    brand = "suzuki"
    
car1 = Car() # object creation (instance of class) They occupy space in teh storage
# print(car1) 
# print(car1.brand) 
    
#constructor in classes executes directly when an object is created

class Cars:
    def __init__(self,brand,color,price):  #attributes
        self.carbrand = brand
        self.color = color
        self.price = price
        
suzuki = Cars("SUZUKI","white",45367)
# print(suzuki.price)    
bmw= Cars("BMW","blue","1.2cr")
mercedes = Cars("Mercedes","Black","1.3cr")
# print(bmw.price)
# print(mercedes.color)  #access data

list_of_cars = [bmw.carbrand,   bmw.price,   mercedes.carbrand,   mercedes.price]

print(list_of_cars)
# print(type(list_of_cars))


class Laptop:  
    school = "xdlinx school"  # class attr
    #default constructor 
    def __init__(self):
        pass
    
    #parameterised constructor 
    def __init__(self,brand,price): #obj attr
        self.laptop_brand = brand
        self.price = price
        
laptop1 = Laptop("Dell",35000)
# print(laptop1.laptop_brand,laptop1.price)

#the data which is different for each object is placed under __init__()
#similar data is placed directly inside the class common data for all objects
#obj attr >> class attr  - higher priority for obj attr


#Methods - functions inside a class

class Person:
    def __init__(self,name,age): #constructor
        self.name = name
        self.age =age
    
    def Greeting(self): #method 1
        print(f"Good Morning {self.name}")
        
    def Get_Age(self): #method 2
        print(f"{self.name} is {self.age} years old")
        
p1 = Person("Adam",29)
p2 = Person("amar",23)
p2.Get_Age()

p2.Greeting()   
# p1.Get_Age()

# practice Test - 1
class Student():
    def __init__(self,name,marks):
        self.student_name = name
        self.marks = marks
   
    
    def Avg_marks(self):
        sum = 0
        for avg in self.marks:
            sum += avg
        print("Average marks of ",self.student_name, "is ", sum/3)

s1 = Student("Adam",[56,89,90])
s1.Avg_marks()

s1.student_name = "Eva"
s1.Avg_marks()


#static methods  - dont use self parameter
#class level methods

class GetData:
    @staticmethod #Decorator
    def hello(name):
        print("hello")
        print(name)
        
a1 = GetData()
a1.hello("adam")



#Abstraction & Encapsulation

#abstraction is hiding the data which is unnecessary to the user

#encapsulation is wrapping data and functions into a single unit(object).


