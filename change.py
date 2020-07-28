change = 0

def costOfGood():
    global cost
    try:
        cost = float(input("Cost of good: "))
    except ValueError:
        print("Please enter a valid cost.")
        costOfGood() 
    if len(str(cost).rsplit('.')[-1]) <= 2:
        return cost
    else:
        print("Please enter a cash value to the nearest cent.")
        costOfGood()

def cashGiven():
    global given
    try:
        given = float(input("Amount of cash given: "))
    except ValueError:
        print("Please enter a valid cash amount.")
        cashGiven()
    if len(str(given).rsplit('.')[-1]) <= 2:
        if given > cost:
            return given
        else:
            print("Customer has not paid enough money.")
            cashGiven()
    else:
        print("Please enter a cash value to the nearest cent.")
        cashGiven()

def hundreds():
    global change
    global given
    hundred = 0
    if (given - cost) >= 100:
        while (given - 100) >= cost:
            hundred += 1
            given -= 100
            change += 100
        print(f"{hundred} hundred dollar bills.")
        return hundred
    else:
        return True

def fifties():
    global given
    global change
    fifty = 0
    if (given - cost >= 50):
        while (given - 50) >= cost:
            fifty += 1
            given -= 50
            change += 50
        print(f"{fifty} fifty dollar bill.")
        return fifty
    else:
        return True

def twenties():
    global given
    global change
    twenty = 0
    if (given - cost >= 20):
        while (given - 20) >= cost:
            twenty += 1
            given -= 20
            change += 20
        print(f"{twenty} twenty dollar bills.")
        return twenty
    else:
        return True

def tens():
    global given
    global change
    ten = 0
    if (given - cost >= 10):
        while (given - 10) >= cost:
            ten += 1
            given -= 10
            change += 10
        print(f"{ten} ten dollar bill.")
        return ten
    else:
        return True

def fives():
    global given
    global change
    five = 0
    if (given - cost >= 5):
        while (given - 5) >= cost:
            five += 1
            given -= 5
            change += 5
        print(f"{five} five dollar bill.")
        return five
    else:
        return True

def toonies():
    global given
    global change
    two = 0
    if (given - cost >= 2):
        while (given - 2) >= cost:
            two += 1
            given -= 2
            change += 2
        print(f"{two} toonies.")
        return two
    else:
        return True

def loonies():
    global given
    global change
    one = 0
    if (given - cost >= 1):
        while (given - 1) >= cost:
            one += 1
            given -= 1
            change += 1
        print(f"{one} loonie.")
        return one
    else:
        return True

def quarters():
    global given
    global change
    twentyfiveCents = 0
    if (given - cost >= 0.25):
        while round(given - 0.25, 2) >= cost:
            twentyfiveCents += 1
            given -= 0.25
            change += 0.25
        print(f"{twentyfiveCents} quarters.")
        return twentyfiveCents
    else:
        return True

def dimes():
    global given
    global change
    tenCents = 0
    if (given - cost >= 0.10):
        while round(given - 0.10, 2) >= cost:
            tenCents += 1
            given -= 0.10
            change += 0.10
        print(f"{tenCents} dimes.")
        return tenCents
    else:
        return True

def nickels():
    global given
    global change
    fiveCents = 0
    if (given - cost >= 0.05):
        while round(given - 0.05, 2) >= cost:
            fiveCents += 1
            given -= 0.05
            change += 0.05
        print(f"{fiveCents} nickel.")
        return fiveCents
    else:
        return True

costOfGood()
cashGiven()
print("\nChange owed:")
hundreds()
fifties()
twenties()
tens()
fives()
toonies()
loonies()
quarters()
dimes()
nickels()
print(f"\nTotal change: ${change:.2f}\n")