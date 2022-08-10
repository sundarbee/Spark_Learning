#Without Inheritance
#base class
class gfather:
 print("Grand Father class")
 agri_land=2000000
#base class
class father:
 print("Father class")
 land=2000000
 agri_land=2000000
 def business(self,investment):
  return investment+(investment*.10)
#base class
class mother:
 cash=1000000
#base class
class son():
 land=2000000
 cash=1000000
 agri_land = 2000000
 def business(self,investment):
  return investment+(investment*.10)

objson=son()
print("constructing a house using my own land and amount {}".format(objson.land+objson.cash))

#Inheritance
#Single Inheritance
#Derived class
class son_single_inherit(father):
 owncash=1000000


obj_son_single_inherited=son_single_inherit()
print("Single Inherit - constructing a house using my inherited property only from my father (since i have money for construction earned already) "
      "like land {} and I use my cash for construction".format(son_single_inherit.land+son_single_inherit.owncash))

#Multiple Inheritance
#Derived class
class son_multiple_inherit(father,mother):
 owncash=100000

objsoninherited=son_multiple_inherit()
print("Multiple Inherit - constructing a house using my inherited properties (since i dont want to put a hard effort of earning it again) "
      "like land and amount {} and I use my cash for interior".format(objsoninherited.land+objsoninherited.cash+objsoninherited.owncash))

#Multilevel Inheritance
#Base class
class gfather:
 print("Grand Father class")
 agri_land=2000000

#Derived/Base class
class father(gfather):
 print("Father class")
 land=2000000

#Derived class
class son_multilevel_inherit(father):
 owncash=100000

objsonmultilevelinherited=son_multilevel_inherit()
print("Multilevel Inherit - constructing a house using my inherited properties (since i dont want to put a hard effort of earning it again) like agri land from grandfather  with amount {} ,land from father with amount {} and I use my cash for constructing house {}".format(objsonmultilevelinherited.agri_land,objsonmultilevelinherited.land,objsonmultilevelinherited.owncash))

#Hierarchical Inheritance
#Base class
class gfather:
 print("Grand Father class")
 agri_land=2000000

#Derived class
class father(gfather):
 print("Father class")
 land=2000000

#Derived class
class son_hierarchical_inherit(gfather):
 owncash=100000
 #agri_land = 3000000

objfatherhierarchicalinherited=father()
objsonhierarchicalinherited=son_hierarchical_inherit()
print("Hierarchical Inherit - Father Inherits agri_land of amount {} from his grandfather and use his own land {}".format(objfatherhierarchicalinherited.agri_land,objfatherhierarchicalinherited.land) )
print("Hierarchical Inherit - Grandson Inherits agri_land of amount {} from his grandfather and use his amount {}".format(objsonhierarchicalinherited.agri_land,objsonhierarchicalinherited.owncash) )

# diamond problem
# ???

#Abstraction - Hiding the complexity/unnecessary things or showing only whatever is needed eg. summary, index page
# Example tv remote. we use the remote buttons but don't know the core logic of programming behind it
# A class is called an Abstract class if it contains one or more abstract methods.
# An abstract method is a method that is defined, but contains no implementation.
# Abstract classes may not be directly instantiated, and its abstract methods must be implemented by its derived classes
# to get it instantiated

from abc import ABC,abstractmethod #Base Absract Class

print("Simple Abstract class example")
# Regular classes can be instantiated directly
class clsnorm():
 def fun1(self):
  print("I am a normal class function")

# Abstract classes cannnot be instantiated directly, rather they can be inherited and instantiated
class clsabc(ABC):
 @abstractmethod #decorator @abstractmethod will convert the immediate next line function defined to abstract method
 def fun1(self):
  print("I am a abstract class function")
 def fun2(self):
  a=100
  print("I am a simple abc class function")

objclsnorm = clsnorm()
print(objclsnorm.fun1())

#objclsabc = clsabc() # We can't instantiate, because it is abstract class
#print(objclsabc.fun1())
#print(objclsabc.fun2())

class abcinherited(clsabc):
 def fun1(self): #this is must
  a=150
  print("I am an implemented abstract method {}".format(a))


objabcinherited=abcinherited()
print(objabcinherited.fun1())
print(objabcinherited.fun2())

print("Simple Abstract class example ends")

#class base_remote: #I am a simple base class
class base_remote(ABC):  # I am an abstract (derived) class now by single inheriting ABC class
 @abstractmethod
 def power(self,a):#un implemented function
  pass
 @abstractmethod
 def volume(self,a):
  pass
 def channel(self,a,b):
  if a=='up':
   return b+1
  else:
   return b-1

class derived_remote_tv(base_remote):#hierarchical Inheritance
 def power(self,a):
  return a+'radio frequency'
 def volume(self,a):
  return a+1


class derived_remote_hometheater(base_remote):#hierarchical Inheritance
 def power(self,a):
  return a+'Infrared'
 def volume(self,a):
  return a+10


obj_tv=derived_remote_tv()
obj_homet=derived_remote_hometheater()

print(obj_tv.power('button pressed '))
print(obj_tv.volume(2))
print(obj_tv.channel('up',1))
print(obj_tv.channel('down',2))
print(obj_tv.power('button pressed '))
print(obj_homet.volume(1))
print(obj_homet.channel('up',1))

#3. Polymorphism (Overloading & Overriding)
# Overloading -> A function with same name but different in the number of arguments or type of arguments
#Benefits:
#Polymorphism (Overloading) doesn't support in python directly, need to use some special functions or workaround, because
# Python is a dynamically typed language
# Overriding ->
def fun1(a:int):
 return a * a

def fun1(a:str):
 return a + a

def fun1(a:int, b:int):
 return a * b

#Work around 1 for applying polymorphism - Function overloading feature
def fun1(*args):
 if len(args)==1:
  if isinstance(args[0],str):
   return 'hello'+args[0]
  else:
   return args[0] * args[0]
 elif len(args)==2:
  return args[0] * args[1]

print(fun1(10))
print(fun1(10,5))

#Work around 2 for applying polymorphism - Function overloading feature (suggested approach)
#multipledispatch - dispatch decorator
from multipledispatch import dispatch
@dispatch(int)
def fun1(a:int):
 return a * a

@dispatch(str)
def fun1(a:str):
 return a + a

@dispatch(int,int)
def fun1(a:int, b:int):
 return a * b

print(fun1(10))
print(fun1('irfan'))
print(fun1(10,5))

#Polymorphism (Overriding) support in python directly,
# when you have two methods with the same name with same number of args and same type that each perform different tasks
# then it is overriding, the overrided method provides your own implementation of it.

class overridebase:
 land=100000
 def business(self,invest):
  return invest+(invest*.20)

objoverridederived=overridebase()
print(objoverridederived.business(5000))

class overridederived(overridebase):
 def business(self,invest):
  return invest+(invest*.30)

objoverridederived=overridederived()
print(objoverridederived.land)
print(objoverridederived.business(10000))
#print(objoverridederived.business1(10000))

#4. Encapsulation - Hiding/Restrict of things (code/implementation)
print("Encapsulation Examples")
class bank:
 __banklocker=100000 #private
 def __locker(self):
  print("100 lines of logic")
 _managerroom="protected manager" #protected
 reception="chairs" #public
 def manager_open_locker(self,withdrawal):
  return self.__banklocker-(self.__banklocker-withdrawal)

#protected example
class bankstaff(bank):#other oops languages like cpp,java,scala this is the way it works
 def member1(self):
#  return self._managerroom #in other prog languages, protected members are allowed only through the member/derived classes
#  return self.__banklocker #Python and all other oops languages will not allow private members to be accessed by inherited or instanciated objects., only through the other members of the class we can access
  return self.manager_open_locker(10000)

objstaffcustomer=bankstaff()
print(objstaffcustomer.member1())


objcustomer=bank()
print(objcustomer.reception)
print(objcustomer._managerroom) #other oops languages like cpp,java,scala this won't work, but python is weak in encapsulation - protected access specifier
#print(objcustomer.__banklocker-(__banklocker-20000)) #since private members can be only accessed by the other members of the class, hence we can't access directly
print(objcustomer.manager_open_locker(20000))

#Basic OOPS
print("Constructor is the instantiation of the class in memory by constructing class without attributes, with non parameterized or parameterized attributes")
print("default constructor")
class class_a:
 x=10 #internally this x will be placed inside the init
 def fun1(self,a,b):
  return a+b+self.x

obj_a=class_a() #construct the class in memory (constructor) and referred using an object

print("non parameterized constructor")
class class_b:
 def __init__(self):
  self.x=10
 def fun1(self,a,b):
  return a+b+self.x

obj_b=class_b() #construct the class in memory (constructor) and referred using an object
print(obj_b.fun1(5,7))

print("parameterized constructor")
class class_c:
 def __init__(self,xx):
  self.x=xx
 def fun1(self,a,b):
  return a+b+self.x

obj_c=class_c(10) #construct the class in memory (constructor) and referred using an object
print(obj_c.fun1(5,7))

obj_c=class_c(20) #construct the class in memory (constructor) and referred using an object
print(obj_c.fun1(5,7))

#Types of Methods in Python using Decorators
print("Instance Method")
#1. Instance Method (most Regularly used method) - class attributes can be accessed only by instantiating the class
class class_d:
 x=10
 def fun1(self,a,b): #Instance Method
  return a+b+self.x

obj_d=class_d()
print(obj_d.fun1(10,20))
#class_d.fun1(10,20)

#2. Static Method (least regularly used method) - class attributes can't be accessed
print("Static Method")
class class_e:
 x=10
 @staticmethod
 def fun1(queuename): #Static Method get instantiated prematurely when the class is defined and it won't wait till the class to instantiate
  if queuename=='grocery':
   return 1
  elif queuename=='stationary':
   return 2
  else:
   return 3

#obj_d=class_e()
print(class_e.fun1("grocery"))
print(class_e.fun1("stationary"))

#3. Class Method (rarely used method) - class attributes can be accessed without instantiating the class
print("Class Method")
class class_f:
 x=10
 @classmethod
 def fun1(cls,queuename): #Class Method
  if queuename=='grocery':
   return 1+cls.x
  elif queuename=='stationary':
   return 2+cls.x
  else:
   return 3+cls.x

#obj_d=class_f()
print(class_f.fun1("grocery"))
print(class_f.fun1("stationary"))