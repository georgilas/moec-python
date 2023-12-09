kat = float(input("Κατανάλωση; "))

poso = kat * 0.7 if kat <= 80 else kat * 0.95 + 10

print(f"Ποσό πληρωμής για κατανάλωση {kat} κ.μ. είναι {poso:.2f} ευρώ.")
