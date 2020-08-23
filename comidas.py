import random
comidasC = ["Fideos con salsa","Pescado frito","Papas duquesas con carne","Churrasco"]
comidasV = ["Fideos al pesto","Ensalada de papas","Lasaña de berenjena","Arroz con papas fritas"]

print("Are you vegetarian? (Y/N)")

choice = input()


if(choice == 'y' or choice == 'Y'):
    print(f"Que tal si comes {random.choice(comidasV)}")
else:
    print(f"Que tal si comes {random.choice(comidasC)}")