
import class_biblioteca
import class_usuarios
import class_libros
import time
#import os
# impo
from B_logger import Logger
import traceback
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()                   # importante     <---
root.withdraw()                  # importante     <---
# log.add_to_log("level", "message")
# log.add_to_log("level", "message" {traceback.format_exc()})
log = Logger()                   

def menu_principal():
    print("=============================================")
    print(f"Bienvenido a {class_biblioteca.biblioteca.name_biblioteca}")
    print("=============================================")
    print("Como Acceder? - Seleccione una opción (1 o 2 o 3 o 4):")
    print("(1)registrarse ")
    print("(2)iniciar sesion ")
    print("(3)biliotecario ")
    print("(4)salir ")


##########################################################################################################

def opcion_1():
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contraseña_usuario = input("Ingrese una contraseña: ")
    class_biblioteca.agregar_usuario(nombre_usuario, contraseña_usuario)
    log.add_to_log("info", f"el Usuario {nombre_usuario} registrado exitosamente.")
        
    print(f"Usuario {nombre_usuario} registrado exitosamente.")
    print("Volviendo al Menu Principal.....")
    time.sleep(2)
    menu_principal()
    

###########################################################################################################

def opcion_2():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    usuario_contraseña = input("Ingrese su contraseña: ")
    usuario_valido = class_usuarios.validar_usuario(nombre_usuario, usuario_contraseña)
    if usuario_valido is None: 
        log.add_to_log("warning", "El USUARIO intentó iniciar sesión con credenciales incorrectas")
        print("Usuario o contraseña incorrectos... intente mas tarde")                # bien    
        time.sleep(2)
        #menu_principal() --> no se usa porque el menu_principal() se llama en un while infinito, 
        
    else:
        log.add_to_log("info", f"El USUARIO {nombre_usuario} inició sesión exitosamente.")
        print("=============================================")
        print(f"  Bienvenido, {usuario_valido['nombre']}!  ")
        menu_usuario(usuario_valido)
    

def menu_usuario(usuario_valido):
    print("=============================================")
    print("¿Qué desea hacer?")
    print(".....................")
    print("(1) leer ")
    print("(2) pedir prestado")
    print("(3) devolver libro")
    print("(4) Volver al menú principal")
    print("_____")
    opcion_usuario = input("> ")
    print("_____")
    if opcion_usuario == "1":
        log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} seleccionó la opción (1): leer libro")
        sub_menu_1_opcion_usuario(usuario_valido)
    elif opcion_usuario == "2":
        log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} seleccionó la opción (2): pedir prestado libro")
        sub_menu_2_opcion_usuario(usuario_valido)
    elif opcion_usuario == "3":
        log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} seleccionó la opción (3): devolver libro")
        sub_menu_3_opcion_usuario(usuario_valido)
    elif opcion_usuario == "4":
        log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} seleccionó la opción (4): volver al menú principal")
        print("volviendo al menu principal...")
        time.sleep(2)
        #menu_usuario() --> no se usa porque el menu_principal() se llama en un while infinito.
    else:
        log.add_to_log("warning", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} ingresó una opción no válida en el menú de usuario")
        print("error, intente de vuelta")
        time.sleep(1.5)
        menu_usuario(usuario_valido)

def volver_al_menu_u(usuario_valido):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("(1) volver al menu o igual")
    opcion_u_leer = input("> ")
    log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} volvio al menú")
    if opcion_u_leer == "1":
        menu_usuario(usuario_valido)
    else:
        menu_usuario(usuario_valido)

def libro_esta(usuario, id_libro):
    if id_libro not in [libro["id"] for libro in usuario["libros_tenidos"]]:
        return False
    else:
        return True
    
def sub_menu_1_opcion_usuario(usuario_valido):
    print("------")
    class_usuarios.ver_libros_tenidos(usuario_valido)
    id_libro_tenido = int(input("seleccione la id del libro a leer: "))  
    if not libro_esta(usuario_valido, id_libro_tenido):
        log.add_to_log("warning", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} intentó leer un libro que no tiene.")
        print("Error: No tienes un libro con esa ID.")
        time.sleep(1.5)
        menu_usuario(usuario_valido)
        return
    print("--------------------------------------------------------------------------------")
    class_usuarios.leer(usuario_valido, id_libro_tenido)
    volver_al_menu_u(usuario_valido)


def sub_menu_2_opcion_usuario(usuario_valido):
    class_biblioteca.ver_libros()
    print("------")
    print("ingrese el id del libro a pedir prestado: ")
    id_libro = int(input("> "))
    if not class_libros.validar_id_libro(id_libro):
        log.add_to_log("warning", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} intentó pedir prestado un libro que no existe.")
        print("Error: No existe un libro con esa ID.")
        time.sleep(1.5)
        menu_usuario(usuario_valido)
        return
    class_usuarios.pedir_prestado(usuario_valido, id_libro)
    log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} pidió prestado el libro con ID: {id_libro}")
    print("...")
    print("libro tenido exitosamente")
    volver_al_menu_u(usuario_valido)


def sub_menu_3_opcion_usuario(usuario_valido):
    class_usuarios.ver_libros_tenidos(usuario_valido)
    print("-------------------------------------------------------------")
    print("ingrese el id del libro a devolver")
    id_libro = int(input("> "))
    if not libro_esta(usuario_valido, id_libro):
        log.add_to_log("warning", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} intentó devolver un libro que no tiene.")
        print("Error: No tienes un libro con esa ID.")
        time.sleep(1.5)
        menu_usuario(usuario_valido)
        return
    print("...")
    class_usuarios.devolver_libro(usuario_valido, id_libro)
    log.add_to_log("info", f"El usuario: [{usuario_valido['id']}]{usuario_valido['nombre']} devolvió el libro con ID: {id_libro}")
    print("libro devuelto exitosamente")
    volver_al_menu_u(usuario_valido)

##########################################################################################################

def opcion_3():
    nombre_bibliotecario = input("Ingrese su nombre de bibliotecario: ")
    biblioteca_contraseña = input("Ingrese la contraseña de la biblioteca: ")
    if biblioteca_contraseña == class_biblioteca.biblioteca.contraseña and nombre_bibliotecario == class_biblioteca.biblioteca.name_biblioteca:
        log.add_to_log("info", "bibliotecario accedió con éxito al sistema")
        print("Acceso concedido. Bienvenido, bibliotecario!")
        menu_bibliotecario()
    else:
        log.add_to_log("warning", "se intentó acceder como bibliotecario con credenciales incorrectas")
        print("acceso denegado...")
        time.sleep(1.5)
        #menu_principal() --> no se usa porque el menu_principal() se llama en un while infinito.

def menu_bibliotecario():
    print("=============================================")
    print("¿Qué desea hacer?")
    print(".....................")
    print("(1) ver libros disponibles")
    print("(2) Agregar libro   <-- mucha precaucion")
    print("(3) Eliminar libro  <-- precaucion")
    print("(4) Ver usuarios")
    print("(5) Eliminar usuario <-- precaucion")
    print("(6) Volver al menú principal")
    print("_____")
    opcion_bibliotecario = input("> ")
    print("_____")
    if opcion_bibliotecario == "1":
        log.add_to_log("info", "El bibliotecario seleccionó la opción (1): ver libros disponibles")
        sub_menu_1_opcion_bibliotecario()
    elif opcion_bibliotecario == "2":
        log.add_to_log("info", "El bibliotecario seleccionó la opción (2): agregar libro")
        sub_menu_2_opcion_bibliotecario()
    elif opcion_bibliotecario == "3":
        log.add_to_log("info", "El bibliotecario seleccionó la opción (3): eliminar libro")
        sub_menu_3_opcion_bibliotecario()
    elif opcion_bibliotecario == "4":
        log.add_to_log("info", "El bibliotecario seleccionó la opción (4): ver usuarios")
        sub_menu_4_opcion_bibliotecario()
    elif opcion_bibliotecario == "5":
        log.add_to_log("info", "El bibliotecario seleccionó la opción (5): eliminar usuario")
        sub_menu_5_opcion_bibliotecario()
    elif opcion_bibliotecario == "6":
        log.add_to_log("info", "El bibliotecario seleccionó la opción (6): volver al menú principal")
        sub_menu_6_opcion_bibliotecario()
    else:
        print("error, intente devuelta....")
        time.sleep(1.5)
        #menu_bibliotecario

def volver_al_menu_b():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("(1) volver al menu o igual")
    opcion_u_leer = input("> ")
    log.add_to_log("info", "El bibliotecario volvió al menú")
    if opcion_u_leer == "1":
        menu_bibliotecario()
    else:
        menu_bibliotecario()


def sub_menu_1_opcion_bibliotecario():
    class_biblioteca.ver_libros()
    print("----------------------------")
    volver_al_menu_b()


def sub_menu_2_opcion_bibliotecario(): #terminar correctamente, falta la parte de hacer bien el:
    print("           agregando libro:      ")          #contenido_libro  como hacer que tenga funcionalidad
    print(".......................................")        # agregar un archivo.txt correctamente

    # IMPORTANTE                     ### medio medio, falta estudiarlo un poco
                                     ### ver bien si falta algo.....
    titulo_libro = input("ingrese el titulo: ").strip().lower()      
    autor_libro = input("ingrese el autor: ").strip().lower()         
    genero_libro = input("ingrese el genero: ").strip().lower()
    
    if not titulo_libro:
        log.add_to_log("warning", "El bibliotecario intentó agregar un libro con título vacío")
        print("Error, titulo: '' no puede ser vacio")
        time.sleep(1.5)
        menu_bibliotecario()
        return
    
    if not autor_libro:
        log.add_to_log("warning", "El bibliotecario intentó agregar un libro con autor vacío")
        print("Error, autor: '' no puede ser vacio")
        time.sleep(1.5)
        menu_bibliotecario()
        return
    
    if not genero_libro:
        log.add_to_log("warning", "El bibliotecario intentó agregar un libro con género vacío")
        print("Error, genero: '' no puede ser vacio")
        time.sleep(1.5)
        menu_bibliotecario()
        return
    

    # 000->>>>>>>>>>
    try:
        contenido_libro = filedialog.askopenfilename(
        title="Selecciona el archivo contenido de texto correspondiente: ", 
        filetypes=[("Archivos de texto", "*.txt")])
    except Exception as e:
        log.add_to_log("error", f"Error al abrir el diálogo de selección de archivo: {traceback.format_exc()}" + f" - Error específico: {e}")
        print("Hubo un problema al abrir el diálogo de selección de archivo.")
        time.sleep(1.5)
        menu_bibliotecario()
        return


# Verificamos si el usuario no seleccionó ningún archivo
    if not contenido_libro:  # Esto cubre cuando se devuelve una cadena vacía
        log.add_to_log("warning", "El bibliotecario no seleccionó ningún archivo para el contenido del libro")
        print("No se seleccionó ningún archivo...")
        time.sleep(2)
        menu_bibliotecario()
        return
    #else:                                  
    #try:
        # Supongo que la función 'agregar_libro' necesita un archivo que se abrirá
        #with open(contenido_libro, "r", encoding="utf-8") as archivo:
         #   contenido = archivo.read()  # Leemos el contenido del archivo
        # Esto es solo para verificar que el archivo existe y es accesible
        # Ahora llamamos al método para agregar el libro
    
        
        # Guardamos solo el nombre en el diccionario
    
    
    class_biblioteca.agregar_libro(titulo_libro, autor_libro, genero_libro, contenido_libro) #contenido
    log.add_to_log("info", f"El bibliotecario agregó el libro: '{titulo_libro}' con contenido del archivo: '{contenido_libro}'")
    time.sleep(1.5)
    print("Libro creado exitosamente...")
    time.sleep(2)
    menu_bibliotecario()
    return
    
    #except FileNotFoundError:
       # print("Hubo un problema al abrir el archivo:")
        #time.sleep(1.5)
        #menu_bibliotecario()
        #return
    #

def sub_menu_3_opcion_bibliotecario(): 
    print("     Eliminar libro:     ")         
    print("............................")   
    class_biblioteca.ver_libros()
    print("....................................")
    print("ingrese el id del libro a eliminar:")      
    print("_____")
    id_libro_elim = int(input("> "))          
    print("_____")
    time.sleep(1.5)
    if not class_libros.validar_id_libro(id_libro_elim):
        log.add_to_log("warning", "El bibliotecario intentó eliminar un libro que no existe.")
        print("Error: No existe un libro con esa ID.")
        time.sleep(1.5)
        menu_bibliotecario()
        return
    class_biblioteca.eliminar_libro(id_libro_elim)  
    log.add_to_log("info", f"El bibliotecario eliminó el libro con ID: {id_libro_elim}")
    print("libro eliminado correctamente...")
    print("-------------------------------------------------------------")  
    print("(1) volver al menu o igual")
    print("(2) ver lista actualizada")
    opcion_u_leer = input("> ")
    if opcion_u_leer == "1":
        menu_bibliotecario()
    elif opcion_u_leer == "2":
        class_biblioteca.ver_libros()
        volver_al_menu_b()
    else:
        menu_bibliotecario()   


def sub_menu_4_opcion_bibliotecario():
    print("............................")   
    class_biblioteca.ver_usuarios()
    print("----------------------------")
    volver_al_menu_b()


def sub_menu_5_opcion_bibliotecario(): #terminar correctamente, solo hice la parte interfaz y un poco mas
    print("     eliminando usuario:    ")       # y no realmente la funcionalidad...
    print("............................")   
    class_biblioteca.ver_usuarios()
    print("..................")
    print("ingrese el id del usuario a eliminar:")      
    print("_____")
    id_usuario_elim = input("> ")          #no se usa la variable simplemente
    print("_____")
    if not class_usuarios.validar_id_usuario(id_usuario_elim):
        log.add_to_log("warning", "El bibliotecario intentó eliminar un usuario que no existe.")
        print("Error: No existe un usuario con esa ID.")
        time.sleep(1.5)
        menu_bibliotecario()
        return
    class_biblioteca.eliminar_usuario(id_usuario_elim)
    log.add_to_log("info", f"El bibliotecario eliminó el usuario con ID: {id_usuario_elim}")
    time.sleep(1.5)
    print("usuario eliminado correctamente...")
    print("-----------------------------------")  
    print("(1) volver al menu o igual")
    print("(2) ver lista actualizada")
    opcion_u_leer = int(input("> "))
    if opcion_u_leer == "1":
        menu_bibliotecario()
    elif opcion_u_leer == "2":
        class_biblioteca.ver_usuarios()
        volver_al_menu_b()
    else:
        menu_bibliotecario()


def sub_menu_6_opcion_bibliotecario():
    print("volviendo al menu principal....")
    time.sleep(2)
    #menu_principal() --> no se usa porque el menu_principal() se llama en un while infinito,



############################################################################################################
#--------------------------------------------------------------------------------------------------------#
log.add_to_log("info", "Iniciando el sistema de biblioteca")
    
while True:
    menu_principal()
    print("-----")
    opcion = input("> ")
    print("-----")

    if opcion == "1":
        log.add_to_log("info", "El USUARIO seleccionó la opción (1): de registrarse")
        opcion_1()

    elif opcion == "2":
        log.add_to_log("info", "El USUARIO seleccionó la opción (2): de iniciar sesión")
        opcion_2()
            
    elif opcion == "3":
        log.add_to_log("info", "El USUARIO seleccionó la opción (3): de acceder como bibliotecario")
        opcion_3()

    elif opcion == "4":
        log.add_to_log("info", "El USUARIO seleccionó la opción (4): de salir del programa")
        print("Saliendo del programa... ¡Hasta luego!")
        time.sleep(3)
        break
    else:
        log.add_to_log("warning", "El USUARIO ingresó una opción no válida")
        print("Opción no válida. Por favor, seleccione 1 o 2 o 3 o 4.")
