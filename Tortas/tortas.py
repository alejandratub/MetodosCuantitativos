#Alejandra Tubilla Castellanos
#A01022960
import random
import numpy as np

def tortas(iterations):
    #Lists to save the info
    dozens = np.zeros(13)
    totals = np.zeros(13)

    for  j in range (0,iterations):
        dozen = 0 
        utilities = 0
        #Gets random number of dozens
        num = random.randint(1,100)
        if (num >= 1) and (num <= 5):
            dozen = 2
        if (num >= 6) and (num <= 15):
            dozen = 4
        if (num >= 16) and (num <= 35):
            dozen = 6
        if (num >= 36) and (num <= 75):
            dozen = 8
        if (num >= 76) and (num <= 95):
            dozen = 10
        if (num >= 96) and (num <= 100):
            dozen = 12
        #Gets the actual number of clients and breads
        bread = dozen * 12
        bought = random.randint(0,12)
        clients = bought * 12

        #Condition to get the utilities if the number of clients is less or the same as the number of breads
        if clients <= bread:
            saleUtilities = (bread * 18) + (clients * 2)
            waste = ((bread - clients)/2) * 1.5
            utilities += saleUtilities + waste
        #Condition to get the utilities if the number of clients is bigger than the number of breads
        if clients > bread:
            saleUtilities = bread * 25
            loss = (clients - bread) * 10
            utilities += saleUtilities - loss
        totals[bought] += utilities
        dozens[bought] += 1

    biggestProfit = 0
    dozenT = 0
    profit = 0

    #Loop to print the utilities based on each range of dozens of breads
    for i in range(0,13,2):
        profit = totals[i] / dozens[i]
        print("For ", i, "dozens, you will make a profit of $", profit)
    #Loop to get the dozen that has the highest utilities
    for i in range(0,13,2):
        profit = totals[i] / dozens[i]
        if(profit > biggestProfit):
            biggestProfit = profit
            dozenT = i
    print("You should buy: ", dozenT, " dozens, to make the biggest profit")

def main ():
  tortas(50000)
if __name__ == "__main__":
	main()
