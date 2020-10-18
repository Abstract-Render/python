# Write a program to calculate a split restaurant check among any number of friends, including tip. Assume that since you're all friends, it's ok to split the check evenly. 
restaurantBill = float(input("Enter restaurant bill "))
salestaxRate = float(input("Enter tax rate "))
serviceRating = int(input("Enter your rating 1-10 "))
numberofPeople = int(input("Enter number of people splitting the check. "))

def calculateTip(Rating):
    if Rating == 10:
        tip = 0.3
    elif  Rating >= 5:
        tip = 0.15
    else:
        tip = 0
    return tip
tip = calculateTip(serviceRating)
def calculateBill():
    return ( restaurantBill/numberofPeople)
def calculateSalesTax():
    return(restaurantBill*salestaxRate)
def calculateTipPerPerson(restaurantBill):
    return (calculateBill()*tip+calculateSalesTax())
def calculateTotalPerPerson(restaurantBill):
    return (calculateBill()+calculateSalesTax())
def calculateTotalBill(restaurantBill):
    return (calculateTotalPerPerson(restaurantBill)+restaurantBill*tip)

print("Bill (with tax) per person: " + str(calculateTotalPerPerson(restaurantBill)))
print("Tip per person: "+ str(calculateTipPerPerson(restaurantBill)))
print("Total per person: "+ str(calculateTotalBill(restaurantBill)))
print("Total bill including tax and tip: " + str(calculateTotalBill(restaurantBill)*numberofPeople))