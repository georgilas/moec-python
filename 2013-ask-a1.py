grapta = int(input("Γραπτά: "))
proforika = int(input("Προφορικά: "))

athrisma = grapta + proforika

if grapta >= 10 and proforika >= 10 and athrisma > 22:
    print(f"Συνολική βαθμολογία: {athrisma:1d}.")
else:
    print("ΕΠΑΝΕΞΕΤΑΣΗ.")
