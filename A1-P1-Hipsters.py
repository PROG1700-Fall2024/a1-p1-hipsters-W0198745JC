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
    print("Hipster's Local Vinyl Records - Customer Order Details")
    print("")    
#input variable customers name
    custName=input("Enter the customers name: ")
#input variable number of kms 
    kms=input("Enter the distance in kilometers for delivery: ")
    pricePerKm=15  #realized this needed its own variable for later calculations.
#input variable cost of records purchased
    recordsCost=input("Enter the cost of records purchased: ")
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
    print("")
    print("Purchase Summary for {0}".format(custName))
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))
    print("Records sales (tx included): ${0:.2f}".format(totalCost))
    print("Total cost : ${0:.2f}".format(finalSalePrice))

#had issues initially connecting to Git Hub so I lost all my commit and Push as it was committing and pushing to my one drive ... I figured it out but i had already finished the program.

    # YOUR CODE ENDS HERE

main()