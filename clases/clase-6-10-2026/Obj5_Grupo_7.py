# Legajo: 114547, Nombre y apellido: Lucas Sponton
from tkinter import *
from tkinter import messagebox

def crear_ventana_login():
    raiz = Tk()
    raiz.title("Login Grupo 7")
    raiz.geometry("300x130")
    raiz.resizable(0, 0)
    raiz.iconbitmap("IMG_Grupo_7.ico")
    raiz.config(bg="#12E3CF")
    datos(raiz)
    raiz.mainloop()

def datos(raiz):
    alumno = Label(raiz, text="Usuario Alumno:")    
    alumno.grid(row=0,column=0, sticky="w", padx=5, pady=5)
    
    clave = Label(raiz, text="Clave:")
    clave.grid(row=1,column=0, sticky="w", padx=5, pady=5)
    
    cuadro_alumno=Entry(raiz)
    cuadro_alumno.grid(row=0, column=1)
    cuadro_alumno.config(justify="center")
    
    cuadro_clave=Entry(raiz)
    cuadro_clave.grid(row=1, column=1)
    cuadro_clave.config(show="*", justify="center")
    
    boton(raiz, cuadro_alumno, cuadro_clave)

def boton(raiz, cuadro_alumno, cuadro_clave):
    boton_ingresar = Button(raiz, text="Ingresar", command=lambda: validar_ingreso(cuadro_alumno.get(), cuadro_clave.get()), width=12, font=("",8)) 
    boton_ingresar.grid(row=2, column=0, columnspan=2)
    
    boton_registrarse = Button(raiz, text="Registrarse", width=12, font=("",8), command=lambda: ventana_registro(raiz)) 
    boton_registrarse.grid(row=3, column=0, columnspan=2, pady=2)

def obtener_usuarios_claves():
    
    usuarios_claves = { 
        "Lautaro": "1234", 
        "Alan": "fiuba2026", 
        "Milena": "python123",
        "Sofia": "benin",
        "Sabrina": "burkina",
        "Lucas": "messi"
        } 
    return usuarios_claves
    
def validar_ingreso(usuario, clave): 
    diccionario = obtener_usuarios_claves() 
    if usuario in diccionario and diccionario[usuario] == clave: 
        messagebox.showinfo("Información", "Usuario y Clave Correctos") 
    else: 
        messagebox.showerror("Error", "Algunos de los datos ingresados es Incorrecto")


def ventana_registro(raiz):
    ventana = Toplevel(raiz)
    ventana.title("Registro Grupo 7")
    ventana.geometry("300x130")
    ventana.resizable(0, 0)
    ventana.iconbitmap("IMG_Grupo_7.ico")
    ventana.config(bg="#D271EA")
    data_registro(ventana)


def data_registro(ventana_reg):
    Label(ventana_reg, text="Nuevo Usuario:", bg="#12E3CF").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    Label(ventana_reg, text="Nueva Clave:", bg="#12E3CF").grid(row=1, column=0, sticky="w", padx=5, pady=5)

    cuadro_alumno_nuevo=Entry(ventana_reg)
    cuadro_alumno_nuevo.grid(row=0, column=1)
    cuadro_alumno_nuevo.config(justify="center")
        
    cuadro_clave_nueva=Entry(ventana_reg)
    cuadro_clave_nueva.grid(row=1, column=1)
    cuadro_clave_nueva.config(show="*", justify="center")
    
    boton_guardar = Button(ventana_reg, text="Crear usuario", command=lambda: validacion_usuario(cuadro_alumno_nuevo.get(), cuadro_clave_nueva.get()))
    boton_guardar.grid(row=3, column=0, columnspan=2, pady=2)
    
    
def validacion_usuario(cuadro_alumno_nuevo, cuadro_clave_nueva):
    diccionario= obtener_usuarios_claves()
    if cuadro_alumno_nuevo == "" or cuadro_clave_nueva == "":
        messagebox.showwarning("Aviso", "Los datos no pueden estar vacios.")
    elif cuadro_alumno_nuevo not in diccionario:
        diccionario[cuadro_alumno_nuevo] = cuadro_clave_nueva
        print(diccionario)
        messagebox.showinfo("Registrado", "Se ha registrado el usuario.")
    else:
        messagebox.showwarning("Reintentar", "Usuario ya existente.") 

def main():
    crear_ventana_login()

main()