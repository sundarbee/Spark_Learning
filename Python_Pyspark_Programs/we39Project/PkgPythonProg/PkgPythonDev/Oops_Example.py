#Difference between direct FBP and Basic OOPS + FBP
def f1(self,a):
    return self+a

print(f1(10,20))
print(f1(20,20))

class cls1:
    def f1(self,a):
        return a-a
class cls2:
    def f1(self,a):
        return a+a
objmem1=cls1() #class loaded in memory along with his functions if i use () to create object.
print(objmem1.f1(10))
print(objmem1.f1(20))
print(objmem1.f1(30))

objmem2=cls2() #class loaded in memory along with his functions if i use () to create object.
print(objmem2.f1(10))
print(objmem2.f1(20))
print(objmem2.f1(30))

#Difference between direct FBP and complete OOPS + FBP features
#OOPS - Inheritance (Single, Multiple, Multilevel, Hierarchical), Polymorphism(Overloading, Overriding), Abstraction(Abstract class, methods), Encapsulation (access specifiers public, protected, private)
#
#1. Inheritance
# No Inheritance
class father:
    land=200000 #Not used
    def func1(self,a,b):
        return a+b
class son:
    land=300000 #to buy this land by the son, he spends earn of time to earn the amount by putting hard efforts
    earnmoney=200000
    def func(self):
        print("Son constructed the house with land he purchased and with the money he earned {} ".format(self.land+self.earnmoney))

objSon=son()
print("No Inheritance")
print(objSon.land)
print(objSon.earnmoney)

#1. Single Inheritance
# Base class
class Father:
    land=200000
    def func1(self):
        return self.land
# Derived class
class Son(Father):
    earnmoney = 100000#Son constructed the house with land father purchased and with the money he earned with the hard effort
    def func(self):
        print("Invoking the land from the father with the value of ",self.land," to construct the house with the amount he earned -",self.earnmoney)
print("Single Inheritance")
objSonFather=Son();
objSonFather.func();
objSonFather.func1();

#2. Multiple Inheritance
#Base Class1
class Father:
    land=200000

#Base Class2
class Mother:
    earnmoney=100000

# Derived class
class Son(Father,Mother):
    #earnmoney = 100000 #Son constructed the house with land father purchased and with the money mother earned
    earnmoney=300000
    interior=10000
    def func(self):
        print("Invoking the land from the father with the value of ",self.land,
              " to construct the house with the amount of his mother earned -",self.earnmoney," Interior amount Son earned",self.interior)
#self variable used above gets access to members of the son class as well as all the classes son class has inherited, here Father and Mother class

obj1=Mother()

print("Multiple Inheritance")
objSonFatherMother=Son();
print(objSonFatherMother.land)
print(objSonFatherMother.func())

#3. Hierarchical Inheritance
#Base Class1
class Father:
    land=200000
    earnmoney = 100000

#Derived Class1
class Son1(Father):
    def func(self):
        print("Invoking the land from the father with the value of ",self.land)

# Derived class2
class Son2(Father):
    def func(self):
        print("Invoking the money from the father with the value of ",self.earnmoney)

obj1=Mother()

print("Multiple Inheritance")
objSon1=Son1();
objSon1.func()
objSon2=Son1();
objSon2.func()


#4. Multilevel Inheritance
#Base Class1
class Grandfather:
    land=200000

#Derived Class1
class Father(Grandfather):
    earnmoney=100000

# Derived class2
class Son(Father):
    def func(self):
        print("Invoking the money from the father with the value of ",self.earnmoney,"and land from grandfather",self.land)

objSonFatherGrandFather=Son()
print("Multilevel Inheritance")
objSonFatherGrandFather.func()

#Hybrid Inheritance - Diamond problem will occur (interview question we will discuss)

#2. Polymorphism - If a function takes different forms or it shows his different faces based on the input that i pass
#a. Overloading - Function with same name but different in number of arguments or different types of arguments

#Python doesn't support overloading directly because of it is a dynamically typed language
class cls1:
    def f1(self,x:int):
     return x+x
    def f1(self,x:str): # above function has been overwrittern by this function
     return x.upper()
    def f1(self,y:int,z:int): #only this function is in existance, rest of the above 2 are ignored
     return y+z

obj1=cls1()
#print(obj1.f1(10))
#print(obj1.f1('irfan'))
print(obj1.f1(10,20))

#workaround 1 - To support overloading, use arbitrary argument and conditional structure (not a suggested methodology)
class cls1:
    def f1(self,*x):
     if len(x)==1:
         if isinstance(x[0],str):
             return x[0].upper()
         else:
             return x[0]+x[0]
     elif len(x)==2:
         return x[0]+x[1]
     else:
         return None

obj1=cls1()
print(obj1.f1('hello'))
print(obj1.f1(10))
print(obj1.f1(10,20))

#workaround 2 - To support overloading, use decorators - suggested feature.
# What is decorator - If a function requires additional functionalities which is achieved with the help of
# another function rather modifying the current function that is called decorators in Python
def decor(fun):
    print("since python doesn't support directly the overloading, this decorator function is going to help achieving it by decorating")
    print(fun())
    return fun #decorated function will be returned

@decor
def myfun():
    return 'my function hello'
print(myfun())

#Python doesn't support overloading directly because of it is a dynamically typed language
from multipledispatch import dispatch
class cls1:
    @dispatch(int)
    def f1(self,x):
     return x+x
    @dispatch(str)
    def f1(self,x): # because of dispatch decorator, the above function hasn't been overwrittern by this function
     return x.upper()
    @dispatch(int,int)
    def f1(self,y,z): #all the above functions are going to be considered because of the decorator dispatch
     return y+z

print("using multiple dispatch decorator function we are achieving overloading")
obj1=cls1()
print(obj1.f1(10))
print(obj1.f1('irfan'))
print(obj1.f1(10,20))

#b. Overriding - Function with same name but different in functionality, achieved using overriding
class father:
    land=100000
    def car(self):
        return 'drive'
    def business(self,invest):
        return invest+(invest*.20)

class son(father):
    land = 200000 #attribute overriding
    def business(self,invest): #method overriding
        return invest+(invest*.30)

objson=son()
objfather=father()
print(objson.car())
print(objson.business(100000))
print(objfather.business(100000))

#3. Abstraction: Hiding of the core functions and providing only the results of the functionality
#lets discuss about abstract class concept and abstract method concept
#normal class can be instantiated and used directly
class normal_cls:
    def fun1(self,a,b):
        return a+b

obj_nc=normal_cls()
obj_nc.fun1(10,20)

#What is Abstract class - if a class that inherits the ABC class and if it contains atleast 1 abstract method, we call it as abstract class
#1. An Abstract class can't be instantiated directly, only throgh the derived class it can be instantiated
# Eg. we can't use the internal part (abstract class/methods) of a tv remote directly,
# rather we have to wrap it with some cover and buttons (inherited class)
#2. All un implemented functions inside the abstract class has to be implemented in the derived class (abstract class is forcing to use some functionlatities)
from abc import ABC,abstractmethod ##concepts used here? module, class, method
class abstract_class(ABC): #concepts used here? inheritance (single)
    @abstractmethod      # concepts used here? decorator
    def fun1(self,a,b):
        pass
print("Trying to instantiate the abstract class")
#obj_dc=abstract_class() #can't be done
#obj_dc.fun1(10,20)
#TypeError: Can't instantiate abstract class abstract_cls with abstract methods fun1

class derived_class(abstract_class): # concepts used here? multilevel
    def fun1(self,a,b): # concepts used here? overriding
        return a+b
    a=100;

print("Trying to instantiate the derived class contains implementation/overriding of the abstract methods")

obj_dc=derived_class()
obj_dc.fun1(10,20)


print("I am going to develop a remote functionality without abstracting the core functions")
class remote:
    def power(self,press):
        if press:
            return 'on'
        else:
            return 'off'
    def up_down(self,press):
        if press:
            return 'up'
        else:
            return 'down'


class tv_remote(remote): #hierarchical
    def hd(self,press):
        return 'on'

class ac_remote(remote): #hierarchical
    def humidity_ctrl(self):
        return 'on'
    def turbo(self,press):
        if press:
            return 'turbo mode on'
        else:
            return 'turbo mode off'

print("No abstraction, remote class is open to instantiate")
obj_remote=remote()
print(obj_remote.power(True)) #no abstraction
print(obj_remote.up_down(True)) #no abstraction
#obj_remote.humidity_ctrl(True) #no abstraction

print("through the tv_remote also we can access tv")
obj_tv=tv_remote()
print(obj_tv.power(True))
print(obj_tv.hd(True))
print("through the ac_remote also we can access tv")
obj_ac=ac_remote()
print(obj_ac.power(True))
print(obj_ac.humidity_ctrl())

print("I am going to develop a remote functionality by abstracting the core functions")
from abc import ABC
class remote(ABC):
    @abstractmethod
    def power(self,press): #un implemented function
        pass
    def up_down(self,press):
        if press:
            return 'up'
        else:
            return 'down'


class tv_remote(remote): #hierarchical
    def power(self,press): #power function must be implemented
        if press:
            return 'on'
        else:
            return 'off'
    def hd(self,press):
        return 'on'

class ac_remote(remote): #hierarchical
    def power(self,press):
        if press:
            return 'on'
        else:
            return 'off'
    def humidity_ctrl(self):
        return 'on'
    def turbo(self,press):
        if press:
            return 'turbo mode on'
        else:
            return 'turbo mode off'

print("Abstraction, remote class is open to instantiate")
#obj_remote=remote()
#print(obj_remote.power(True)) #no abstraction
#print(obj_remote.up_down(True)) #no abstraction
#obj_remote.humidity_ctrl(True) #no abstraction

print("through the tv_remote also we can access tv")
obj_tv=tv_remote()
print(obj_tv.power(True))
print(obj_tv.hd(True))
print(obj_tv.up_down(True))
print("through the ac_remote also we can access tv")
obj_ac=ac_remote()
print(obj_ac.power(True))
print(obj_ac.humidity_ctrl())

#4. Encapsulation - hiding or controlling the access of the attributes or functions inside the class
# 3 types of access specifiers are there public,private,protected
#python has weak encapsulation wrt protected, good in public or private

class bank:
    #__locker=100000
    __locker = 100000
    def __fun_locker(self,amt_to_withdraw,passwd):
        __passwd='bank@123'
        locker=self.__locker
        if __passwd==passwd:
            return locker-(locker-amt_to_withdraw)
        else:
            return 0
    _manager="meeting the manager" #Protected is used lightly only for representation purpose
    def accountant(self,amt_to_withdraw):
        return self.__fun_locker(amt_to_withdraw,'bank@123')
    reception="reception"

obj1=bank()
print("Public member is accessed")
print(obj1.reception)
print("Protected member is accessed")
print(obj1._manager)
print(obj1.accountant(10000))
#print(obj1.__fun_locker(10000,'bank@123'))


#GOLDER WORDS for learning OOPS-
# FORGET EVERYTHING we learned in OOPS (Inheritance, polymorphism, abstraction, encapsulation):)
# Never FORGET what we learned in basic OOPS (pkg, subpkg, modules, Classes, Function, Object, constructors):)
# Few more stuffs to not forget - constructors, special types of class functions (importantly 1 class functions (instance method) we need to know)

#Constructors in Python - Default, parameterized, non-parameterized
# Default constructor
class cls1:
    a=100
obj1=cls1()
print(obj1.a)

#non-parameterized
class cls1:
    def __init__(self):
     self.a=200
obj1=cls1()
print(obj1.a)

#parameterized
class cls1:
    def __init__(self,x):
     self.a=x

obj1=cls1(300)
print(obj1.a)

obj2=cls1(200)
print(obj2.a)


#special types of class functions (importantly 2 class functions we need to know)
#Instance Method, Static Method & Class Method

a=100
def fun1(b):
    return a*b
print(fun1(10))

print("1. Instance Method - common way of defining functions inside the class")
class cls_ins():
    def __init__(self):
        self.aa=100
    def ins(self,b): #Instance method
        return self.aa*b
# Two things to consider
#1. the class has to be instantiated to access the functions
#2. we have to use the self argument to access the class attributes.
obj_ins=cls_ins()
print(obj_ins.ins(10))

print("2. Static Method - moderately used functions inside the class when we need to define some staticaly defined functions")
class cls_static():
    def __init__(self,aa):
        self.aa=aa
    @staticmethod
    def stat(b): #static/standalone method
        if b==1:
            return 'on'
        else:
            return 'off'
# Two things to consider
#1. the class is not required to be instantiated to access the functions
#2. we don't use self argument to access the class attributes or we can't access the attributes of the class at all.
#obj_ins=cls_ins()
print(cls_static.stat(10))

print("3. Class Method - rarely used functions inside the class when we need to define some staticaly defined classes and functions")
class cls_method():
    aa=1
    @classmethod
    def clsfunc(cls,b): #static class and method
        if b==cls.aa:
            return 'on'
        else:
            return 'off'
# Two things to consider
#1. the class is not required to be instantiated to access the functions
#2. we have to use the cls argument to access the static class attributes using cls argument.
#obj_ins=cls_ins()
print(cls_method.clsfunc(1))