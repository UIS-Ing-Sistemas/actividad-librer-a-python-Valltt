
def collatz(numero):
    secuencia= [numero]
    while numero!= 1:
        if numero % 2==0:
            numero= numero//2
    else:
        numero= numero*3+1
        secuencia.append(numero)
        return secuencia
  

N= 12
numeros= []

for i in range (N):
    n= int(input ("Ingrese el numero : "))
    numeros.append(n)


promedio= sum(numeros)/N
    
collatzpromedio= collatz (int(promedio))
    
print ("La secuencia de collatz para el promedio es {promedio}:")
print(collatzpromedio)