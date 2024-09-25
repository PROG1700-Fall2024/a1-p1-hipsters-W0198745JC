#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

"""
Student Name:    Jenille Cheney
Program Title:  Hipster's Local Receipt Calculator
Description:    Creating a retro program to calculate a receipt for customers including travel, item cost, and taxes. With inputs
"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#Welcome to program 
    print("Welcome to Hipster's Local Vinyl Records")
    print("This is our receipt generator")    
#input variable customers name
    custName=input("Please enter customers name: ")
#input variable number of kms 
    kms=input("How far is the delivery in kilometers: ")
    pricePerKm=15  #realized this needed its own variable for later calculations.
#input variable cost of records purchased
    recordsCost=input("Please enter the total cost of purchase: ")
#Delivery cost variable
    deliveryCost=int(kms)*pricePerKm
# adding taxes to the cost of purchase
    taxes= 14/100
    totalTax= taxes* float(recordsCost) 
    # had to change cast from int to float
#creating a total cost variable 
    totalCost=totalTax+float(recordsCost) 
    # was initially missing this equation so was displaying just tax not total cost
    finalSalePrice=totalCost+deliveryCost 
#print string using either casting or injection ({0:.2f} for money float value)
    print("{0}'s purchase has".format(custName))
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))
    print("Records sales (tx included): ${0:.2f}".format(totalCost))
    print("Total cost : ${0:.2f}".format(finalSalePrice))


    # YOUR CODE ENDS HERE

main()