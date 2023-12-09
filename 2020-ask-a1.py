n = int(input("Αριθμός ξώβεργων; "))

prostimo = 200 if n <= 72 else 200 + (n - 72) * 10

print(f"Το πρόστιμο για {n:2d} ξώβεργες είναι {prostimo:.2f} ευρώ.")
