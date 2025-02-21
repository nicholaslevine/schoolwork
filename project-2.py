"""
Name : Nicholas Levine
Date : 2/21/25
Program: Ashcon County Cheese Purchase
"""
min = 0.25
max = 100
price = 7.99
def buy(pounds : float):
    if pounds < min:
        return f"{str(pounds)} lbs is below the minimum order amount"
    
    if pounds > max:
        return f"{str(pounds)} lbs is more than is currently in stock"
    return f"{pounds} lbs of cheese costs ${round((pounds * price), 2)}."
while True:
    print("Welcome to the Ashe County Cheese Company")
    print()
    print("Please place your cheese order below:")
    print()
    lbs = float(input("Enter cheese order weight (pounds): "))
    print(buy(lbs))




