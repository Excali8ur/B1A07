### Converteren van variabelen
# Type conversion is the explicit conversion of operands to a specific type.
# Type conversion can be applied even if loss of information results.
# Python provides built-in type conversion functions int() and float(), with the int() function truncating results

# Van tekst (string) naar gehele getallen (integer):
tekst = "1234"
getal_int = int(tekst)
# Van tekst (string) naar kommagetallen (float):
tekst = "567.89"
getal_float = float(tekst)

print(getal_int, getal_float)
# En terug naar tekst (denk eraan: als je strings bij elkaar 'opteld', worden ze aan elkaar geplakt
tekst = str(getal_int) + str(getal_float)
print(tekst)

# Bekijk onderstaande regels en let op de verschillen:
print(2 + 4.5)
print(float(2) + 4.5)  # No loss of information
print(2 + int(4.5))    # Loss of information
