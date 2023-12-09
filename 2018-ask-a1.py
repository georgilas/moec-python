leof = int(input("Πόσα λεωφορεία θα χρειασστούν; "))

timi_ana_leof = 50

pososto_ekp = 0.2 if leof > 15 else 0.1

teliki_timi_pro_ekp = leof * timi_ana_leof

ekptosi = teliki_timi_pro_ekp * pososto_ekp

teliki_timi = teliki_timi_pro_ekp - ekptosi

print(f"\nΈκπτωση: {ekptosi:.2f} ευρώ.\nΤελικό ποσό: {teliki_timi:.2f} ευρώ.")
