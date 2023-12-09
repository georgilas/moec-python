workers = 5
threshold = 500

tot = 0

for i in range(workers):
    name = input("Όνομα εργάτη: ")
    cases = int(input("Αριθμός κιβωτίων: "))

    diff = cases - threshold

    tot += cases

    if diff < 0:
        print(f"Όνομα: {name} - Ρήτρα: {abs(diff):.2f} ευρώ.")
    elif diff == 0:
        print(f"Όνομα: {name} - Μηδενικό επίδομα.")
    elif 1 <= diff <= 15:
        print(f"Όνομα: {name} - Επίδομα: {diff * 1.0:.2f} ευρώ.")
    elif 16 <= diff <= 30:
        print(f"Όνομα: {name} - Επίδομα: {diff * 2.0:.2f} ευρώ.")
    else:
        print(f"Όνομα: {name} - Επίδομα: {diff * 3.0:.2f} ευρώ.")

print(f"\nΣυνολικός αριθμός κιβωτίων: {tot:1d}")
