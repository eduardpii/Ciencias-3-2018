from pila import *
from arbol import *

cuentaNumeros=0
aux = 0
pila = Pila ()
        
def convertir(lista, pila,cuentaNumeros):
    if lista != []:
        if lista[0] in "+-*/=":
            if pila.es_vacia() != True:
                nodo_der = pila.desapilar()
            else:
                return False
            if pila.es_vacia() != True:
                nodo_izq = pila.desapilar()
            else:
                return False
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
            cuentaNumeros=0
        else:
            if cuentaNumeros<2:
                pila.apilar(Nodo(lista[0]))
                cuentaNumeros=cuentaNumeros+1
            else:
                return False
        return convertir(lista[1:],pila,cuentaNumeros)
    return True

def evaluar(arbol):
    if arbol.valor == "=":
        resultado =arbol.der.valor+ "=" +str(evaluar(arbol.izq))
        return resultado
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

def cargarArchivo(nombre):
    archivo = open(nombre,"r")
    lista =[]
    for linea in archivo.readlines():
        expresion=linea.split(" ")
        lista.append(expresion[:-1])
    return lista

def verificaCaracter(lista):
    if(lista[-2].isalpha()):
        return True
    else:
        return False
    
def ejecutar(lista):
    if lista != []:
        if(convertir(lista[0],pila,cuentaNumeros) and verificaCaracter(lista[0])):
            print evaluar(pila.desapilar())
        else:
            print("error")
        return ejecutar(lista[1:])
        
    
    

def main ():
    listaDatos=cargarArchivo("datos.txt")
    ejecutar(listaDatos)
   
    
if __name__ == "__main__":
    main()



