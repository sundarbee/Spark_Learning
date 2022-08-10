#from mainroad.street.ShowRoom import suv_innova
#from mainroad.street import ShowRoom

'''import mainroad.street.ShowRoom
SunithaOnRoadObj1=mainroad.street.ShowRoom.suv_innova()
SunithaOnRoadObj2=mainroad.street.ShowRoom.suv_xuv()
'''
'''from mainroad.street.ShowRoom import suv_innova
from mainroad.street.ShowRoom import suv_xuv
from mainroad.street.ShowRoom import *
SunithaOnRoadObj1=suv_innova()
SunithaOnRoadObj2=suv_xuv()
'''

from mainroad.street import ShowRoom
SunithaOnRoadObj1=ShowRoom.suv_innova()
SunithaOnRoadObj2=ShowRoom.suv_xuv()


SunithaOnRoadObj1.fueltype('Diesel')
SunithaOnRoadObj1.cruise()
SunithaOnRoadObj2.fueltype()
SunithaOnRoadObj2.cruise()

#package mathematical->calculation-> calculator.py -> CalcClass -> add/sub/mul functions
#package auditing -> auditor -> profit_loss.py -> object calc_inhand=CalcClass() ->  calc_inhand.add(100,200) -> return 300
