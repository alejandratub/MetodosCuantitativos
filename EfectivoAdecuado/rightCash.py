#Alejandra Tubilla Castellanos
#A01022960
import random
import numpy as np
import math
from scipy import stats
from statistics import mean, stdev

def cash(iterations):
    cost = 0
    total_cost = []
    totalCost = 0
    dev_std = 0
    for  j in range (0,iterations):
        cars = 0 
        #Gets random number of dozens
        numberCars = random.randint(1,100)
        if (numberCars >= 1) and (numberCars <= 5): #3 cars
            cars = 3
        if (numberCars >= 6) and (numberCars <= 20): #4 cars
            cars = 4
        if (numberCars >= 21) and (numberCars <= 50): #5 cars
            cars = 5
        if (numberCars >= 51) and (numberCars <= 75): #6 cars
            cars = 6
        if (numberCars >= 76) and (numberCars <= 90): #7 cars
            cars = 7
        if (numberCars >= 91) and (numberCars <= 100):#8 cars
            cars = 8
        
        for i  in range(cars):
            typeCar = random.randint(1,100)
            if (typeCar >= 1) and (typeCar <= 45): #small
                num = random.randint(1,100)
                if (num >= 1) and (num <= 45):
                    cost += 350
                if (num >= 46) and (num <= 60):
                    cost += 1575
                if (num >= 61) and (num <= 80):
                    cost += 1925
                if (num >= 81) and (num <= 90):
                    cost += 2540
                if (num >= 91) and (num <= 100):
                    cost += 700
            if (typeCar >= 46) and (typeCar <= 80): #medium
                num = random.randint(1,100)
                if (num >= 1) and (num <= 25):
                    cost += 550
                if (num >= 26) and (num <= 50):
                    cost += 1975
                if (num >= 51) and (num <= 65):
                    cost += 2545
                if (num >= 66) and (num <= 85):
                    cost += 2925
                if (num >= 86) and (num <= 100):
                    cost += 700
            if (typeCar >= 81) and (typeCar <= 100): #large
                num = random.randint(1,100)
                if (num >= 1) and (num <= 10):
                    cost += 750
                if (num >= 11) and (num <= 25):
                    cost += 2275
                if (num >= 26) and (num <= 55):
                    cost += 2845
                if (num >= 56) and (num <= 95):
                    cost += 3415
                if (num >= 96) and (num <= 100):
                    cost += 700
        total_cost.append(cost)
    
    totalCost = cost/iterations
    std = stdev(total_cost)/iterations

    seventy = stats.norm.interval(0.70, loc = totalCost, scale = std / np.sqrt(len(total_cost)))
    eighty = stats.norm.interval(0.80, loc = totalCost, scale = std / np.sqrt(len(total_cost)))
    ninety = stats.norm.interval(0.90, loc = totalCost, scale = std / np.sqrt(len(total_cost)))
    ninetyFive = stats.norm.interval(0.95, loc = totalCost, scale = std / np.sqrt(len(total_cost)))
    ninetyNine = stats.norm.interval(0.99, loc = totalCost, scale = std / np.sqrt(len(total_cost))) 
   

    print("Total Cost: ", totalCost)
    print("Desviación: ", std)
    print("Cost at 70%:", seventy)
    print("Cost at 80%:", eighty)
    print("Cost at 90%:", ninety)
    print("Cost at 95%:", ninetyFive)
    print("Cost at 99%:", ninetyNine)
    
    
def main ():
  cash(50000)
if __name__ == "__main__":
	main()

