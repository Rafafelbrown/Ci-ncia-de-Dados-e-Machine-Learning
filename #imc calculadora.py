#imc calculadora
peso =float(input(print("qual o peso")))
print(peso)
altura =float(input(print("qual a altura"))) 
print(altura)
i =float( (peso/ altura**2 )*10)
y =[]
o=i/10
t=int (200)
k=int (249)
for  i in range(t, k):
    y.append(i/10 + 0.1)
pesoid= i*(altura**2)/10
print(f"peso ideal dado a altura {round(pesoid+0.001, 2)}")
print(f"imc: {round(o, 2)}\n")
if o < 16:
    print("subpeso severo\n")
elif o < 19.9:
    print("subpeso\n")
elif o <24.9:
    print("normal\n")
elif o <29.9:
    print("sobrepeso\n")
elif o < 39.9:
    print("obeso\n")
else:
    print("obeso morbido\n")
if o > 25:
 print(f"preca por mes {round((peso-pesoid)/12+0.001, 2)}")
elif o < 20:
    print(f"ganhe por mes {round((peso-pesoid)/12+0.001, 2)*(-1)}")
else:
    print("ta ok")