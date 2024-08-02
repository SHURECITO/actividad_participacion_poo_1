def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

grados_f = float(input("Ingresa la temperatura en grados fahrenheit: "))
grados_c = fahrenheit_a_celsius(grados_f)

print(grados_f, " grados F, equivale a ",grados_c," Celsius")
