# Samenvatting Introduction to Python - Dierbach
# Auteur: Rianne Boumans - 2019
# Hoofdstuk 2: Operatoren

### Soorten operatoren
# Optellen
uitkomst = 5 + 3
print("5 + 3 =", uitkomst)
# Aftrekken
uitkomst = 5 - 3
print("5 - 3 =", uitkomst)
# Vermenigvuldigen
uitkomst = 5 * 3
print("5 * 3 =", uitkomst)
# Delen
uitkomst = 5 / 3
print("5 / 3 =", uitkomst)
uitkomst = 5 // 3
print("5 // 3 =", uitkomst)
# Modulo (rest na deling)
uitkomst = 5 % 3
print("5 % 3 =", uitkomst)
# Machtsverheffen
uitkomst = 5 ** 3
print("5 ** 3 =", uitkomst)

# Rekenen met behulp van math library:
# Normaal zet je alle 'import' helemaal bovenaan het bestand
import math
# Machtsverheffen
uitkomst = math.pow(5, 3)
print("math.pow(5, 3) =", uitkomst)
# Worteltrekken
uitkomst = math.sqrt(5)
print("math.sqrt(5) =", uitkomst)
# math heeft nog veel meer rekenkundige functies, allemaal te vinden in de documentatie van Python

### Volgorde van operatoren
# 4 + 3 * 5
# In welke volgorde wordt dit uitgevoerd?
# (4 + 3) * 5 (= 35) of 4 + (3 * 5) (= 19)?
print("4 + 3 * 5:", 4 + 3 * 5)

# Some might say that the first version is the correct one by the conventions of mathematics.
# However, each programming language has its own rules for the order that operators are applied,
# called operator precedence, defined in an operator precedence table.
# This may or may not be the same as in mathematics, although it typically is.

# Volgorde in Python:
# ** (Exponent)                     <- van rechts naar links
# -  (Negatief)                     -> van links naar rechts
# * (keer), / en //(delen), % (mod) -> van links naar rechts
# + (optellen), - (aftrekken)       -> van links naar rechts

# Wat is de uitkomst van 2**2**3?
print("2**2**3 = ",2**2**3)
# Want ** lees je (als enige) van rechts naar links. Dus eigenlijk doet hij:
print("2**(2**3) = ", 2**(2**3))
# Anders krijg je:
print("(2**2)**3 = ",(2**2)**3)

# Ander voorbeeld:
print("4 + 2 ** 5 // 10 = ", 4 + 2 ** 5 // 10)
#Oftewel:
print("4 + ((2 ** 5) // 10) = ", 4 + ((2 ** 5) // 10))

# Tip: Wil je zeker weten dat de juiste volgorde gebruikt wordt?
# Gebruik dan haakjes en / of voer de bereking uit op meerdere regels.
