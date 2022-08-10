from PythonProg.PythonForDevelopers import Class_Funct_Module
from PythonProg.PythonForDevelopers.TelephoneModule import Telephone

obj1=Class_Funct_Module.calc()
print(obj1.add(10,20))
print(obj1.sub(20,10))

rotaryobject= Telephone('rotary',10)
print("cost for installion of rotary "+ str(rotaryobject.installationcost(4)))

touchtoneobject= Telephone('touchtone',5)
print("cost for installion rotary "+ str(touchtoneobject.installationcost(3)))

cellobject= Telephone('cell',1)
print("cost for installion cell "+ str(cellobject.installationcost(1)))