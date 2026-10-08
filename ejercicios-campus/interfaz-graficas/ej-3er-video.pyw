





from tkinter import *

root=Tk()

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre) 
#cuadroNombre.place(x=100, y=100) 
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame) 
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame) 
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4,column=1, padx=10, pady=10)

scrollVertical=Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew") #le indica que tome el alto q ocupe la entrada de texto a la scrollbar


textoComentario.config(yscrollcommand=scrollVertical.set) #pone el scroll bar q coincuida con donde estoy parado en el texto


nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10) 

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10) 

passLabel=Label(miFrame, text="Contrasena:")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10) 

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10) 

def codigoBoton():
    minombre.set("Juan")


botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()


root.mainloop()






