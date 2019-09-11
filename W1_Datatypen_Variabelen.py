# Samenvatting Introduction to Python - Dierbach
# Auteur: Rianne Boumans - 2019
# Hoofdstuk 1 & 2 - Dataypen & Variabelen

# Soorten Datatypen
# Integer / int (gehele getallen)
print("Integer: ", 27, 8, 0, -12)
# Float (komma getallen)
print("Float:", 3.14, -0.9, 8.00065, .25)
# Charakters / char (1 karakter)
print("Character:",'p', 'A', '8', '<', '%')
# String (rij van karakters / tekst)
print("String:", "aap", "Dit is een string.", "7#2s1%")
# Boolean / bool (waar/onwaar)
print("Boolean:", True, False)

### Variabelen
# Een variabele is een geheugenplaats voor tijdelijke opslag van gegevens
# Je geeft het geheugenvakje een naam en de inhoud / waarde kun je aanpassen en (her)gebruiken

# Belangrijke termen:
# Declareren: De variabele moet bekendgemaakt worden (hoe heet hij?)
# Definiëren: Je moet aangeven waarvoor hij gebruikt wordt (welk datatype?) -> Dit doet Python zelf
# Initialiseren: Je moet hem een beginwaarde geven voordat je hem kunt gebruiken

getal = 17
som = (getal + 5) * 4
kopie = som
print("kopie", kopie)
#Hierboven staan 3 variabelen: getal, som en kopie. Allemaal van het type integer

### Naamgeving Variabelen / Datacontainers
# An identifier is a sequence of one or more characters used to provide a name for a given program element.
# Python is case sensitive, thus, Line is different from line.
# Identifiers may contain letters and digits, but cannot begin with a digit.
# The underscore character, _, is also allowed to aid in the readability of long identifier names. It should not be
# used as the first character, however, as identifiers beginning with an underscore have special meaning in Python.

# A keyword is an identifier that has predefined meaning in a programming language.
# Therefore, keywords cannot be used as "regular" identifiers. Doing so will result in a syntax error,
# as demonstrated in the attempted assignment to keyword and below:

# Namen die niet toegestaan zijn:
# and = 10      # -> and is een keyword
# 1e_getal = 5  # -> Niet beginnen met een getal
# een%getal = 1 # -> Geen speciale tekens toegestaan (behalve _)
# _getal = 10   # -> namen met een _ aan het begin hebben een speciale betekenis (niet zomaar gebruiken!!)

# Wat mag dan wel? Alle andere dingen ;)
eerste_getal = 15
kies_maar_iets_leuks = "Iets Leuks"
a = [1,2,3,100]
x1 = 5
x2 = 7
honderd = 200

# Ondanks dat veel mag, wordt aangeraden om variabelen nuttige namen te geven!!
# Dat is voor jezelf en andere vele malen leesbaarder, zeker na een tijdje

