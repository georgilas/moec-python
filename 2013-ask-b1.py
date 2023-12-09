plithos = 0
plithos_mioseon = 0
syn_sim_misthon = 0
syn_mioseon = 0

name = input("Δώσε όνομα υπαλλήλου (ΤΕΛΟΣ για διακοπή): ")

while name != "ΤΕΛΟΣ":
    simerinos_misthos = float(input("Δώσε σημερινό μισθό υπαλλήλου: "))
    while simerinos_misthos <= 0:
        simerinos_misthos = float(input("ΛΑΘΟΣ ΜΙΣΘΟΣ - Δώσε σημερινό μισθό υπαλλήλου: "))

    plithos += 1
    syn_sim_misthon += simerinos_misthos

    if simerinos_misthos <= 1000:
        miosi = 0
    elif simerinos_misthos <= 2500:
        miosi = (simerinos_misthos - 1000) * 0.05
        plithos_mioseon += 1
    elif simerinos_misthos <= 4000:
        miosi = 1500 * 0.05 + (simerinos_misthos - 2500) * 0.075
        plithos_mioseon += 1
    else:
        miosi = 1500 * 0.05 + 1500 * 0.075 + (simerinos_misthos - 4000) * 0.10
        plithos_mioseon += 1

    syn_mioseon += miosi

    neos_misthos = simerinos_misthos - miosi

    print(f"Σημερινός μισθός: {simerinos_misthos:.2f} - Μείωση: {miosi:.2f} - Νέος μισθός: {neos_misthos:.2f}")

    name = input("Δώσε όνομα υπαλλήλου (ΤΕΛΟΣ για διακοπή): ")

print(f"\nΠλήθος υπαλλήλων: {plithos}")
print(f"Σύνολο σημερινών μισθών (χωρίς μειώσεις): {syn_sim_misthon:.2f}")
print(f"Σύνολο μειώσεων: {syn_mioseon:.2f}")
print(f"Πλήθος υπαλλήληων με μείωση μισθού: {plithos_mioseon}")
