

"""
To run this script, type

  python buyLotsOfFruit.py
  
Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75, 'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples
            
    Returns cost of order
    """ 
    totalCost = 0.0             
    "*** YOUR CODE HERE ***"
    for x in range(0,len(orderList)):
        for y in range(0, len(orderList)+2):
            if orderList[x][0] == fruitPrices.keys()[y]:
                totalCost+=(orderList[x][1])*fruitPrices[orderList[x][0]]
                break
            elif y == 4:
                print "\nError, fruit does not exist"
                return None
    
    return totalCost    
    
                
                
  
        
    
    
    
    
    
# Main Method    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    print 'Cost of', orderList, 'is', buyLotsOfFruit(orderList)