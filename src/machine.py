class Machine(object):
    def __init__(self, building=None, floor=None, number=None, 
                 controller=None, code=None):
        self.buildingName = building
        self.floor = floor
        self.machineNumber = number
        self.controller = controller
        self.cscCode = code

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.buildingName, self.floor, 
                                       self.machineNumber, self.controller
                                       self.cscCode)