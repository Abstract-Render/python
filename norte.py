# from math import e
# from math import log10
from math import ceil

carloan = float(input("Enter loan amount: "))
interestRate = float(input("Enter interest rate decimals: "))
loanInterest = float(input("Enter your loan's interest"))
# time = int(input("Enter number years to pay back: "))
# timeMonths = time / 12
# total = carloan * e ** (time*interestRate)
# montlyTotal = total / timeMonths
montlyTotal = loanInterest / (interestRate*carloan)
print("You will pay off your car in "+ str(ceil(montlyTotal*12))+ " Months")