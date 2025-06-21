# class person :
#     def __init__ (self, name , age ):
#         self.name= name
#         self.__age =age 
    
#     def get(self):
#         print("hi" ,self.name)
        
# a = person("vaishnavi",23)    
# a.get()

class person :
    def __init__ (self, name , age ):
        self.name= name
        self.age =age 
    
class t(person) :
    def __init__(self, name,age,ph):
       super().__init__(name,age)
       self.ph =ph
       print (self.name,self.age,self.ph)
       
       
       
       
x =t("vaishnavi","23",99999)                



    
    
    
    