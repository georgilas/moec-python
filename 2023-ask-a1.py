tariff = 6

days = int(input("Days? "))

if days > 7:
	discount = 0.2
else:
	discount = 0

amount = (days * tariff) * (1.0 - discount)

print(f"\nAmount payable for {days} days: {amount:4.2f} euro.")
