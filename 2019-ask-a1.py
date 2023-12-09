epitr_orio_tax = int(input("Επιτρεπόμενο όριο ταχύτητας; "))
tax_odigou = int(input("Ταχύτητα οδηγού;"))

if tax_odigou > epitr_orio_tax:
	ypervasi = tax_odigou - epitr_orio_tax
	prostimo = ypervasi * 5
	print(f"Το πρόστιμο για υπέρβαση τού επιτρεπόμενου ορίου ταχύτητας κατά {ypervasi:2d} χλμ ανά ώρα είναι {prostimo:.2f} ευρώ.")
else:
	print("Δεν υπάρχει πρόστιμο.")
