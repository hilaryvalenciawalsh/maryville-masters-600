import json

class InventoryItem:

    def __init__( self, itemName ):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
 
    def addToStocked( self, stockAmt ):
        self.totalStocked = self.totalStocked + stockAmt

    def addToInStock( self, inStockAmt ):
        self.totalInStock = self.totalInStock + inStockAmt

    def incrementSlots( self ):
        self.totalSlots = self.totalSlots + 1

    def getNumberSold( self ):
        return self.totalStocked - self.totalInStock
    
    def getSoldPct( self ):
        return self.getNumberSold() / self.totalStocked

    def getStockNeed( self ):
        return 8 * self.totalSlots - self.totalInStock

    def getName( self ):
        return self.name

    def getNumberInStock( self ):
        return self.totalInStock

    def __repr__( self ):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format( self.name, self.totalInStock, self.totalStocked, self.totalSlots )

####machine!
class machineStatus:
    def __init__(self, machName):
        self.name = machName
        self.previousBevStock = 0
        self.currentBevStock = 0
        self.totalIncome = 0.0
     
    def percent(self):
        return (self.previousBevStock - self.currentBevStock) / self.previousBevStock * 100
    
    def income(self, income):
        self.totalIncome = self.totalIncome + income
     
    def lastStock(self, prevBevStock):
        self.previousBevStock = self.previousBevStock + prevBevStock
     
    def beverageStock(self, currentBevStock):
        self.currentBevStock = self.currentBevStock + currentBevStock
     
    def getName(self):
        return self.name
    
    def getCurrentStock(self):
        return self.currentBevStock
    
    def getPrevStock(self):
        return self.previousBevStock
    
    def total(self):
        return self.totalIncome
    
    def __repr__(self):
        return "Name {}, Income {}, Sold Pct {:2f}".format(self.name, self.totalIncome, self.percent())

def main():
    inventoryFileNames = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]
    itemNameToInventoryItem = {}
    machDictionary = {}
  
    for inventoryFileName in inventoryFileNames:
        inventoryFile = open( inventoryFileName, 'r' )
        inventoryData = json.loads( inventoryFile.read() )
        machName = inventoryData['machine_label']
        mach = machDictionary.get( machName, machineStatus(machName) )
        contents = inventoryData['contents']

        for row in contents:
        
            for slot in row['slots']:
                itemName = slot['item_name']
                inventoryItem = itemNameToInventoryItem.get( itemName, InventoryItem( itemName ) )
                inventoryItem.addToStocked( slot['last_stock'] )
                inventoryItem.addToInStock( slot['current_stock'] )
                inventoryItem.incrementSlots();
        
                mach.income(slot['item_price']*(slot['last_stock']-slot['current_stock']))
                mach.lastStock(slot['last_stock'])
                mach.beverageStock(slot['current_stock'])
        
                itemNameToInventoryItem[itemName] = inventoryItem
        
        machDictionary[machName] = mach
    sortChoice = input('Would you like the (m)achine report or (i)nventory report? ')
    inventoryItemsList = list( itemNameToInventoryItem.values() )
    machList = list(machDictionary.values())

   # cokeItem = itemNameToInventoryItem['Coke']
    if sortChoice == 'm':
            print('{:15} {:15} {:10}'.format('Machine Name', 'Percent Sold', 'Sales Total'))
            for item in machList:
                print('{:10} {:10.2f}% ${:8.2f}'.format(item.getName(), item.percent(), item.total()))
    elif sortChoice == 'i':
            while sortChoice != 'q':
                sortChoice = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
  
            # sortChoice = '' this part isn't working.... only if i hit "q" 

            if sortChoice == 'n':
                inventoryItemsList.sort( key=InventoryItem.getName )

            elif sortChoice == 'p':
                inventoryItemsList.sort( key=InventoryItem.getSoldPct )
                inventoryItemsList.reverse()

            elif sortChoice == 's':
                inventoryItemsList.sort( key=InventoryItem.getStockNeed )
                inventoryItemsList.reverse()
            print( 'Item Name      Sold   % Sold   In Stock Stock needs')

            for item in inventoryItemsList:
                print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
            print()  
main()