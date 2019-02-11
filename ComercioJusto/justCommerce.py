#Alejandra Tubilla Castellanos
#A01022960
import random
from statistics import mode

def justCommerce(iterations):
    down = 0 # pay down
    up = 0 # pay up
    price = 0 #price to pay
    for  j in range (iterations):
        num = (random.randint(0,99))
        if (num >= 20) and (num <= 99): #pay down ($99)
            up += 99
        else: #pay up ($100)
            down += 100

    #Calculates de most common price to pay
    price = ((up + down) / iterations)
    print("Price: ", price)
def main ():
  justCommerce(50000)
if __name__ == "__main__":
	main()
