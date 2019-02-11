#Alejandra Tubilla Castellanos
#A01022960
import random

def queue(iterations,teamSize):
    for  j in range (0,iterations):
        trucks = 0 
        arrival = 0
        service = 0

        #Gets random number of trucks waiting
        numberTrucks = random.randint(1,100)
        if (numberTrucks >= 1) and (numberTrucks <= 50): #0 trucks
            trucks  = 0
        if (numberTrucks >= 51) and (numberTrucks <= 75): #1 truck
            trucks = 1
        if (numberTrucks >= 76) and (numberTrucks <= 90): #2 trucks
            trucks = 2
        if (numberTrucks >= 91) and (numberTrucks <= 100): #3 trucks
            trucks = 3

        #Gets random time of arrival
        arrivalTime = random.randint(1,100)
        if (arrivalTime >= 1) and (arrivalTime <= 2): #20 minutes
            arrival = 20
        if (arrivalTime >= 3) and (arrivalTime <= 10): #25 minutes
            arrival = 25
        if (arrivalTime >= 11) and (arrivalTime <= 22): #30 minutes
            arrival = 30
        if (arrivalTime >= 23) and (arrivalTime <= 47): #35 minutes
            arrival = 35
        if(arrivalTime >= 48) and (arrivalTime <= 67): #40 minutes
            arrival = 40
        if(arrivalTime >= 68) and (arrivalTime <= 82): #45 minutes
            arrival = 45
        if (arrivalTime >= 83) and (arrivalTime <= 92): #50 minutes
            arrival  = 50 
        if(arrivalTime >= 93) and (arrivalTime <= 97): #55 minutes
            arrival = 55
        if(arrivalTime >= 98) and (arrivalTime <= 100): #60 minutes
            arrival = 60

        #Gets service time deppending on the team size
        if teamSize == 3: #team of 3
            serviceTime = random.randint(1,100)
            if (serviceTime >= 1) and (serviceTime <= 5): #20 minutes+
                service = 20
            if (serviceTime >= 6) and (serviceTime <= 15): #25 minutes
                service = 25
            if (serviceTime >= 16) and (serviceTime <= 35): #30 minutes
                service = 30
            if (serviceTime >= 36) and (serviceTime <= 60): #35 minutes
                service = 35
            if (serviceTime >= 61) and (serviceTime <= 72): #40 minutes
                service = 40
            if (serviceTime >= 73) and (serviceTime <= 82): #45 minutes
                service = 45
            if (serviceTime >= 83) and (serviceTime <= 90): #50 minutes
                service = 50
            if (serviceTime >= 91) and (serviceTime <= 96): #55 minutes
                service = 55
            if (serviceTime >= 97) and (serviceTime <= 100): #60 minutes
                service = 60
        
        if teamSize == 4: #team of 4
            serviceTime = random.randint(1,100)
            if (serviceTime >= 1) and (serviceTime <= 5): #15 minutes
                service = 15
            if (serviceTime >= 6) and (serviceTime <= 20): #20 minutes
                service = 20
            if (serviceTime >= 21) and (serviceTime <= 40): #25 minutes
                service = 25
            if (serviceTime >= 41) and (serviceTime <= 60): #30 minutes
                service = 30
            if (serviceTime >= 61) and (serviceTime <= 75): #35 minutes
                service = 35
            if (serviceTime >= 76) and (serviceTime <= 87): #40 minutes
                service = 40
            if (serviceTime >= 88) and (serviceTime <= 95): #45 minutes
                service = 45
            if (serviceTime >= 96) and (serviceTime <= 99): #50 minutes
                service = 50
            if (serviceTime == 100): #55 minutes
                service = 55
        
        if teamSize == 5: #team of 5
            serviceTime = random.randint(1,100)
            if (serviceTime >= 1) and (serviceTime <= 10): #10 minutes
                service = 10
            if (serviceTime >= 11) and (serviceTime <= 28): #15 minutes
                service = 15
            if (serviceTime >= 29) and (serviceTime <= 50): #20 minutes
                service = 20
            if (serviceTime >= 51) and (serviceTime <= 68): #25 minutes
                service = 25
            if (serviceTime >= 69) and (serviceTime <= 78): #30 minutes
                service = 30 
            if (serviceTime >= 79) and (serviceTime <= 86): #35 minutes
                service = 35
            if (serviceTime >= 87) and (serviceTime <= 92): #40 minutes
                service = 40
            if (serviceTime >= 93) and (serviceTime <= 97): #45 minutes
                service = 45
            if (serviceTime >= 98) and (serviceTime <= 100): #50 minutes
                service = 50      

        if teamSize == 6: #team of 6
            serviceTime = random.randint(1,100)
            if (serviceTime >= 1) and (serviceTime <= 12): #5 minutes
                service = 5
            if (serviceTime >= 13) and (serviceTime <= 27): #10 minutes
                service = 10
            if (serviceTime >= 28) and (serviceTime <= 53): #15 minutes
                service = 15
            if (serviceTime >= 54) and (serviceTime <= 68): #20 minutes
                service = 20
            if (serviceTime >= 69) and (serviceTime <= 80): #25 minutes
                service = 25
            if (serviceTime >= 81) and (serviceTime <= 88): #30 minutes
                service = 30
            if (serviceTime >= 89) and (serviceTime <= 94): #35 minutes
                service = 35 
            if (serviceTime >= 95) and (serviceTime <= 98): #40 minutes
                service = 40
            if (serviceTime >= 99) and (serviceTime <= 100): #45 minutes
                service = 45
    
def main ():
  queue(50000,3)
if __name__ == "__main__":
	main()

