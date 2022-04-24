class Employee:
#constructor
    def __init__(self,name,number):
        self.name = name
        self.number = number
#getters and setters
    def getName(self):
        return self.name

    def getNumber(self):
        return self.number
  
    def setName(self,name):
        self.name = name

    def setNumber(self,number):
        self.number = number
  
class ProductionWorker(Employee):
#constructor
    def __init__(self,name,number,shiftNum,hourlyRate):
        super().__init__(name,number)
        self.shiftNum = shiftNum
        self.hourlyRate = hourlyRate
#getters and setters
    def getShiftNum(self):
        return self.shiftNum
  
    def getHourlyRate(self):
        return self.hourlyRate
  
    def setShiftNum(self,shiftNum):
        self.shiftNum = shiftNum
  
    def setHourlyRate(self,hourlyRate):
        self.hourlyRate = hourlyRate
  
def main():
#asking for user inputs
    name = input("Enter employee name: ")
    number = int(input("Enter employee number: "))
    shift = int(input("Enter employee shiftNum(1-Day,2-Night): "))
    rate = float(input("Enter employee's hourly rate: "))
#instantiating an object
    productionWorker = ProductionWorker(name,number,shift,rate)
#printing the details using getter methods
    print('\nEmployee Name:',productionWorker.getName())
    print('Employee Number:',productionWorker.getNumber())
    print('Employee shift number:',productionWorker.getShiftNum())
    print('Employee hour rate:',productionWorker.getHourlyRate())
#calling the main method
main()