# Universidad Finis Terrae, Laboratorio Evaluado nÂ°2 (lab4)
# Profesor: Manuel Alba
# Estudiantes: Miguel Orellana | Ismael Solis
# Fecha de entrega: 27 de octubre 2021
from ServidorRSA import*
from ClienteRSA import*
from math import gcd 


#una funcion de inverso multiplicativo que encontramos en google para simplificar trabajo no nos mate pls
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#---------------------

n=p*q

fi=(p-1)*(q-1)

print("el valor publico n es:",n)#para probar que de numeros, como un texto de debug pero charcha 
print("el valor de fi(n) es:",fi)


verdadero=True

while verdadero==True: #while gigante pa q no se arruine el codigo poniendo un valor de e falso y tener que hacer f5 altiro
    global maximus
    global e
    
    try: 
        e=int(input("Anote el número público e: "))
        if e==0:
            print("Valor no puede ser 0")
        elif e==fi:
            print("Valor no puede ser fi, introduzca un numero menor")#tiraba hartos problemas este while en general uwu
        elif e==1:
            print("Valor no puede ser 1, introduzca un numero mayor")            
        
        while True:
            if gcd(e,fi)!=1:
                print("Valor de GCD (MCD en español) no puede ser distinto de 1, intente otro valor e")
                break
            
            elif gcd(e,fi)==1 and e!=1: 
                print("El valor publico e es igual a:", e, "y efectivamente tiene un mcd de 1")      
                verdadero=False
                break
            else:
                print("Valor de e probablemente sea erróneo, y/o el MCD es mayor a 1")
                break
        else:# aca iwal
            print("El valor publico e es igual a:", e)
            
    except:
        print("Input erróneo")
        

llae_privaa=modinv(e,fi)#Esta es la llave privada d
print("la yae privaa es", llae_privaa)



elmalditomensaje=input("Introduzca el mensaje a encriptar: ")
elmalditomensaje=bytes(elmalditomensaje, 'utf-8')
f=int.from_bytes(elmalditomensaje, byteorder='big')


enc=((f)^e)%n
print(enc)
with open( 'mensajeentrada.txt', 'w' ) as a:
    a.write(str(enc))


dec= (enc**llae_privaa)%n           #no tenemos como decriptarlo de int --> byte --> str .. F de aca pa abajo ta malo pero queda la idea
paso1dec=int.to_bytes(2,byteorder='big')
paso2dec=paso1dec.decode('utf-8')

with open( 'mensajeentrada.txt', 'r' ) as a:
    a.read(dec)





























