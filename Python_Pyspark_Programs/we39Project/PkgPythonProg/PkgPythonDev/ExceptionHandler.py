#everybody do this in their project
#exit(1)
#example 0 - bare minimum everyone has to know is the below 4 lines for learning exception handling
print("example 0 - bare minimum everyone has to know is the below 4 lines for learning exception handling")
try:
 print(10+20)
except Exception as err:
 print("exception occured {}".format(err))

#import sys
'''Blocks of Exception Handling? try, except, else, finally
1. Inorder to enable exception handler in our code we have start write the code inside try block
2. try should be used with either except or finally block
try+except or try+finally or try+except+else or try+except+else+finally
'''
print("Exception Example 1 - Simple example")
try: # block where i will write my regular code, where i have opportunities for getting exceptions
 print("Irfan is trying to purchase prod1")
 print("Irfan is trying to purchase prod2")
# print("Irfan have his purse")
 print("Irfan lost his purse"+10)
 print("continue purchasing n number of products")
except Exception as err_msg: #handler code runs when any exception occured in the try block code
 print("I will be printed, In case any one of the line of code failed in try block")
 print("continue purchasing of n number of products despite of error - {}".format(err_msg))
 print("I lost my purse, I still will pay with gpay")
else: #If no exception occured or if the control didn't go to except block, then else block will be called
 print("I will be printed, In case if everything goes fine in the try block")
 print("I will be billing the products i purchased and will be in a happy path")
finally:
 print("Executes at any cost whether try is successfull or except block is called or else block is called, try +except+finally or try+else+finally")
 print("Shop keeper - I completed my purchase, I am going home taking the product, thanks for service")
 print("Shop keeper - I lost my purse, I am going home keeping the product in the rack/basket itself, thanks for understanding")

print("Exception Example 2 - block level exception, we use regularly")
#lets learn about the statement level and block level exception concept using different types of exceptions
#below code is an example for block level exception
try:
 print("enter numerator - total profit")
 n=int(input())
 print("enter denominator - number of share holders")
 d=int(input())
 print("Lets calculate the divident")
 res=n/d #logic 1 calculating the divident
 print("Divident is completed with the result {} and program completed successfully".format(res))
 lst=list(['usd','sgd','ind'])
 print("enter the currency you want to pay the shareholder")
 idx=int(input())
 currency=lst[idx] #logic 2
 print("currency value identified as {0} , so paying the share holder with the currency {0} with an amount of {1} and the program completed successfully ".format(currency,res))
except ZeroDivisionError as exvalue:
 print("There is an exception occured with the message of - {}".format(exvalue))
 res=n/1
 print("system generated result is {} ".format(res))
except IndexError as exvalue:
 print("There is an exception occured with the message of - {}".format(exvalue))
 aa = lst[len(lst)-1]
 print(aa)
except Exception as exvalue:
 print("There is an exception occured with the message of - {}".format(exvalue))
else:
 print("No exception occured, closing the program with a success status")
 print("send success mail")
finally:
 print("whether the program completed successfully or exception occured or no exception with else clause occured, I will be running at any cost")
 print("Good bye")


print("Exception Example 3 - statement level exception")
#lets learn about the statement level and block level exception concept using different types of exceptions
#below code is an example for statement level exception
try:
 print("enter numerator - total profit")
 n=int(input())
 print("enter denominator - number of share holders")
 d=int(input())
 print("Lets calculate the divident")
 res=n/d #logic 1 calculating the divident
 print("Divident is completed with the result {} and program completed successfully".format(res))
except ZeroDivisionError as exvalue:
 print("There is an exception occured with the message of - {}".format(exvalue))
 res = n / 1
 print("Entire amout goes to one share holder {} ".format(res))
except Exception as exvalue:
    print("There is an exception occured with the message of - {}".format(exvalue))
try:
 lst=list(['usd','sgd','ind'])
 print("enter the currency to identify")
 idx=int(input())
 currency=lst[idx] #logic 2
# print("currency value identified as {0} , so paying the share holder with the currency {0} with an amount of {1} and the program completed successfully ".format(currency,res))
 print("currency value identified as {0}".format(currency))
except IndexError as exvalue:
 print("There is an exception occured with the message of - {}".format(exvalue))
 aa = lst[len(lst)-1]
 print(aa)
except Exception as exvalue:
 print("There is an exception occured with the message of - {}".format(exvalue))
else:
 print("No exception occured, closing the program with a success status")
 print("send success mail")
finally:
 print("whether the program completed successfully or exception occured or no exception with else clause occured, I will be running at any cost")
 print("Good bye")

print("Exception Example 4 - How to avoid exception")
#lets learn about the statement level and block level exception concept using different types of exceptions
#below code is an example for statement level exception
try:
 print("enter numerator should be number - total profit")
 n=int(input())
 print("enter denominator should be number - number of share holders")
 d=int(input())
 print("Lets calculate the divident")
 if d != 0:
  res=n/d #logic 1 calculating the divident
  print("Divident is completed with the result {} and program completed successfully".format(res))
 else:
  res=n/1
  print("Divident is completed with the default result {} and program completed successfully".format(res))
except Exception as exvalue:
 print("There is a common exception occured with the message of - {}".format(exvalue))
else:
 print("No exception occured, closing the program with a success status")
 print("send success mail")
finally:
 print("whether the program completed successfully or exception occured or no exception with else clause occured, I will be running at any cost")
 print("Good bye")

print("Exception Example 5 - How to raise exception")
#lets learn about the statement level and block level exception concept using different types of exceptions
#below code is an example for statement level exception
try:
 print("enter numerator should be number - total profit")
 n=int(input())
 print("enter denominator should be number - number of share holders")
 d=int(input())
 print("Lets calculate the divident")
 if d > 1:
  res=n/d #logic 1 calculating the divident
  print("Divident is completed with the result {} and program completed successfully".format(res))
 else:
  print("Since this is a pvt ltd or public ltd and not properatory ltd hence Divident can't be calculated for less than 2 shareholders".format(res))
  if d==0:
   raise ZeroDivisionError
  else:#user defined exception
   raise Exception
except ZeroDivisionError as exvalue:
 print("There is a zero division exception occured with the message of - {}".format(exvalue))
 sys.exit(0)
except Exception as exvalue:
 print("There is a common exception occured with the message of - {}".format(exvalue))
 exit(1)
else:
 print("No exception occured, closing the program with a success status")
 print("send success mail")
finally:
 print("whether the program completed successfully or exception occured or no exception with else clause occured, I will be running at any cost")
 print("Good bye")