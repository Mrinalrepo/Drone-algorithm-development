from geopy.geocoders import Nominatim
from math import sin, cos, sqrt, atan2, radians
#location class
class Location():
    def getLatLong(self,loca):
        self.loca=loca
        locator = Nominatim(user_agent="All")
        location = locator.geocode(self.loca)
        self.latitude=location.latitude
        self.longitude=location.longitude
        return [self.latitude,self.longitude]
    def getWeatherCond(self):
        return "Good"

#drone class
class Drone(Location):

    Drone_id="xyz"
    status=0
    Battery=0.0
    Capacity=0.0
    Remaining_capacity=Capacity
    current_location=""
    Travel_dist=0.0
    Point_dist=0.0
    Work_done=0.0
    weather="Good"
    
    
    def getDistance(self):
        
        loc = self.getLatLong("Taj Mahal,India")
        print(loc)
        x1 = loc[0]
        y1 = loc[1]
        
        x2, y2 = self.getLatLong("gwalior fort,India")
        R = 6373.0
        print(x2,y2)
        x1 = radians(x1)
        y1 = radians(y1)
        x2 = radians(x2)
        y2 = radians(y2)
        dlong = y2 - y1
        dlat = x2 - x1
        a = sin(dlat / 2)**2 + cos(x1) * cos(x2) * sin(dlong / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.distance = R * c
        self.Point_dist=self.distance
        return self.distance
    def getOrder(self):
        pass # calculate amount of distance drone can tavel with current battery and store it to Travel_dist
        

    def Capacity():
        pass # calculate remaining capacity of drone and store it to Remaining_capacity

class Cost_Calculation():
    Work_done_cost=0.0
    Cost=0.0
    def WorkDone(self):
        pass
    def Cost_calculation(self,Work_done_cost):
        pass

#Station class
class Station(Location,Cost_Calculation):
    def __inti__(self):
        self.station=Station()
        return self.station
    

# Hub class having composition with Station class
class Hub(Location):
    Name=""
    No_of_present_drone=0
    Supplies_status=0
    Order_dist=0.0
    Order_mass=0.0
    weather="Good"
    def __init__(self):
        self.drones=Drone()
    def getDistance(self):
        loc = self.getLatLong("Taj Mahal,India")
        print(loc)
        x1 = loc[0]
        y1 = loc[1]
        x2, y2 = self.getLatLong("gwalior fort,India")
        R = 6373.0
        print(x2,y2)
        x1 = radians(x1)
        y1 = radians(y1)
        x2 = radians(x2)
        y2 = radians(y2)
        dlong = y2 - y1
        dlat = x2 - x1
        a = sin(dlat / 2)**2 + cos(x1) * cos(x2) * sin(dlong / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.distance = R * c
        return self.distance
        

    def getOrder(self,Source_name,Dest_name,Supplies):
        self.Source_name=Source_name
        self.Dest_name=Dest_name
        self.Supplies=Supplies

        pass #   get the item in form of dictionary and store to Supplies

    def efficient_Drone(self):
        
        if(self.drone.Travel_dist>self.Order_dist):
            if(self.drone.Remaining_capacity>self.Order_mass):
                return self.drone.Drone_id



    def setDelivery(self):
        self.cost_calc=Cost_Calculation()
        cost=self.cost_calc.WorkDone(self.Supplies,self.drone.Drone_id)
        return cost
    def getMass(self):
        weight=0
        for supply in Supplies.values():
            weight=weight+supply
        return weight

    def suppliesStatus(self):
        weight=0;
        for supply in Supplies.values():
            weight+=supply
        if(weight>0):
            return 1
        else:
            return 0
    
    





dist1=Drone()
dist=dist1.getDistance()
print(dist," kilometer")
