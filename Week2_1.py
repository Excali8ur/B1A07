#Week 2.1
print("Infinity voorbeeld: 1.5e200 * 2.0e210")
print(1.5e200 * 2.0e210)
print("Arithmetic underflow: 1.0e-300 / 1.0e100")
print(1.0e-300 / 1.0e100)

print("12/5: ", 12/5)
print("format(12/5, '.2f')",format(12/5, '.2f'))
print("5/7: ",5/7)
print("format(5/7, '.2f')",format(5/7, '.2f'))


tax = 0.08
print('Your cost: $', (1 + tax) * 12.99)
print('Your cost: $', format((1 + tax) * 12.99, '.2f'))
print(format(13402.25, ',.2f'))

letter_A = "A"
ascii_A = ord("A")
letter_a = "a"
ascii_a = ord("a")

print(letter_A, "=", ascii_A)
print(letter_a, "=", ascii_a)

#ascii_getal = int(input("Geef een ascii waarde:"))
#print(chr(ascii_getal))

print("format('Hello', '<20')")
print(".",format('Hello', '<20'),".")
print("format('Hello', '20')")
print(".",format('Hello', '20'),".")

print("format('Hello', '>20')")
print(".",format('Hello', '>20'),".")

print("format('Hello', '^20')")
print(".",format('Hello', '^20'),".")

print('Hello', format('#', '_<20'), 'Have a Nice Day!')
print('Hello', format('#', '1>20'), 'Have a Nice Day!')
print('Hello', format('#', '&^20'), 'Have a Nice Day!')













