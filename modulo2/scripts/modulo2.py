#ejercicio 1
while True:
    try:
        inpu=str(input("""
                Elija una opción:
                   1)ingresar la altura de la piramide
                   2)para salir
                   opción elegida: """))
        if inpu=="1":
            height=int(input("""
            ingrese la altura de la piramide: """))
            if height<0:
               print("escriba otro número ")
            for i in range(height):
                print(" "*(height-i-1)+"#"*(i+1))
        elif inpu=="2":
                break
    except:
        print("escriba otro número ")
#ejercicio 2
import string
alfabeto=string.ascii_lowercase
try:
    a==0
    while a==0:
        k=int(input(""))
        if k>=0:
            break
        else:
            print("1")
            a==0
    pl=input("plaintext: ")
    ci=""
    for l in pl:
        if l.lower() in alfabeto:
            p=alfabeto.find(l.lower())
            c=(p+k)%26
            if l.islower():
                ci+=alfabeto[c]
            else:
                ci+=alfabeto[c].upper()
        else:
            ci+=l
    print("ciphertext: ",ci)
    print("0")

except:
    print("1")
#ejercicio 3 #ejercicio 4
#ejercicio 5
def ingresenota():
    try:
        nota=float(input("ingrese nota entre 0 y 10: "))
        if nota >=0 and nota<=10:
            return nota
        else:
            print("introcusca notas entre 0 y 10")
            ingresenota()
    except:
        print("introduce un número")
        ingresenota()

try:
    n=int(input("ingresa el número de alumnos: "))
    
    datos=list()
    for i in range(1,n+1):
        registro={}
        registro["nombre"]=input("nombre completo {}: ".format(i))
        registro["nota1"]=ingresenota()
        registro["nota2"]=ingresenota()
        registro["nota3"]=ingresenota()
        datos.append(registro)
    print(datos)
except:
    print("ingrese un numero")

            
    

def LISTAR(lista):
    for i in lista:
        print("-------Alumno {}-------".format(lista.index(i)+1))
        print("""
        Nombre: {}
        nota1: {}
        nota2: {}
        nota3: {}
        """. format(i["nombre"], i["nota1"], i["nota2"], i["nota3"]))
LISTAR(datos)

def promedio(datos):
    prom=float()
    for i in datos:
        prom=round((i.get("nota1")+i.get("nota2")+i.get("nota3"))/3,2)
        i["promedio"]=prom    
promedio(datos)

for i in datos:
    situacion=""
    if i["promedio"]<4:
        situacion+="Desaprobado"
        print("""
        --------Alumno {}----------
        Nombre: {}
        Situación: {}""".format(datos.index(i)+1, i.get("nombre"), situacion))
    else:
        situacion+="Aprobado"
        print("""
        --------Alumno {}----------
        Nombre: {}
        Situación: {}""".format(datos.index(i)+1, i.get("nombre"), situacion))


for i in datos:
    print("""
        --------Alumno {}----------
        Nombre: {}
        promedio: {}""".format(datos.index(i)+1, i.get("nombre"), i.get("promedio")))

        def maximo(datos):
    maximo=[]
    for i in datos:
        maximo.append(i.get("promedio"))
    m=float()
    ind=float()
    m=max(maximo)
    ind=maximo.index(m)
    print("""
    promedio más alto obtuvo: """, datos[ind].get("nombre"))
maximo(datos)

def minimo(datos):
    minimo=[]
    for i in datos:
        minimo.append(i.get("promedio"))
    m=float()
    ind=float()
    m=min(minimo)
    ind=minimo.index(m)
    print("""
    promedio más baja obtuvo: """, datos[ind].get("nombre"))
minimo(datos)

def buscar(datos):
    nombre=input("Nombre para buscar: ")
    m=[]
    for i in datos:
        m=[]
        m=[n for n in (i.get("nombre")).split(" ")]
        n=[a for a in nombre.split(" ")]
        for k in m:
            for j in n:
                if j.lower()==k.lower(): 
                    ind=float()
                    ind=datos.index(i)
                    print("""
                    Nombre: {}
                    nota1: {}
                    nota2: {}
                    nota3: {}
                    promedio: {}
                    """. format(i["nombre"], i["nota1"], i["nota2"], i["nota3"], i["promedio"]))
buscar(datos)
#ejercicio 6
#ejercicio 7