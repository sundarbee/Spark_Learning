'''In general'''
#print("Irfan is going to a shop, to purchase some items, he fails inbetween he abruptly close his activity"+str(1/0))
x=1
print("pass the denominator")
y=int(input())
#seperate try/except/else/finally, will handle exception for every statement and ensure all try block statements are executed (with or without exception)
try:
    #assert will help you to raise assertion error alone
    print("first try block")
    assert y != 0 #leads to except block if this assertion fails without meeting the condition
except AssertionError as msg:
    print("In case of any failure ( {} ) in purchase occurs, Irfan is going to handle it in some way".format(msg))
else:
    print("In case no failure in purchase, Irfan is going to run this block for doing something additional to his purchase")
finally:
    print("Whether success or fail of purchase, finally run do something")
try:
    print("second try block")
    print("Irfan is going to a shop, to purchase some items"+ str(x/y))
except ZeroDivisionError as msg:
    print("In case of any failure ( {} ) in purchase occurs, Irfan is going to handle it in some way".format(msg))
else:
    print("In case no failure in purchase, Irfan is going to run this block for doing something additional to his purchase")
finally:
    print("Whether success or fail of purchase, finally run do something")
try:
    print("third try block")
    if x/y > .1:
        raise ArithmeticError #you can raise any type of exception
except ArithmeticError as msg:
    print("In case of any failure ( {} ) in purchase occurs, Irfan is going to handle it in some way".format(msg))
else:
    print("In case no failure in purchase, Irfan is going to run this block for doing something additional to his purchase")
finally:
    print("Whether success or fail of purchase, finally run do something")


#multiple statements in one try, will not continue the rest of the statements if any exception occur inbetween
try:
    #assert will help you to raise assertion error alone
    assert y != 0 #leads to except block if this assertion fails without meeting the condition
    print("Irfan is going to a shop, to purchase some items"+ str(x/y)) #failed will take to line 7 and 11, success will take to 9 and 11
    if x/y > .1:
        raise ArithmeticError #you can raise any type of exception
except Exception as msg:
    print("In case of any failure ( {} ) in purchase occurs, Irfan is going to handle it in some way".format(msg))
else:
    print("In case no failure in purchase, Irfan is going to run this block for doing something additional to his purchase")
finally:
    print("Whether success or fail of purchase, finally run do something")


try:
    sal=10000
    bonus_sal=sal+1000
    print('bonus_sal for an employee {}'.format(bonus_sal))
except Exception as msg:
 print("some exception occured {} , hence routing the call to the agent".format(msg))

try:
    totalleave=30
    bal_leave=totalleave-20
    print('balance leave for an employee {}'.format(bal_leave))
except Exception as msg:
 print("some exception occured {} , hence routing the call to the agent".format(msg))

try:
    sal = 10000
    bonus_sal = sal + 1000
    print('bonus_sal for an employee {}'.format(bonus_sal))
    incentive=bonus_sal+2000
except Exception as msg:
    print("some exception occured {} , hence routing the call to the agent".format(msg))

import sys
try:
 print("Try Block1")
 num1 = 10
 "Strongly typed" + num1
except Exception as msg:
 print("some exception occured {} , hence routing the call to the agent".format(msg))
 #sys.exit(100)

try:
 print("First try block is completed, I am the second try block")
 vowels = ['a', 'e', 'i', 'o', 'u']
 print(vowels[3])
 lst=['eng','tam','tel']
 print("Enter option 0 for english/1 for tamil/2 for telugu")
 userinput=int(input())
 print('user selected {}'.format(lst[userinput]))
 userinput2=int(input())
 if userinput2==0:
  raise ArithmeticError #user raised exception
 else:
  print(userinput/userinput2)
 print('IVR continue the other options with 10 more lines of code execution in the down')
#except IndexError as msg:
# print("Since user chosen a wrong IVR option and got an error {} , hence routing the call to the agent".format(msg))
except ArithmeticError as msg:
 print("user raised the exception because input chosen is zero")
except Exception as msg:
 print("some exception occured {} , hence routing the call to the agent".format(msg))
else:
 print("Happy to see this program didn't go to the exception block, all the statements are succeeded")
finally:
 print("Finally will be executed any cost, whether exception occured or not")
 print("Close all the db connections")
 print("Have a nice day customer")