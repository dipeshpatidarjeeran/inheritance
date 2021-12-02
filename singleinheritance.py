#class defination
class student:
    #property
    #constructor
    #method
    def subj(self):  #method/function
        print("hello friends")

    def claa(self):   #method/function
        print("this classs is 12")

 #class instatiation / object
myobject = student()
 #calling the function
myobject.subj()
myobject.claa()       
#second class defination
class student2(student):
    #property 
    def __init__(self):
        print("hello from init method")                    #contructor
    #method
    def name(self):
        print("dipesh,ajay,sadit")
mystu = student2() #create the object
#calling the function
mystu.subj()
