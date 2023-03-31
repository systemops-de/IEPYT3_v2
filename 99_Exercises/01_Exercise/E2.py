# Calculates Pfand for a given number of plastic and glas bottles

print("Willkommen bei EDEKA")
print("-" * 20)

# Constants
PREIS_GLAS = 0.08
PREIS_PLASTIK = 0.25


# User Inputs Phase
n_plastik = int(input("Anzahl von Plastikflaschen: "))
n_glas = int(input("Anzahl von Glasflaschen: "))


# Calculation
guthaben = n_plastik * PREIS_PLASTIK + n_glas * PREIS_GLAS

# Rounding
guthaben = round(guthaben, 2)

# Outputsphase
print(f"Ihr Guthaben beträgt {guthaben} €")