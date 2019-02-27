#Alejandra Tubilla Castellanos 
#A01022960
import random

def art(iterations):
    sale = 500000
    saleDay1 = 0
    saleDay2 = 0
    saleDay3 = 0
    for i in range(0,iterations):
        probabilityDay1 = random.randint(1,100)
        if(probabilityDay1 >= 40): #if it is available the first day I can either buyit or wait
            saleDay1 += sale - 400000
            probabilityDay2 = random.randint(1,100)
            if(probabilityDay2 >= 40): #If I waited the second day and it is available I can either buy it or wait
                #plan2 compra y plan3 espera. 
                saleDay2 += sale - 300000
                probabilityDay3 = random.randint(1,100)
                if(probabilityDay3 >= 40): #If it is available the third day I buy it
                    saleDay3 += sale - 260000
                else:
                    saleDay3 += 0 #Not available the third day
            else: #Not available the second Day
                saleDay2 += 0
                saleDay3 += 0
        else: #Not available the third day
            saleDay1 += 0
            saleDay2 += 0
            saleDay3 += 0
    high = max([saleDay1, saleDay2,saleDay3])
    print("Total Profit of buying the first day is: ", saleDay1)
    print("Total Profit of buying the second day is: ", saleDay2)
    print("Total Profit of buying the third day is: ", saleDay3)
def main ():
  art(50000)
if __name__ == "__main__":
	main()