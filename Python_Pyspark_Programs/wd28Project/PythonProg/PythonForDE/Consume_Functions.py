#from PythonProg.PythonForDevelopers.FunctionsExample import generate_email
import PythonProg.PythonForDevelopers.FunctionsExample

import sys
print("HRs are going to use the below function")
list_of_emp=[['irfan','md'],['priya'],['b','anand']]
for i in list_of_emp:
    try:
        if len(i)>1:
        #positional arguments
            print('mail id of ' + i[0] + ' ' + i[1] + ' is ' + PythonProg.PythonForDevelopers.FunctionsExample.generate_email(i[0], i[1]))
        #keyword/named arguments
            print('mail id of ' + i[1] + ' ' + i[0] + ' is ' + PythonProg.PythonForDevelopers.FunctionsExample.generate_email(lname=i[0], fname=i[1]))
        else:
            print('mail id of ' + str(i) + ' is ' + PythonProg.PythonForDevelopers.FunctionsExample.generate_email(i[0]))
    except IndexError as idxerr:
        print(" Index error {}".format(idxerr))
        #sys.exit(1)

no_of_emp=3
#for i in range(1,no_of_emp+1):
i=1
while i<=no_of_emp:
    print("enter the {} employee's fname and lname ".format(i))
    a=input("enter fname")
    b=input("enter lname")
    print('mail id of ' + a + ' ' + b + ' is ' + PythonProg.PythonForDevelopers.FunctionsExample.generate_email(a, b))
    print("send_email(PythonProg.PythonForDevelopers.FunctionsExample.generate_email(a, b))")
    i+=1

#   print('mail id of '+a+' '+b+' is '+PythonProg.PythonForDevelopers.FunctionsExample.generate_email(a,b))

#lambda function or anonymous function or function literal or value function
#xyz=lambda x:x.upper()+x.lower()
#PythonProg.PythonForDevelopers.FunctionsExample.xyz('Inceptez')

#if i use the below xyz commonly, then create it as a common python function
# def xyz(x):
#  return x.upper()+x.lower()
#lambda function
xyz=lambda x:x.upper()+x.lower() #anonymous function for current module's usage repeatedly

print(xyz('Inceptez'))
print("some lines of code")
print(xyz('Irfan'))
print("some lines of code")
print(xyz('Python'))

print("some lines of code")
import PythonProg.PythonForDevelopers.FunctionsExample
print(PythonProg.PythonForDevelopers.FunctionsExample.xyz('Python'))

import PythonProg.PythonForDevelopers.FunctionsExample #NOT A RIGHT way to use
print(PythonProg.PythonForDevelopers.FunctionsExample.xyz1('Python')) #NOT A RIGHT way to use

#inline functionality
x='Inceptez'
print(x.upper()+x.lower())
print("some lines of code")

print("Higher Order Function")
