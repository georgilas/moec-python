wallet = 500.0

price = float(input("Τιμή υπολογιστή: "))

if price > wallet:
    print("\nΑΓΟΡΑ ΑΔΥΝΑΤΗ")
else:
    print(f"\nΑΓΟΡΑ ΔΥΝΑΤΗ - Υπόλοιπο: {(wallet - price):.2f} ευρώ.")
