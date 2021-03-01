num=int(input("Ingrese el número de tarjeta: "))

def validar(num):    
    l=[]
    for i in str(num):
        l.append(i)
    l==l.reverse()
    n=len(l)
    suma=""
    l1=[]
    s=0
    val=""
    for i in range (1,n,2):
        l1.append(2*int(l[i]))
    for i in l1:
        suma +=str(i)
    for i in suma:
        s = s+int(i)
    for i in range (0,n,2):
        s=s+int(l[i])
    if s%10 ==0:
        val+="VALID"   
    else:
        val+="INVALID"
    return val



def CARD(num):
    num=str(num)
    j=int()
    j = len(num)
    card=""
    if 15 ==j and num[0]=="3" and (num[1]=="4" or num[1]=="7"):
        card+="AMEX"
    elif 16 ==j and num[0]=="5" and (num[1]=="1" or num[1]=="2" or num[1]=="3" or num[1]=="4" or num[1]=="5"):
        card+="MASTERCARD"
    elif (13 ==j or 16 ==j) and num[0]=="4" :
        card+="VISA"
    else:
        card+="INVALID"
    return card

#AMEX 34 o 37                           números de 15 dígitos
#MASTERCARD 51, 52, 53, 54 o 55         números de 16 dígitos
#VISA 4                                 números de 13 y 16 dígitos
#INVALID

if validar(num)=="VALID":
    amd=CARD(num)
    print(amd)
elif validar(num)=="INVALID":
    print(validar(num))

# ejercicio 2
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