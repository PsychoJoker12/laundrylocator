#Use pip install xlrd
import xlrd

#define variable linked to excel spreadsheet w data
#to run on your pc you'll have to correct the path
loc = ("/Users/jduval/Documents/GitHub/laundrylocator/src/exampleSheet.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0,0)

totalList = []


class machine():
    def __init__(self):
        self.buildingName = "";
        self.floor = 0;
        self.machineNumber = 0;
        self.controller = "A";
        self.cscCode = "";

    def printInfo(self):
        print(self.buildingName + "-" + str(self.floor) + "-" + str(self.machineNumber) + "-" + self.controller + "-" + self.cscCode);

#Looping through data sheet and making array of machines
#set row number to 1 bc list is 0 index
for i in range(1, sheet.nrows):
    machineID = machine()
    row_array = sheet.row_values(i)
    machineID.buildingName = row_array[0]
    machineID.floor = int(row_array[1])
    machineID.machineNumber = int(row_array[2])
    machineID.controller = row_array[3]
    machineID.cscCode = row_array[4]

    totalList.append(machineID.printInfo());

print(totalList)
