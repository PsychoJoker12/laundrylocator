#Use pip install xlrd
import xlrd

#define variable linked to excel spreadsheet w data
#to run on your pc you'll have to correct the path
loc = ("/Users/jduval/Documents/GitHub/laundrylocator/src/exampleSheet.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0,0)


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
exampleMachine.buildingName = "AAA"
exampleMachine.floor = 5
exampleMachine.machineNumber = 0;
exampleMachine.cscCode = "xxx-xxx";

exampleMachine.printInfo();

#Example using sheet, should print data on first row of sheet
#We can automate this process later
exampleMachine2 = machine()
row_array = sheet.row_values(1)

exampleMachine2.buildingName = row_array[0]
exampleMachine2.floor = int(row_array[1])
exampleMachine2.machineNumber = int(row_array[2])
exampleMachine2.controller = row_array[3]
exampleMachine2.cscCode = row_array[4]

exampleMachine2.printInfo();
