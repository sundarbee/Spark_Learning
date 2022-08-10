from abc import ABC,abstractmethod
class clsa(ABC):
    @abstractmethod
    def x(self,a):
        pass
class clsb(clsa):
    def x(self,b):
        return b*b
obj11=clsb().x(100)
class cls1():
    def __init__(self):
        self.a=10
    def x(self,aa):
        pass
class ccls1(cls1):
    def x(self,aa):
        return aa+aa+self.a

if __name__=="__main__":
    obj1=ccls1();
    print(obj1.x(100))
#print(cls1.a)
#print(cls1(10).x(100))

# class cls1():
#     x=100
#     def __init__(self,a):
#         self.a=a
#     def add1(self,b):
#         return self.x+self.a+b
#
# if __name__=="__main__":
#     print(cls1.x)
#     print(cls1(50).add1(100))
#
# from multipledispatch import dispatch
# @dispatch(int, int)
# def f1(a,b):
#  print (a+b)
#
# @dispatch(int, str,str)
# def f1(a,b,c):
#  print( a+int(b)+int(c))
#
# print(f1(10,2))
# print(f1(10,'2','2'))
#
# print("Ducktyping + Function Overloading with difference in number of arguments + Closure example")
# lst = [5,4,2,3,1] #Closure
# def func1() :
#     if lst.count(6) == 1:
#         print("method if block")
#     elif lst.count(5)==1:
#         print("method elif block")
#     else:
#         print("method else block")
#
# func1()
#
# def func1(arg1:int):
#   print ("method with one int argument")
# #func1()
# func1(10)