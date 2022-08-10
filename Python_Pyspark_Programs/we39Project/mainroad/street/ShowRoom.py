class suv_innova:
    cruisemode=False
    def fueltype(self,a):
        print(a)
    def cc(self,a):
        print(a)
    def cruise(self):
        if self.cruisemode:
            print("Innova car has cruise mode")
        else:
            print("Innova doesn't contains cruise mode")
class suv_xuv:
    cruisemode=True
    def fueltype(self,a='Diesel'):
        print('the fuel type is '+a)
    def cc(self,a):
        print(a)
    def cruise(self):
        if self.cruisemode:
            print("car has cruise mode")

class sedan_verna:
    def fueltype(self,a):
        print(a+'+CNG')
    def cc(self,a):
        print(a)
    def voicecontrol(self,a):
        if a:
            print("car has voice control")
