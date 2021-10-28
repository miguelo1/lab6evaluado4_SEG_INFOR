from math import sqrt 

def is_prime(n):    
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True

def prime_gen(limit=2000):
    n=2
    while True:
        if n<limit:
            if is_prime(n):
                yield n
            n+=1
        else:
            break

listaprimos=list(prime_gen())
# primo_seleccionado=random.choice(listaprimos) #Simulacion de un número primo (menor a 1000 para conveniencia del ejercicio elegido por el server)
# gen_aleatorio=random.randrange(1,(len(listaprimos)-1),1)



