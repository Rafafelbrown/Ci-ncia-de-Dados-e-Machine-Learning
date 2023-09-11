import math

# Insira os valores dos lados do triângulo
a = float(input("Insira o comprimento do lado a: \n"))
b = float(input("Insira o comprimento do lado b: \n"))
c = float(input("Insira o comprimento do lado c: \n"))

# Calcula o ângulo em radianos
cos_a = (b**2 + c**2 - a**2) / (2*b*c)
sin_a = math.sqrt(1 - cos_a**2)

# Exibe os resultados
print(f"O seno do ângulo A é {sin_a:.2f}\n")
print(f"O cosseno do ângulo A é {cos_a:.2f}\n")
