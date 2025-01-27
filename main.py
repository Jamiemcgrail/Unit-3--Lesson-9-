

# Run command
# python main.py

taxRate = 0.0875

print("Welcome to the tax calculator program!")
print()

costUSD = float(input("Enter cost of item: $ "))
taxUSD = costUSD * taxRate
totalUSD = costUSD + taxUSD

print("Cost: $ ", end='')
print('{:.2f}'.format(costUSD))

print("Tax: $ ", end='')
print('{:.2f}'.format(taxUSD))

print("Total: $ ", end='')
print('{:.2f}'.format(totalUSD))

print()
print("Goodbye!")