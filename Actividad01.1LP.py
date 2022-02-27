
Nlista  =   int(input("ingrese valor N para el rango de la lista : "))

#listas
listaN  =   [*range(2,Nlista+1)]
print(listaN)
print()


listaMarcados= []

#funcion hallar N# primo
def esPrimo(n):
    for i in range(2,n-1):
        if (n% i == 0):
            return False
    return True


#Funcion es multiplo
def esMultiplo(numero, multiplo):
   return numero   %   multiplo == 0
        
#Funcion es multiplo
def esMultiplo02(numero, multiplo):
  if numero   %   multiplo == 0:    
    return True
  else:
      return False


def eliminarMultiplos(self):
    i = 0
    while(listaN[i]*listaN[i] <= Nlista):
        # Mientras el cuadrado del elemento actual sea menor que el ultimo elemento
        for num in listaN:
            if num <= listaN[i]:
                # Cada iteracion del while hace que el for comience desde el primer elemento. 
                # Esto es para omitir los numeros primos ya encontrados
                continue
            elif num % listaN[i] == 0:
                # Si un numero es divisible entre el elemento actual del while
                # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
                listaN.remove(num)
            else:
                # Si no es divisible, entonces omitirlo (no hacer nada)
                pass
        i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)

def eliminarMultiplos1(self):
    p=0
    while(listaN[p]*listaN[p] <= Nlista):
        for num in listaN:
            if num <= listaN[p]:
                continue
            else:
                if esMultiplo(num,listaN[p]):
                    listaN.remove(num)
                else:
                    pass
        p += 1 

#print(listaN)
#print(list(map(eliminarMultiplos,listaN)))

Resultado  =   map(eliminarMultiplos1,listaN)  
print(list(Resultado)) 

#result = filter(, listaN)
#print(list(result))

