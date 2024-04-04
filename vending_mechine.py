def vending_machine(drinks, drink, cash):
    notes = [100, 50, 20, 10, 5, 1]
    drink = drink.title()
    note_return = {}
    balance = cash - drinks[drink]
    for x in notes:
    	divisible = balance - balance % x
    	balance = balance % x
    	note_return["RM"+str(x)] = int(divisible / x) 
    	    
    return (note_return)

drinks = {
    "Coke": 1,
    "Pepsi": 2,
    "Wonda": 5,
    "Evian": 9,
}
cash = int(input("I have RM"))
drink = input("I wish to buy <Coke(RM1)/Pepsi(RM2)/Wonda(RM5)/Evian(RM9)>:")
print("Returned least number of notes is: "+str((vending_machine(drinks, drink, cash)))) 

