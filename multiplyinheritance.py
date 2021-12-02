#1 class defination////////////////////////////////
class parent():
    #property
    #contructor
    #method
    def name(self):   #method/function
        print("the class is base class")
#create object
mynam = parent()
#function calling
mynam.name()
#2 class defination/////////////////////////////////
class parent2():
    #property
    #contructor
    #method
    def name2(self):     #method/function
        print("the second class is base class")
#create object
dipesh = parent2()
#function calling
dipesh.name2()
#3 class defination/////////////////////////////////
class child(parent,parent2):
    #property
    #contructor
    #method
    def child2(self):  #method/function
        print("this class is multiply inheritance")
#create object
mystu = child()
#function calling
mystu.name()
mystu.name2()
mystu.child2()