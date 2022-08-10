def func_name(a):
    return a
def func_name(a,b):
    return a+b
print(func_name(10,20));


def generate_email(fname,lname='noname'): #Default Arguments
    return fname+'.'+lname+'@inceptez.com'

#print(func_name())

#print(func_name1(100))

def xyz(x): #common function for every one's usage
    return x + x.lower()+x.upper()

xyz1=lambda x:x.upper()+x.lower() #not supposed to be created commonly, but can be done

#try convert the below program applying closure, HOF, nested function
def optimal_offer(purchase_amount, offer_percent, max_offer_amt):
 offer_amt = purchase_amount*offer_percent
 if (offer_amt > max_offer_amt):
  print("Calculated offer amount is more than the max offer amount, hence returning the max_offer_amt applied total amount");
  return purchase_amount-max_offer_amt
 else:
  print("Calculated offer amount is less than the max offer amount, hence returning the  offer_percent applied total amount");
  return int(purchase_amount-(purchase_amount*offer_percent))

print(optimal_offer(500,.5,200))
print(optimal_offer(300,.5,200))

#scope of the variable
# A global variable is a variable that has scope across the program
# A local variable is a variable that has scope within the function
glob_var='Sun' #any variable declared outside a function is a global variable
def func_room():
 loc_var1='AC' #any variable declared inside a function is a local variable
 print(glob_var,loc_var1)

func_room()
print(loc_var1)#can't be used since it is local

def func_road():
 global loc_var2
 loc_var2='AC' #any variable declared inside a function is a local variable
 print(glob_var,loc_var2)

func_road()
print(loc_var2)#can be used since it is global