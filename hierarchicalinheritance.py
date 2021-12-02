#1 class defination///////////////////////////////
class parent():
    #property
    #contructor
    #method
    def name(self):     #method /function
        print("this is a class function")
#create object
nyname = parent()
#function calling
nyname.name()
#2 class defination////////////////////////////
class child(parent):
    #property
    #contructor
    #method
    def name2(self):   #method/function
        print("this is a singlelevel inheritance class")
#create object
my = child()
#function calling
my.name()
#3 class defination//////////////////////////////
class child2(parent):
    #property
    #contructor
    #method
    def name3(self):      #method/function
        print("this class is hierarchical inheritance")
#create object
my1 = child2()
#function calling
my1.name()
my.name2()
my1.name3()