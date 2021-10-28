from prime_gentest import*


#ciclo while pa generar un primo privado para el cliente conocido solo por este
while True:
    global p
    try: 
        p=int(input("Anote el número primo privado(P): "))
        if p==0:
            print("Valor no puede ser 0")
        elif is_prime(p)==False:
            print("Valor no es primo")  
        else:
            break
    except:
        print("Input erróneo")
        
        
