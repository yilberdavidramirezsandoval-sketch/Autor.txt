def tomar_numero():
    numero_a_digitar = int(input("digitar el numero a analizar:"))
    return numero_a_digitar
def identificar_numero(numero):
    if numero% 2==0:
        return "el numero es par"
    else:
        return "el numero es impar"
    
def enviar_mensaje(numero_a_digitar,numero):
    mensaje = f"el numero{numero_a_digitar}en{numero}"
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)

#*****************codigo principal**************
numero =1;
while numero!=0:
    dato_numero= tomar_numero()
    tipo_numero= identificar_numero(dato_numero)
    dato_mensaje = enviar_mensaje(dato_numero,tipo_numero)
    imprimir_mensaje(dato_mensaje)
    print("finalizo el programa")
    