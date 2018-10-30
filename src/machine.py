class Machine(object):
    def __init__(self, machine_type=None, building=None, floor=None, 
                 number=None, controller=None, code=None):
        """Initialize the machine object by storing its data in variables
        
        Keyword Arguments:
        - type: "washer" or "dryer"
        - building: the building in which the machine resides
        - floor: the floor of the building in which the machine resides
        - number: the machine number tied to the controller
        - controller: the controller letter for the machine room
        - code: the service request code for CSC CoinMatch
        """
        self.type = machine_type
        self.buildingName = building
        self.floor = floor
        self.machineNumber = number
        self.controller = controller
        self.cscCode = code

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.buildingName, self.floor, 
                                       self.machineNumber, self.controller
                                       self.cscCode)
