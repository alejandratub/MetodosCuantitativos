#Alejandra Tubilla Castellanos
#A01022960
import random
import numpy as np

def meet(iterations):
    time = np.zeros(61) #array that will save the meeting times
    no = 0

    for i in range (0,iterations):

        arrivalR  = random.randint(0,59) #random arrival time for Rosy
        arrivalA = random.randint(0,59) #random arrival time for Afrodicio

        if (arrivalR == arrivalA): #If their arrival times are the same
            time[arrivalA] += 1
        
        if (arrivalR < arrivalA) and (arrivalR + 15 > arrivalA): #if Rosy's arrival time is before Afrodicio's, 
                                                                #and if Afrodicio's time is before Rosy leaves 
            time[arrivalA] += 1
        
        if (arrivalA < arrivalR) and (arrivalA + 20 > arrivalR): #if Afrodicio's time is before Rosy's
                                                                #and if Rosy's time is before Afrodicio leaves
            time[arrivalR] += 1
        
        else: #if they don't meet
            no += 1
    
    times = time.argsort()[-1:][::-1]
    print("Highest probability of meeting is at minute:", times)

def main ():
  meet(50000)
if __name__ == "__main__":
	main()
