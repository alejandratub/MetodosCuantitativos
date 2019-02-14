#Alejandra Tubilla Castellanos
#A01022960
import random
import numpy as np

def arrivalT():
    arrival = 0
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
    
    return arrival
    
def team3():
    #Gets service time for a team of 3
    service = 0
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
    
    return service

def team4():
    #Gets service time for a team of 4
    service = 0
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
    
    return service

def team5():
    #Gets service time for a team of 5
    service = 0
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
    
    return service

def team6():
    #Gets service time for a team of 6
    service = 0
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
    
    return service

iterations = 50000
workingHours = 1440
serviceHours = 1470
salary = 25.00
extraSalary = 37.50
lunch = False

salaries = np.zeros(7)
waiting = np.zeros(7)


def simulation(teamMembers):
	clock = 0
	arrivalTime = 0
	truckTime = 0
	serviceTime = 0
	waitingCost = 0
	workingCost = 0
	freeTime = 0
	lunch = False
	numberTrucks = 0
	

	prob = round(random.uniform(0.01, 1.0), 2)
	if(prob >= 0.01 and prob <= 0.50):
		numberTrucks = 0

		arrivalTime = arrivalT()
		clock += arrivalTime
		numberTrucks += 1
	
	elif(prob >= 0.51 and prob <= 0.75):
		numberTrucks = 1;

		serviceTime = time_service(teamMembers);
		arrivalTime = arrivalT();

		if(arrivalTime > serviceTime):
			freeTime += (arrivalTime - serviceTime)
			clock += serviceTime + freeTime
		else:
			truckTime += (serviceTime - arrivalTime)
			clock += serviceTime + truckTime
	
	elif(prob >= 0.76 and prob <= 0.90):
		numberTrucks = 2;

		serviceTime = time_service(teamMembers);
		truckTime += serviceTime;
		clock += serviceTime;

		serviceTime = time_service(teamMembers);
		arrivalTime = arrivalT();

		if(arrivalTime > serviceTime):
			freeTime += (arrivalTime - serviceTime)
			clock += serviceTime + freeTime
		else:
			truckTime += (serviceTime - arrivalTime)
			clock += serviceTime + truckTime

	elif(prob >= 0.91 and prob <= 1.0):
		numberTrucks = 3

		serviceTime = time_service(teamMembers)
		truckTime += serviceTime
		clock += serviceTime

		serviceTime = time_service(teamMembers)
		truckTime += serviceTime
		clock += serviceTime
		
		serviceTime = time_service(teamMembers)
		arrivalTime = arrivalT()

		if(arrivalTime > serviceTime):
			freeTime += (arrivalTime - serviceTime)
			clock += serviceTime + freeTime
		else:
			truckTime += (serviceTime - arrivalTime)
			clock += serviceTime + truckTime
		
		if(clock > serviceHours):
			serviceTime = time_service(teamMembers)
			clock += serviceTime

	while(clock <= serviceHours):
		
		if(clock >= 240 and lunch == False):
			clock += 30
			lunch = True    
		arrivalTime = arrivalT()
		serviceTime = time_service(teamMembers)
		
		if(arrivalTime > serviceTime):
			freeTime += (arrivalTime - serviceTime)
			clock += serviceTime + freeTime
			numberTrucks += 1
		else:
			truckTime += (serviceTime - arrivalTime)
			clock += serviceTime + truckTime
			numberTrucks -= 1
	
	pay = (teamMembers * 8 * salary) + (extraSalary * teamMembers *((clock-serviceHours) / 60))
	wait = (500 * (clock / 60)) + (100 * (truckTime / 60))
	salaries[teamMembers] += pay
	waiting[teamMembers] += wait
	totalCost = pay + wait

	return totalCost

def time_service(grupo):
	tiempo = 0
	if(grupo == 3): tiempo = team3()
	if(grupo == 4): tiempo = team4()
	if(grupo == 5): tiempo = team5()
	if(grupo == 6): tiempo = team6()
	
	return tiempo
def queue():	
	cost3 = 0
	cost4 = 0
	cost5 = 0
	cost6 = 0

	for i in range(iterations):
		cost3 += simulation(3)
		cost4 += simulation(4)
		cost5 += simulation(5)
		cost6 += simulation(6)
	
	total3 = cost3/iterations
	total4 = cost4/iterations
	total5 = cost5/iterations
	total6 = cost6/iterations 
	print("TEAM OF 3 MEMBERS\n","Total Cost: ", total3, "\n Salaries:", salaries[3]/iterations, "\n Waiting Cost:", waiting[3]/iterations)
	print("\nTEAM OF 4 MEMBERS\n","Total Cost: ", total4, "\n Salaries:", salaries[4]/iterations, "\n Waiting Cost:", waiting[4]/iterations)
	print("\nTEAM OF 5 MEMBERS\n","Total Cost: ", total5, "\n Salaries:", salaries[5]/iterations, "\n Waiting Cost:", waiting[5]/iterations)
	print("\nTEAM OF 6 MEMBERS\n","Total Cost: ", total6, "\n Salaries:", salaries[6]/iterations, "\n Waiting Cost:", waiting[6]/iterations)

	totals = np.zeros(7)
	totals[3] = total3 / 3
	totals[4] = total4 / 4
	totals[5] = total5 / 5
	totals[6] = total6 / 6
	
	tmp1 = 0
	tmp2 = 0
	for i in range(len(totals)):
		if tmp1 < totals[i]:
			tmp1 = totals[i]
			tmp2 = i
	print("\nOptimal team size: ", i)

def main():
	queue()

if __name__ == "__main__":
	main()

