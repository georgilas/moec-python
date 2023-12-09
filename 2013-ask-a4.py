plithos = 0
synoliki_timi = 0

timi = float(input("Δώσε τιμή προϊόντος: "))

while timi > 0:
    fpa = timi * 0.18
    synoliki_timi += timi + fpa
    plithos += 1
    timi = float(input("Δώσε τιμή προϊόντος: "))

if synoliki_timi > 100:
    ekptosi = synoliki_timi * 0.10
else:
    ekptosi = synoliki_timi * 0.05

teliki_timi = synoliki_timi - ekptosi

print(f"\nΑριθμός προϊόντων: {plithos}")
print(f"Συνολική τελική τιμή: {teliki_timi:6.2f}")
