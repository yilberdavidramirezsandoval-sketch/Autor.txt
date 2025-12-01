def dar_letra():
    while True:
        print ("digite la letra 'A' para actualizar sistema")
        print ("digite la letra 'B' para eliminar catalogo")
        print ("digite la letra 'C' para crear programa")
        print ("digite la letra 'D' para salir del programa")
        letra = str (input ("seleccione opcion"))
        return letra 

def validar_letra(dato_let):

     if dato_let=='D' or dato_let=='d':
        mensaje = "finalizando con exit. "
     elif dato_let == 'A' or dato_let== 'a':
        mensaje = "actualizando sitema........."

     elif dato_let == 'B' or dato_let == 'b':
         mensaje = "eliminando catalogo............."
     elif dato_let == 'C' or dato_let=='c':
        mensaje = "creando productos............"
     
     return mensaje 

def dar_mensaje(dato_mensaje ):
    print("se esta " + dato_mensaje)  

def mensaje_alt()  :
    print("EL DO_WHILE ha finalizado")


#******************zona de codigo**************

dato_let = dar_letra()
dato_mensaje = validar_letra(dato_let)
dar_mensaje (dato_mensaje)
mensaje_alt()