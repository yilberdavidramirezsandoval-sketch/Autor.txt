def definir_numero():
    numero = int(input("digite un numero del 1 al 12:"))
    return numero
def procesar_resultado(numero):
    
    match numero:
        case 1:
            print("el mes de enero.")
        case 2:
            print("el mes de febrero.")
        case 3:
            print("el mes de marzo.")
        case 4:
            print("el mes de abril.")
        case 5:
            print("el mes de mayo.")
        case 6:
            print("el mes de junio.")
        case 7:
            print("el mes de julio.")
        case 8:
            print("el mes de agosto.")
        case 9:
            print("el mes de septiembre.")
        case 10:
            print("el mes de octubre.")
        case 11:
            print("el mes de noviembre.")
        case 12:
            print("es el mes de diciembre.")

def imprimir_resultado():
    print("el programa finaliza.")
    
#***************codigo principal**************

numero = definir_numero()
procesar_resultado(numero)
imprimir_resultado()
    
        
        