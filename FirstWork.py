bill = input(" Ingrese el costo: ")
cost = float(bill[1:])
print(f" Bill: {bill}")

print("\n List of recommended tips ammount:")
print(f" 15% = {cost * .15}\n 18% = {cost * .18}\n 20% = {cost * .20} ")

# Example imput: $500
# Return:
# List of recommended tips ammount:
# 15% = 75.0
# 18% = 90.0
# 20% = 100.0 