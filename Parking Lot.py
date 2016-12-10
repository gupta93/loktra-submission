
################################# Parking Lot Design    #############################################################



#### Manaeger class wil handle everything   ################
class Manager:
    total_count_of_vehicle = 0
    lot = None

    def __init__(self):

    # parking lot object
    # parking space object correspondin to that parking lot


    def createVehicleDetails(self):

    ### will create a Vehicle object according to the type(Car,Bike,Truck)


    def park(self):

    #### will call the ParkingLot method to get a parkin space
    def unpark(self):


### will call the ParkingLot method to empty a parking space



########### ParkingLot class can have many Parking Spaces object for extensibilty
class ParkingLot:



    lots = []
    def __init__(self):


    def assignParkinSpace(self,obj):


    #### will assign the parkin space object to the parking lot object

    def getParkinSpace(self):

        ##### will get the parking spot from the parking space object and return true/false

    def removeParkingSpace(self):

        ### will empty a parkin space



####### Parking Space will have Level class obbjects as ParkingSpace has different levels of parking
class ParkinSpace:
    space = []  # will contain level objects

    def __init__(self):


    def getLevel(self, level_obj):

        # will take a level object and assign it to the current ParkingSpace object




    def findSpace(self, vehilcle):



            # will go through the spaces list and find type of vehicle and no of parking spot it needs




#### ParkingSpot will give a grid of spots having properties such as type of grid(Car,Bike,Truck) and no of unit it can hold of that type
class ParkingSpot:
    ##  vehicle_type = ''
    ##  no_of_unit = 0
    ## status will indicate if the spot is empty or not
    ##  vehicle_id  indicate the vehicle it will be holding as required when unparkin a vehicle


    def __init__(self, vtype, num):

#### will create a spot object having above defined properties





############# Vehicle Class can have sub classes #######################
class Vehicle:

    #total_count = 0

    units = 0

    def __init__(self,count):

        # count = no of spots it needs

class Car(Vehicle):

    type = 'C'
    def __init__(self,count):

        Vehicle.__init__(self,count)
        # self.type = Car.type


class Bike(Vehicle):
    type = 'B'

    def __init__(self, count):
        Vehicle.__init__(self,count)
        # self.type = Car.type

class BigVehicle(Vehicle):
    type = 'V'

    def __init__(self, count):
        Vehicle.__init__(self,count)
        # self.type = Car.type














