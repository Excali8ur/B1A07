# Samenvatting Introduction to Python - Dierbach
# Auteur: Rianne Boumans - 2019
# Hoofdstuk 2 - Text Format

# It is important to understand the limitations of floating-point representation.
# For example, the multiplication of two values may result in arithmetic overflow,
# a condition that occurs when a calculated result is too large in magnitude (size) to be represented,
# This results in the special value inf ("infinity") rather than the arithmetically correct result 3.0e410,
# indicating that arithmetic overflow has occurred.
print("Infinity voorbeeld: 1.5e200 * 2.0e210")
print(1.5e200 * 2.0e210)
# Similarly, the division of two numbers may result in arithmetic underflow, a condition that occurs when
# a calculated result is too small in magnitude to be represented.
# This results in 0.0 rather than the arithmetically correct result 1.0e-400,
# indicating that arithmetic underflow has occurred.
print("Arithmetic underflow: 1.0e-300 / 1.0e100")
print(1.0e-300 / 1.0e100)

# Format Function
# Vooral heel handig om tekst leesbaar / netjes op het scherm te krijgen

### Cijfers beter leesbaar maken:
print("12/5: ", 12 / 5)
print("format(12/5, '.2f')", format(12 / 5, '.2f'))
print("5/7: ", 5 / 7)
print("format(5/7, '.2f')", format(5 / 7, '.2f'))
print("format(5/7, '.5f')", format(5 / 7, '.5f'))
# For very large (or very small) values 'e' can be used as a format specifier
print("format(2 ** 100, '.6e')", format(2 ** 100, '.6e'))

tax = 0.08
print("Zonder format: $", (1 + tax) * 12.99)
print("Met format: $", format((1 + tax) * 12.99, '.2f'))
# Finally, a comma in the format specifier adds comma separators to the result
print(format(13402.25, ',.2f'))

### Tekst uitlijnen:
print("format('Hello', '<20')")
print(".", format('Hello', '<20'), ".")
print("format('Hello', '20')")
print(".", format('Hello', '20'), ".")

print("format('Hello', '>20')")
print(".", format('Hello', '>20'), ".")

print("format('Hello', '^20')")
print(".", format('Hello', '^20'), ".")

print('Hello', format('#', '_<20'), 'Have a Nice Day!')
print('Hello', format('#', '1>20'), 'Have a Nice Day!')
print('Hello', format('#', '&^20'), 'Have a Nice Day!')

### Gebruik van enters en tabs
# Als een stuk tekst afgedrukt wordt, kun je ook gebruik maken van enters en tabs
# Hiervoor wordt in de meeste talen dezelfde karakters gebruikt

# Voor een tab gebruik je '\t' (van Tab)
print("Eerste stuk \t tweede stuk")
print("***********************")
# Voor een enter gebruik je '\n' (van Newline)
print("Eerste regel \nTweede regel")
print("***********************")
print("Omdat\t\t\thet\tkan\n\n\n\nWaarom niet?")
print("***********************")

# LET OP: '\n' en '\t' tellen als 1 karakter (ook al worden er 2 tekens gebruikt)
# De '\' wordt een escape-character genoemd. Hiermee wordt aangeduid dat er een speciaal karakter gaat
# komen. Kijk daarom uit met '\' in teksten.
# Zeker als je gaat werken met bestandsnamen en directories, zie onderstaand voorbeeld:
print("C:\test\nieuwbestand.txt")

# Om daadwerkelijk een \ af te drukken, moet je daarom 2 \  (dus \\) plaatsen
print("Hiermee wordt 1 \\ afgedrukt")
# Een andere optie is om een 'R' te gebruiken voor een tekst (van Raw). Hiermee worden escape-characters genegeerd.
print(R"Hiermee wordt 1 \\ afgedrukt")
print(r"C:\test\nieuwbestand.txt")


### Rekenen met letters
# ASCII tabel (volledige tabel op te zoeken op internet)
letter_A = "A"
ascii_A = ord("A")
letter_a = "a"
ascii_a = ord("a")

print(letter_A, "=", ascii_A)
print(letter_a, "=", ascii_a)

ascii_getal = int(input("Geef een ascii waarde:"))
print("Het ascii getal", ascii_getal, "is het karakter:", chr(ascii_getal))

# Rekenen met letters kan op deze manier wel eens van pas komen
eerste_letter = input("Geef het eerste karakter:")
tweede_letter = ord(eerste_letter) + 1
tiende_letter = ord(eerste_letter) + 9

print("1 letter verder is: ", chr(tweede_letter))
print("9 letters verder is: ", chr(tiende_letter))
