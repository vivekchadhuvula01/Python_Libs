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
# s1.Avg_marks()

s1.student_name = "Eva"
# s1.Avg_marks()

# del s1.student_name  #deletes the attribute from the object memory

# print(s1.student_name)

# AttributeError: 'Student' object has no attribute 'student_name'

# class scope  ------   global scope
class Account:
    def __init__(self,Acc_no,Acc_pass):
        self.acc_no = Acc_no
        self.__password = Acc_pass  #private cannot be accessed outside the class
        
    def get_pass(self): 
        print(self.__password)
    def reset_pass(self):
        old_pass =input( "Enter old password: ")
        if(old_pass == self.__password):
            new_pass = input("Enter new password: ")
            self.__password = new_pass
        else:
            print("Wrong password")
acc1 = Account(23415,"qwerty")
acc2 = Account(14253,"password")
# print(acc1.__password)   ##AttributeError: 'Account' object has no attribute '__password'

# acc1.get_pass()   # can be accessed from inside the class using a function
# acc2.get_pass()
# acc1.reset_pass()

# acc1.get_pass()
#same as for Methods also

class person:
    __name = "something"
    
    def __greet(self): #private method cannot access outside the method
        print("Welcome to the team")
        
    def Welcome(self):
        self.__greet()
        
p1 = person()

# p1.__greet()   AttributeError: 'person' object has no attribute '__greet'
# p1.Welcome()


# #------------------------INHERITANCE-------------------------------------------
# #when one class (child) derives props of another class(parent) then it  is called inheritance

class Engine:
    def __init__(self, fuel, cc, power):
        self.power = power
        self.capacity = cc
        self.fuel = fuel

    def EngineDetails(self): #method
        print("Fuel:", self.fuel)
        print("Capacity (cc):", self.capacity)
        print("Power (HP):", self.power)


class TataEngine(Engine):  # TataEngine is a child class of Engine
    def __init__(self, name, fuel, cc, power):
        super().__init__(fuel, cc, power)  # Call parent class constructor
        self.name = name

    def TataDetails(self):
        print("Model Name:", self.name)
        self.EngineDetails()  # Optionally show engine details as well


car = TataEngine("nexon","petrol","1198","112hp")
car.TataDetails()     
# # car.EngineDetails()
# # car.TataDetails()  

# #hierarchical inheritance

# class MahindraEngine(Engine):
#     def __init__(self,name,fuel,cc,power):
#         super().__init__(fuel,cc,power)
#         self.name = name
        
#     def MahindraDetails(self):
#         print(self.name)
#         self.EngineDetails()
        
# car2 = MahindraEngine("XUV700","Diesel",2198,"180hp")
# # car2.EngineDetails()

# #multilevel inheritance

# class CarVarient(TataEngine):
#     def __init__(self,varient, name, fuel, cc, power):
#         super().__init__(name, fuel, cc, power)
#         self.varient = varient
        
#     def Curvv_Details(self):
#         print("Varient: ",self.varient)
#         self.TataDetails()

# TATA_Curvv = CarVarient("Smart plus","TATA Curvv","Diesel",1497,"116hp")
# TATA_Curvv.Curvv_Details()