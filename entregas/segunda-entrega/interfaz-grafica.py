# Legajo: 114547; Nombre y apellido: Lucas Sponton
from tkinter import *
from tkinter import messagebox

def crearVentana():
    raiz=Tk()
    raiz.geometry("500x300")
    raiz.title("Ingreso de Datos")
    crearFrame(raiz)
    raiz.mainloop()


def crearFrame(raiz):
    miFrame=Frame(raiz,width=500, height=300, bg="#F55133")
    miFrame.pack(fill="x")
    formulario(miFrame)
    firma(miFrame)

def formulario(miFrame):
    frameFormulario=Frame(miFrame, bg="#F55133")
    frameFormulario.place(relx=0.45, rely=0.4, anchor="center")
    datos = []
    crearCajaTexto(frameFormulario)
    crearCajaIngreso(frameFormulario, datos)
    botonEnviar(frameFormulario, datos)

def crearCajaTexto(formulario):
    nombreLabel=Label(formulario, text="Nombre:", bg="#F55133", fg="#180501")
    nombreLabel.grid(row=0, column=0, sticky="e")

    apellidoLabel=Label(formulario, text="Apellido:", bg="#F55133", fg="#180501")
    apellidoLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    emailLabel=Label(formulario, text="Email:", bg="#F55133", fg="#180501")
    emailLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

def crearCajaIngreso(formulario, datos):
    cuadroNombre=Entry(formulario, width=25)
    cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
    cuadroNombre.config(justify="center", fg="#440D03")

    cuadroApellido=Entry(formulario, width=25)
    cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
    cuadroApellido.config(justify="center", fg="#440D03")

    cuadroEmail=Entry(formulario, width=25)
    cuadroEmail.grid(row=2, column=1, padx=10, pady=10)
    cuadroEmail.config(justify="center", fg="#440D03")

    datos.append(cuadroNombre)
    datos.append(cuadroApellido)
    datos.append(cuadroEmail)

def botonEnviar(formulario, datos):
    botonEnviar=Button(formulario, text="Enviar", command=lambda: envio(datos))
    botonEnviar.grid(row=3, column=1)
    botonEnviar.config(bg="#FCC5BB", fg="#440D03",cursor="hand2")

def envio(datos):
    nombre = datos[0].get()
    apellido = datos[1].get()
    email = datos[2].get()

    if not validarTexto(nombre):
        messagebox.showerror("Error", "El nombre solo puede contener letras y hasta 25 caracteres.")
        return
    if not validarTexto(apellido):
        messagebox.showerror("Error", "El apellido solo puede contener letras y hasta 25 caracteres.")
        return
    if not validarEmail(email):
        messagebox.showerror("Error", "La dirección de email no es válida.")
        return
    messagebox.showinfo("Éxito", "Los datos fueron recibidos correctamente.")

def firma(miFrame):
    firmado= Label(miFrame, text="Hecho por: Lucas Sponton", bg="#F45133", fg="#180501", font=("Comic Sans MS", 18))
    firmado.place(relx=0.25, rely=0.98, anchor="s")


def validarTexto(cadena):
    return cadena.isalpha() and len(cadena) <= 25

def validarEmail(email):
    return (len(email) > 0 and len(email) <= 20 and email.count("@") == 1 and email[0] != "@" and email[-1] != "@")

def main():
    crearVentana()

main()