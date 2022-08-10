class CarSales:
    gst=.18
    def alto(self,color):
        totalcost=400000+(400000*self.gst)
        return totalcost
    def swift(self,color):
        if color=='red':
            totalcost=850000+(850000*self.gst)
            return totalcost
        else:
            totalcost=800000+(800000*self.gst)
            return totalcost

class CarService:
    gst=.18
    def alto(self,type):
        if type=='complete':
            return 10000++(10000*self.gst)
        elif type=='water':
            return 1000 + +(1000 * self.gst)
        else:
            return 3000 + +(3000 * self.gst)
    def swift(self,type):
        if type=='complete':
            return 15000++(15000*self.gst)
        elif type=='water':
            return 1000 + +(1000 * self.gst)
        else:
            return 5000 + +(5000 * self.gst)

