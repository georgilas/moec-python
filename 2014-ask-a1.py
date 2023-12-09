n = int(input("Αριθμός μαθητή: "))

match n:
    case n if n in range(1, 9):
        g = "ΑΜΜΟΧΩΣΤΟΣ"
    case n if n in range(9, 17):
        g = "ΚΕΡΥΝΕΙΑ"
    case n if n in range(17, 26):
        g = "ΜΟΡΦΟΥ"

print(f"Ομάδα: {g}")
