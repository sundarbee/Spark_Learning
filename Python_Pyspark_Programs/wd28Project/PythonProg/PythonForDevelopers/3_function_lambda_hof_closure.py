print("************** 6. Simple (not keeping in a pkg or classes)/Named reusable Function **************" )

def add(a:int,b:int): #I will call the function as a function if the function is not a member of a class
    print(type(a))
    print("Parameter 1:",a)
    print("Parameter 2:",b)
    return a + b #return is optional - if i dont return the function will act like a procedure (used a subroutine)

print(add(10,20))
print(add("abc","xyz")) # will it work or not? it runs

def add1(a,b): # no need of the input type because python is dynamically typed language.
    print(type(a))
    print("Parameter 1:",a)
    print("Parameter 2:",b)
    a + b #return KEYWORD is mandatory if you need get some return value from the function unlike scala we dont have to mention return keyword

print(add1(10,20))
print(add1("abc","xyz"))

print(" ************** 7. lambda = anonymous function (used within a program, not accross classes/modules) ************** ")
# anonymous functions are functions without name ; they are not defined using "def" keyword
# lambda can take any number of arguments, but can have only one expression
# syntax = lambda <arguments>: <expression>
anonym_lambda_func1=(lambda x,y: x+y) # map(x,y=>x+y)
anonym_lambda_func=(lambda l, b, h: l*b*h)
# print the output in the below placeholder using {} the format function output
print("cubic size: {} ".format(anonym_lambda_func(10,2,5)))
print("cubic size: {} ".format(anonym_lambda_func(5,3,2)))
print("cubic size: {} ".format(anonym_lambda_func(8,6,3)))

lst=[1000,2000,3000,4000,5000]
#print(lst.__add__(lst))
res=map(lambda x:x+100,lst)
for i in list(res):
    print(i)

print(" ************** 8. Higher Order Function  ************** ")
#Higher Order Function
def even_filtering(filter_argument): #normal named function
    if (filter_argument % 2) == 0:
        return True
    else:
        return False

filter_list = [5, 10, 15, 20, 25, 30, 35]
#filter_list.filter(x=>(x%2==0))
#filter(lambda x: (x % 2 == 0), filter_list)
#x=>x equivalent in python is lambda x:x
#Not using higher order method
print("higher order function eg. with even list of values by calling lambda function inside the filter function")
even_object = filter(lambda x: (x % 2 == 0), filter_list) #lambda/anonymous function
#even_object=filter_list.filter(lambda x: (x % 2 == 0))
print(even_object)
print(list(even_object))

print("higher order function eg. with filtered even list calling normal named function: ")
normal_filtering = filter(even_filtering, filter_list)
print(list(normal_filtering))