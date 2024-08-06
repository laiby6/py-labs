
#Loop Control Statements
#Continue Statement

for letter in 'Python':
    if letter == 't' or letter == 'o':
        continue
    print('Current Letter: ',letter)

#Break Statement
for letter in 'Python':
    if letter =='t' or letter == 'o':
        break
    print("Current letter: ",letter)

#Python Funtions

def first_function():
    print("This is a function")
first_function()    

#Functions with Parameters
def first_function(fname):
    print(fname,"Whatever")
first_function("emil")  
first_function("gmil") 
first_function("fmil")   

#Default Parameter Value

def first_function(country = "Norway"):
    print("Tooba is From "+country)
first_function("Paistan") 
first_function("India") 
first_function()   

#Passing a List as a Parameter

def first_function(food):
    for x in food:
        print(x)

fruit = ["apple","orange","bnana"]
first_function("fruit")        

#Returning values in a Funtion

def first_function(x):
    return 5*x

print(first_function(2) )  
print(first_function(5) ) 
print(first_function(10) ) 

#Keyword Arguments

def first_function(child3,child2,child1):
    print("The youngest child is: "+child3)

first_function(child2 ="Tobias",child3="Emil",child1="Linus")

#Classes in Python

class myClass: x = 5

#Objects in Python

p1=myClass() 
print(p1.x)

#The Init Function

class Person:
   def __init__(self,name,age):
      self.name=name
      self.age = age
p1=Person("John",36)

print(p1.name)
print(p1.age)

#Object Methods

class Person:
    def __init__(self,name,age):
      self.name=name
      self.age = age
def myfun(self):
    print("Hello My name is: "+self.name)

    p1 = Person("John",36)
    p1.myfun()      