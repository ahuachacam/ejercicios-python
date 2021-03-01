# Ejercicio 1
nombre=input("What is your name?")
print("hello, {}".format(nombre))
# Ejercicio 2
while True:
    key=input()
    lista1=[]
    for i in key:
        lista1.append(i.lower())
    lista1=sorted(lista1)
    abecedario="abcdefghijklmnopqrstuvwxyz"
    lista2=[]
    for i in abecedario:
        lista2.append(i)
    if lista1!=lista2:
        print("1")
        break
    pl=input("plaintext: ")
    ci=""
    for i in pl:
        if i.isalpha():
            if i.islower():
                index=lista2.index(i)
                c=""
                c+=key[index]
                ci+=c.lower()
            else:
                index=lista2.index(i.lower())
                c=""
                c+=key[index]
                ci+=c.upper()
        else:
            ci+=i
    print("ciphertext: ",ci)
    print("0")
# Ejercicio 3
cant=float(input("ingresa la cantidad depositada"))

cant=round(cant*1.04,2)
print("cantidad de ahorros tras el primer año:",cant)

cant=round(cant*1.04,2)
print("cantidad de ahorros tras el segundo año:",cant)

cant=round(cant*1.04,2)
print("cantidad de ahorros tras el tercer año:",cant)


#
a=float(input("ingrese el coficiente cuadratico: "))
b=float(input("ingrese el 2do coficiente lineal: "))
c=float(input("ingrese el 3er coficiente independiente: "))

try:
    R=b**2-4*a*c

    if R>0:
        X1=round((-b-(R)**0.5)/(2*a),2)
        X2=round((-b+(R)**0.5)/(2*a),2)
        print("""
        Primera raiz: {}
        Segunda raiz: {}""".format(X1,X2))
    elif R==0:
        print("""
        Raiz Unica: {}
        """.format(X1))
    else:
        print("Ecuación no presenta solución real")
except:
    if a==0:
        print("No es un ecuacion de segundo grado")