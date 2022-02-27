
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
    return listaN 



Resultado  =   map(eliminarMultiplos,listaN)  
print(list(Resultado)) 
print()
result = filter(eliminarMultiplos, listaN)
print(list(result))



