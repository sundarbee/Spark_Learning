#generate_mail=lambda fname,lname,domain:
def generate_mail(fname,lname,domain): #for repeated and common usage
    lam_func=lambda x:x.lower() # Nested Function- a function inside another function
    dom=lam_func(domain)
    return fname+lname+dom
print(generate_mail('md','irfan','@INCEPTEz.com'))

#higher order function
lam_func1=lambda x:x.lower()
lam_func2=lambda x:x.upper()
def generate_mail_lambda(fname,lname,domain,lam_func_arg): #for repeated and common usage
    dom=lam_func_arg(domain)
    return fname+lname+dom
print(generate_mail_lambda('md','irfan','@INCEPTEz.com',lam_func1))
print(generate_mail_lambda('md','irfan','@INCEPTEz.com',lam_func2))

#below is not a right practice, lambda functions will be used only with in the module not accross
#generate_mail1=lambda fname,lname,domain:fname+lname+domain #repeatedly called, but not used commonly