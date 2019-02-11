#Alejandra Tubilla Castellanos
#A01022960
import random
from statistics import mode
import numpy as np

def lottery(iterations):
    #random.seed(1)
    timesRepeated = np.zeros(71)
    extraRepeated = np.zeros(26)
    for  j in range (0,iterations):
        numbers = set()
        count = 0
        #Gets the 5 random numbers
        while count < (5):
            num = (random.randint(1,70))
            if num not in numbers:
                numbers.add(num) #if the random number is not repeated, it saves it
                timesRepeated[num] += 1
                count += 1
        extra = (random.randint(1,25))
        extraRepeated[extra] += 1 #saves the extra number
    #Gets the 5 numbers that repeat the most
    top5Numbers = timesRepeated.argsort()[-5:][::-1]
    print("The 5 numbers that repeat the most are: ", top5Numbers)
    #Gets the extra number that repeats the most
    extra = extraRepeated.argsort()[-1:][::-1]
    print("The extra number that repeats the most is: ", extra)

    countNew = 0
    while 1:
        countNew += 1
        newnumbers = set()
        count2 = 0
        #Gets the 5 random numbers
        while count2 < (5):
            num = (random.randint(1,70))
            if num not in numbers:
                newnumbers.add(num)
                count2 += 1
        extra2 = (random.randint(1,25))
        #Gets the difference between the two sets of numbers
        difference = newnumbers.symmetric_difference(top5Numbers)
        #Gets the lenght of the new set (if the lenght is = 0, the sets have the same numbers)
        total= len(difference)
        #Compares if the numbers are the same
        if((total == 0)and(extra2 == extra)):
            print("Number of tickets needed: ", countNew)
            break
def main ():
  lottery(50000)
if __name__ == "__main__":
	main()
