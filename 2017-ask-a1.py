timi_isitiriou = float(input("Τιμή εισιτηρίου; "))
ilikia_pelati = int(input("Ηλικία πελάτη; "))

if 18 < ilikia_pelati <=65:
	print(f"\nΚΑΜΜΙΑ ΕΚΠΤΩΣΗ\nΤιμή εισιτηρίου: {timi_isitiriou:.2f} ευρώ.")
else:
	print(f"\nΤιμή εισιτηρίου: {timi_isitiriou * 0.6:.2f} ευρώ.")
