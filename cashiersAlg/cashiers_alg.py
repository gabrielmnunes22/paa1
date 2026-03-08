# MENU IMPLEMENTATION

def cashiersAlg(amount):
    cash = [100, 25, 10, 5, 1]
    bestTry = 0

    while amount > 0:
        for change in cash:
            if amount >= change:
                amount -= change
                bestTry += 1
                break
    
    print(f"Optimal Solution: {bestTry}")



def giveChange(amount):
    print("a)1¢   b) 5¢   c)10¢   d)25¢   e)$1")
    
    while True:
        changeOption = input("change: ")

        match changeOption:
            case 'a':
                change = 1
            case 'b':
                change = 5
            case 'c':
                change = 10
            case 'd':
                change = 25
            case 'e':
                change = 100
            case _:
                print("Incorrect Input")
        
        if change <= amount:
            return change
        

def main(amount):
    originalAmount = amount 
    tries = 0

    while True:
        print(f"\nAMOUNT = {amount / 100}")
        choice = int(input("\n1-give change\n2-clear tray\n3-exit\n"))
    
        match choice:
            case 1:
                change = giveChange(amount)
                amount -= change
                tries += 1

                if amount == 0:
                    print("\nChange given!")
                    print(f"solution: {tries} steps")
                    break

            case 2:
                amount = originalAmount
            case 3:
                break
            case _:
                print("unknown option")


if __name__== "__main__":
    amount = int(float(input("amount: ")) * 100)

    main(amount)            # your try
    cashiersAlg(amount)     # best solution