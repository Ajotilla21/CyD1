# Leer 10 notas y contar cuantas son menores a 5 y cuantas mayores.
aprobados=0
suspensos=0
for x in range(10):
    nota=int(input("Introduce una nota: "))
    if (nota<5):
        suspensos=suspensos+1
    else:
        aprobados=aprobados+1
print("Aprobados: ",aprobados)
print("Suspensos: ",suspensos)
