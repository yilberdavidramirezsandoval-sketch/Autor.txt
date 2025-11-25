# **************** ZONA DE FUNCIONES ********************

def capturar_nombre():
    nombre_usuario = input("Escriba el nombre del usuario: ")
    return nombre_usuario
def capturar_rol():
    rol_usuario = input("Escriba su rol: ")
    return rol_usuario
def capturar_hora():
    hora = int(input("Escriba la hora (0-23): "))
    
    if 0 <= hora < 12:
        saludo = "Buenos días"
    elif 12 <= hora < 18:
        saludo = "Buenas tardes"
    elif 18 <= hora < 24:
        saludo = "Buenas noches"
    else:
        saludo = "Hora incorrecta"
    
    return saludo, hora

def hacer_mensaje(nombre_usuario, rol_usuario, saludo, hora):
    mensaje = f"{saludo} {nombre_usuario}. Su rol es {rol_usuario}. La hora es {hora}."
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)


# **************** ZONA DE CÓDIGO PRINCIPAL ********************

dato_nombre = capturar_nombre()
dato_rol = capturar_rol()
saludo, dato_hora = capturar_hora()
dato_mensaje = hacer_mensaje(dato_nombre, dato_rol, saludo, dato_hora)
imprimir_mensaje(dato_mensaje)