#1class defination////////////////////////////
class parent:
    #property 
    #contructor
    #method
    def fun1(self):         #method/function
        print("this is a function")
#create object
myper = parent()
#calling function
myper.fun1()    
#2 class defination////////////////////////////
class child(parent):
    #property
    #contructor
    #method
    def med(self):    #method/function
        print("this class is inherite")
#create object
mych = child()
#function calling
mych.med()        
#3 class defination/////////////////////////////
class child2(child):
    #property
    #contructor
    #method
    def stu(self):    #method/function
        print("this class is multilevel inheritance")
#create object
mystud = child2()
#function calling
mystud.fun1()
mystud.med()
mystud.stu() 
