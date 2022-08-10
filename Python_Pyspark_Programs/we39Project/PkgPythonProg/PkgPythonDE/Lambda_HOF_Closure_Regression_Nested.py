#If I invoke the functions directly as given below we have couple of challenges
#1. Everytime the function will be loaded in memory and cleaned - hence inefficient
#2. I can't have the functions with same name that can do different operations or I can't modify the functions functionality
#3. I can't reuse the functions more efficiently
#4. Lesser security
from PkgPythonProg.PkgPythonDev.Function_Based_Prog import *
print("HR Dept need to create mail id")
day1lst=[('md','irfan','@inceptez.com'),('venkat','ravi','@cts.com')]

for i in day1lst:
    print(generate_mail(i[0],i[1],i[2]))

day2lst=[('md','basith','@inceptez.com'),('sri','damo','@cts.com')]
for i in day2lst:
    print(generate_mail(i[0],i[1],i[2]))

print("Marketing Dept need to create mail id")

day2lst=[('md','basith','@inceptez.com'),('sri','damo','@CTS.com')]
for i in day2lst:
    print(generate_mail(i[0],i[1],i[2].lower()))


print("repeatedly called, but not used commonly")
generate_mail1=lambda fname,lname,domain:fname+lname+domain #repeatedly called, but not used commonly
#def generate_mail1(fname,lname,domain):
# return fname+lname+domain
day2lst=[('md','basith','@inceptez.com'),('sri','damo','@cts.com')]
for i in day2lst:
    print(generate_mail1(i[0],i[1],i[2]))
day3lst=[('md','basith','@inceptez.com'),('sri','damo','@cts.com')]
for i in day3lst:
    print(generate_mail1(i[0],i[1],i[2]))

#Can we apply positional, keyword, default, arbitrary, arbitrary keyword in Lambda
#Can we have more than one line of coding logic implemented in lambda
generate_mail_lambda=lambda fname,lname,domain:fname+lname+domain
generate_mail_lambda('sri','damo','@cts.com')#positional
generate_mail_lambda(fname='sri',domain='@cts.com',lname='damo')#keyword
generate_mail_lambda_default=lambda fname,lname,domain='@inceptez.com':fname+lname+domain
generate_mail_lambda_default(lname='damo',fname='sri')#default
generate_mail_lambda_default_arbit=lambda *args:args[0]+args[1]+args[2]
generate_mail_lambda_default_arbit('sri','damo','@cts.com')#arbitrary
generate_mail_lambda_default_arbit_kw=lambda **kwargs:kwargs['fname']+kwargs['lname']+kwargs['domain']
generate_mail_lambda_default_arbit_kw(fname='sri',domain='@cts.com',lname='damo')#arbitrary Keyword Arguments

#Can we have more than one line of coding logic or more than one expression inside the lambda: No
generate_mail1=lambda fname,lname,domain:(fname+lname+domain).lower()

#Can we create lambda fn in reg fn - Nested Function- a function inside another function
def generate_mail_lambda_inside(fname,lname,domain): #for repeated and common usage
    lam_func=lambda x:x.lower()
    dom=lam_func(domain)
    return fname+lname+dom
print(generate_mail_lambda_inside('md','irfan','@INCEPTEz.com'))

#Can we pass lambda fn into a reg fn
#higher order function
lam_func1=lambda x:x.lower()
lam_func2=lambda x:x.upper()
def generate_mail_lambda_outside(fname,lname,domain,lam_func_arg): #for repeated and common usage
    dom=lam_func_arg(domain)
    return fname+lname+dom
print(generate_mail_lambda_outside('md','irfan','@INCEPTEz.com',lam_func1))
print(generate_mail_lambda_outside('md','irfan','@INCEPTEz.com',lam_func2))

#Can we call a function passing collection as argument or can we get the collection as a result
generate_mail1=lambda fname,lname,domain:{fname+lname:fname+lname+domain[0]}
print(generate_mail1('md','irfan',['@inceptez.com']))

#Can we call a lambda function using looping construct or built in def functions to achieve some functionality
lst_purchase=list([10000,20000,25000,30000])
add_surcharge=lambda purchase:purchase+(purchase*.01)
lst_surcharge=[]
for i in lst_purchase:
    lst_surcharge.append(add_surcharge(i))
#or
lst_surcharge=list(map(add_surcharge,lst_purchase))

print("Higher order Function")
#A function that takes another function as an argument or A function that returns another function, then it is higher order functions
#below eg shows the calc_sal reg. function is taking incentive or deduction lambda functions as an argument, so calc_sal is a HOF
incentive=lambda sal,incen:sal+incen
deduction=lambda sal,deduct:sal-deduct

def calc_sal(sal,bonus,deduct_incentive,funcname):
 bonus_sal=sal+bonus
 incentive_deduct_bonus_val=funcname(bonus_sal,deduct_incentive)
 print("incentive applied or deduction applied salary bonus is {}".format(incentive_deduct_bonus_val))
 return incentive_deduct_bonus_val

calc_sal(10000,1000,500,incentive)
calc_sal(10000,1000,500,deduction)

#HOF example 2 - check whether map is a higher order function or not?
lst_purchase=list([10000,20000,25000,30000])
add_surcharge=lambda purchase:purchase+(purchase*.01)
give_rebate=lambda purchase:(purchase,purchase-(purchase-(purchase*.02)))
lst_surcharge=[]
lst_surcharge=list(map(add_surcharge,lst_purchase))
lst_offeramt=[]
lst_offeramt=list(map(give_rebate,lst_purchase))

#Single Example to understand, Closure, Nested Function,HOF

def sal_hike(sal,hike):
 salhike=sal+hike
 def incentives(incentive): # Closure Function- the value salhike derived/declared outside of the incentives function is going to change the result of the incentive function, we call this concept as "Closure"
  return salhike+incentive # Nested Function- a function inside another function
 return incentives # HOF- a function is returned from another function

incenfunc=sal_hike(10000,1000)
incenfunc(500)

#Recursive Functions