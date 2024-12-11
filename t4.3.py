#sueldo de cada empleado e informe cuantos cobran entre 100 y 300 y cuantos mas
#Ademas el programa deberá informar el importe que gasta la empresa en sueldos
mas300=0
entre100y300=0
n=int(input("¿Cuantos empleados tiene la empresa?"))
for x in range(n):
    sueldo=int(input("Introduce un sueldo:"))
    if (sueldo>300):
        mas300=mas300+1
    else:
        if (sueldo>=100):
            entre100y300=entre100y300+1
print("Empleados que ganan mas de 300: ",mas300)
print("Empleados que ganan entre 100 y 300: ",entre100y300)
