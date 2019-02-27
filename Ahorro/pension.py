#Alejandra Tubilla Castellanos 
#A01022960
import sys
import random

def pension(iterations):

    monthlyPay = 30000
    transportOptions = [1300,1800,2300,2800,3300,3800]
    itemBalance=0
    optionProbability=1/6
    funBalance=0
    investmentBalance=0
    foodBalance=0
    pensionBalance=0
    unforseenBalance=0
    transportTotal=0
    funTotal=0
    investmentTotal=0
    unforseenTotal=0
    pensionTotal=0
    foodTotal=0
   
    for i in range(0,iterations):
        #The Monthly pay is $30000
        funBalance=0
        investmentBalance=0
        foodBalance=0
        pensionBalance=0
        unforseenBalance=0
        itemBalance=0
        Transport = random.random()

        if(Transport<optionProbability):
            #1300
            itemBalance = monthlyPay - transportOptions[0]
        elif(Transport>=optionProbability and Transport < (2*optionProbability)):
            #1800
            itemBalance = monthlyPay - transportOptions[1]

        elif(Transport>=(2*optionProbability) and Transport < (3*optionProbability)):
            #2300
            itemBalance = monthlyPay - transportOptions[2]

        elif(Transport>=(3*optionProbability) and Transport < (4*optionProbability)):
            #2800
            itemBalance = monthlyPay - transportOptions[3]

        elif(Transport>=(4*optionProbability) and Transport< (5*optionProbability)):
            #3300
            itemBalance = monthlyPay - transportOptions[4]

        else:
            #3800
            itemBalance = monthlyPay - transportOptions[5]

        #after the transport expenses, the balance is divided by the other different ones:
        foodBalance = itemBalance*.20
        investmentBalance=itemBalance*0.4
        funBalance = itemBalance*0.3

        unforseen = random.random()
        if(unforseen<0.35): #35% for an unforseen event 
            unforseenBalance = itemBalance * 0.1
        else:
            pensionBalance = itemBalance * 0.1

        
        transportTotal+=monthlyPay - itemBalance
        foodTotal+=foodBalance
        pensionTotal+=pensionBalance
        unforseenTotal+=unforseenBalance
        investmentTotal+=investmentBalance
        funTotal+=funBalance

    unforseenAverage = unforseenTotal/5000
    foodAverage = foodTotal/5000
    pensionAverage = pensionTotal/5000
    investmentAverage= investmentTotal/5000
    transportAverage = (transportTotal)/5000
    funAverage=funTotal/5000


    print("Monthly recommended distribution based on the Salary")
    print("Transport: ", transportAverage)
    print("Fun: ", funAverage)
    print("Investment: ", investmentAverage)
    print("Pension: ", pensionAverage)
    print("Food and Clothes: ", foodAverage)
    print("Unforseen: ", unforseenAverage)

    print(" ")
    print("Salary percentage:")
    print("Transport:", ((transportAverage / monthlyPay) * 100), "%")
    print("Fun:", ((funAverage / monthlyPay) * 100), "%")
    print("Investment:", ((investmentAverage/monthlyPay)*100), "%")
    print("Pension:", ((pensionAverage / monthlyPay) * 100), "%")
    print("Food and Clothes:",((foodAverage / monthlyPay) * 100), "%")
    print("Unforseen:", ((unforseenAverage / monthlyPay) * 100), "%" )

    print(" ")
    print("Total after 50000 months: ")
    print("Transport: ", transportTotal)
    print("Fun: ", funTotal)
    print("Investment: ", investmentTotal)
    print("Pension: ", pensionTotal)
    print("Food and Clothes: ", foodTotal)
    print("Unforseen: ", unforseenTotal)

def main ():
  pension(50000)
if __name__ == "__main__":
	main()