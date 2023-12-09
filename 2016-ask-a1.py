arith_dianykt = int(input("Αριθμός διανυκτερεύσεων: "))
timi_dianykt = float(input("Τιμή ανά διανυκτέρευση: "))

syn_timi = arith_dianykt * timi_dianykt

if arith_dianykt > 3 and timi_dianykt >= 100:
    pos_ekp = 0.3
else:
    pos_ekp = 0.1

ekptosi = syn_timi * pos_ekp

tel_timi = syn_timi - ekptosi

print(f"\nΤελική τιμή: {tel_timi:.2f} ευρώ.")
