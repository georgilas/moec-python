cost_per_gram = 0.017

weight_in_grams = int(input("Weight in grams? "))

if 20 <= weight_in_grams <= 500:
	amount_payable = weight_in_grams * cost_per_gram
	print(f"\nAmount payable: {amount_payable:.2f}")
else:
	print("\nWEIGHT OUT OF LIMITS")
