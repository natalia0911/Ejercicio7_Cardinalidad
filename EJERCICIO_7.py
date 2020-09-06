# Creado por Natalia Vargas Reyes 219077180
# Fecha creacion: 30/09/2020
# Version python 3.8.5

def detPrimo(num,cont):
    """
    Funcion: Decir si un numero es primo o no.
    Entradas: num,cont.
    Salidas: True o False.
    """
        
    if num%cont == 0 and num!=2 or num==1:
        return False
    elif cont > num/2:
        return True
    else:
        return detPrimo(num,cont+1)



def detPrimo_Aux(num):
    """
    Funcion: validar el num.
    Entradas: num.
    Salidas: True o false.
    """
    try:
        num = int(num)
        if num < 1:
            return False
        else:
            return detPrimo(num,2)
    except:
        return False


def conjunto(rango):
    """
    Funcion: Devuelve el conjunto.
    Entradas: Rango de numeros enteros positivos.
    Salidas: conjunto lista.
    """
    conjunto=[]
    for i in range(rango):
        numero=0
        num= str(i)
        if ((len(num)>1 and len(num)<3)and detPrimo_Aux(i)):
            #Si entra al if es primo y de dos digitos
            for j in num:
                numero+=int(j)
            if numero==10:
                conjunto.append(numero)
                
    return conjunto


#Programa principal
print("La cardinalidad del conjunto: ",len(conjunto(100)))

