import random
done = False

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Starting at 0 miles, you must travel 200 miles to escape the desert")
print("Choose the best option to survive your desert trek and outrun the natives.")

milesTraveled = 0
milesTraveled = int(milesTraveled)
thirst = 0
thirst = int(thirst)
tiredness = 0
tiredness = int(tiredness)
drinks = 4
drinks = int(drinks)
nativeDistance = 20
nativeDistance = int(nativeDistance)


          
while True:
    print("A. Drink water from your canteen")
    print("B. Advance at moderate speed")
    print("C. Advance at full speed")
    print("D. Stop and rest")
    print("E. Status check")
    print("Q. Quit")
    
    answer1 = input("Your choice: ")
    
    if answer1.upper() == "Q" or answer1 == "q":
        print("Thank you for playing!")
        break

    elif answer1.upper() == "A" or answer1 == "a":
        drinks = drinks-1
        print("You now have", drinks, "drinks left")
        
    elif answer1 == "B" or answer1 == "b":#moderate speed
        print("The Natives are", random.randint(5,13), "miles behind you.")
        milesTraveled = milesTraveled+random.randint(10,21)
        print("You have traveled", milesTraveled, "miles") 
        thirst = thirst+1
        print("Your thirst value is now at", thirst)
        tiredness = tiredness+1
        print("Your camel tiredness is", tiredness)
        
    elif answer1 == "C" or answer1 == "c":#full speed
        print("The Natives are", random.randint(30,61), "miles behind you.")
        milesTraveled = milesTraveled+random.randint(10,16)
        print("You have traveled", milesTraveled, "miles")
        thirst = thirst+1
        print("Your thirst value is now at", thirst)
        tiredness = tiredness+random.randint(1,4)
        print("Your camel tiredness is", tiredness)
        
    elif answer1 == "E" or answer1 == "e":
        milesTraveled = milesTraveled
        print("You have traveled", milesTraveled, "miles")
        print("Drinks in canteen : 4")
        print("The Natives are", nativeDistance, "miles behind you.")
        
    elif answer1 == "D" or answer1 == "d":
        tiredness = 0
        print("Your camel is well rested. Camel Tiredness is, ", tiredness)
        print("The Natives are", random.randint(7,15), "miles behind you.")




    if milesTraveled == 200:
        print("Congrats! You've successfully outran the Natives!")

    elif thirst >= 8:
        print("You died of thirst!")
        break

    elif tiredness >= 10:
        print("Your camel died from exhaustion!")
        break

    elif drinks == 0:
        print("You don't have any more water in your canteen!")
        break

 

   
