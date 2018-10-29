class machine():
    def __init__(self):
        self.buildingName = "";
        self.floor = 0;
        self.machineNumber = 0;
        self.controller = "A";
        self.cscCode = "";

    def printInfo(self):
        print(self.buildingName + "-" + str(self.floor) + "-" + str(self.machineNumber) + "-" + self.controller + "-" + self.cscCode);

exampleMachine = machine()
exampleMachine.buildingName = "KER"
exampleMachine.floor = 6
exampleMachine.machineNumber = 1;
exampleMachine.cscCode = "xxx-xxx";

exampleMachine.printInfo();
