#In the commonmodule.py program By adding basic OOPS of keeping the functions inside the class
# def summation(x,y=0):
#     z=x+y
#     print("summation of x and y is {}".format(z))
#     return z
#
# def taxation(x,y=0):
#     z=x-y
#     print("tax reduced salary is {}".format(z))
#     return z
# def summation(x,y=0):
#     z=x+y+10
#     print("summation of x and y is {}".format(z))
#     return z
#The below functions kept with in the class is helping us loading the functions in memory once for all when the class got instantiated
#We can access the respective functions from the respective classes despite it has the same name
class commoncls():
    val1=10#class attributes
    def summation(self,x, y=0):#members
        z = x + y+self.val1
        print("summation of x and y is {}".format(z))
        return z
    def taxation(self,x, y=0):
        z = x - y-self.val1
        print("tax reduced salary is {}".format(z))
        return z

class commoncls1():
    def summation(self,x, y=0):
        z = x + y+10
        print("summation of x and y is {}".format(z))
        return z
    def taxation(self,x, y=0):
        z = x - y-10
        print("tax reduced salary is {}".format(z))
        return z

obj1=commoncls()
x=obj1.summation(y=10,x=20)
y=obj1.summation(10,200)
print(x)
print(y)

obj2=commoncls1()
x=obj2.taxation(y=10,x=20)
y=obj2.taxation(10,200)
print(x)
print(y)
