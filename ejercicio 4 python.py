def definir_cantidad():
    return int(input("digite la cantidad de numero que desea sumar:"))

def acumular_suma(cantidad):
    suma = 0 
    for i in range(cantidad):
        print("digite el numero", str(i + 1)+":")
        numero = int(input())
        suma = suma + numero 
    return suma
def mostrar_total(suma):
    print("la sumatoria total es:",suma)
    
#****************codigo principal*********
cantidad = definir_cantidad()
suma_total = acumular_suma(cantidad)
mostrar_total(suma_total)