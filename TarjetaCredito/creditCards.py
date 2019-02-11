#Alejandra Tubilla Castellanos
#A01022960
import random
from statistics import mean, mode, variance, median, stdev
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def creditCards(iterations):
    credit2 = []
    commision = 0
    callsNotAnswered = 0
    count0 = 0 
    count200 = 0
    count400 = 0
    count600 = 0
    count800 = 0
    employees = []
    #Eaxch employee makes 50000 calls 
    for k in range(0,20):
        for  j in range (0,iterations):
            calls = (random.randint(1,100))
            if calls in range(1,30): #call answered
                gender = (random.randint(1,100))
                if gender in range (1,80):#woman
                    sales = (random.randint(1,100))
                    if sales in range(1,15): #made a sale
                        credit = (random.randint(1,100))
                        if credit in range(1,60): #$50,000
                            commision = 200
                            count200 += 1
                        if credit in range(61,90): #$100,000
                            commision = 400
                            count400 += 1
                        if credit in range(91,100): #$150,000
                            commision = 600
                            count600 += 1
                    if sales in range(16,100): #didn't make a sale 
                        count0 += 1
                if gender in range (81,100): #man
                    sales = (random.randint(1,100))
                    if sales in range(1,25):
                        credit = (random.randint(1,100))
                        if credit in range(1,10): #$50,000
                            commision = 200
                            count200 += 1
                        if credit in range(11,50): #$100,000
                            commision = 400
                            count400 += 1
                        if credit in range(51,80): #$150,000
                            commision = 600
                            count600 += 1
                        if credit in range(81,100): #$200,000
                            commision = 800
                            count800 += 1
                    if sales in range(26,100):
                        count0 += 1
                #Call not answered
            else:
                callsNotAnswered += 1
            credit2.append(commision)
        #List of all employees commisions
        emp = sum(credit2)
        employees.append(emp)
    print("Highest employee commision: $",max(employees))
    media = mean(credit2)
    moda = mode(credit2)
    suma = sum(credit2)/20
    var = variance(credit2)
    med = median(credit2)
    svar = stdev(credit2)
    print("Total of commisions earned: $", suma)
    print("Most common commision earned (mode): $", moda)
    print("Average commision earned (mean): $", media)
    print("The variance: ", var)
    print("The median: ", med)
    print("Standard variation: ",svar)

    #Graph the commisions of the 20 employees from lowest to highest commision
    bars = ('20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1') 
    y_pos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    plt.bar(y_pos, employees)
    plt.xticks(y_pos, bars)
    plt.show()

def main ():
  creditCards(50000)
if __name__ == "__main__":
	main()
