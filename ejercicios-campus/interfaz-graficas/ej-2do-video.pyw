#tipos de sintaxis de label
#text= texto que se muestra en el label
#anchor= COntrola la posicion del texto si hay espacio suficiente para el(center por defecto)
#bg= Color de fondo
#bitmap= mapa de bits que se mostrara como grafico
#bd= grosor del borde (2 px por defecto)
#font= tipo de fuente a mostrar
#fg= color de la fuente
#width= ancho de label en caracteres(no en pixeles)
#height= altura de label en caracteres(no en pixeles)
#image= muestra imagen en el label en lugar de texto
#justify= justificacion del texto del label

# variableLabel= ;abel(contenedor, opciones) #contenedor seria donde quiero q este si en el raiz o en el frame o un frame dentro de otro frame


from tkinter import *

root=Tk()

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

#miImagen=PhotoImage(file="rutaALaImagen .gif o .png")

miLabel= Label(miFrame, text="Hola alumnos de python", fg="red", font=("Comic Sans MS", 18)) # le paso como variable al texto el color de dicho, la tipografia y el tamano, hay mas, podria averiguar
miLabel.place(x=100, y=200) #respeta el ancho y alto q le indique anteriormente en el frame.
# Label(miFrame, text="Hola alumnos de Python").place(x="100", y="200") #otra forma si no vuelvo a utilizar la variable miLabel
# Label(miFrame, image=miImagen).place(x=100, y=200) para en vez de texto utilizar una imagen

cuadroNombre=Entry(miFrame) #para crear una casilla estilo input
#cuadroNombre.place(x=100, y=100) si solo quisiera posicionar por x e y.. pero no me da mucha libertar, mejor usar grid
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame) #para crear una casilla estilo input
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame) #para crear una casilla estilo input
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame) #para crear una casilla estilo input
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.place(x=100, y=100)#metodo grid para posicionar objetos 
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10) #posicion sticky con coodenadas cardinales para posicionar

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.place(x=100, y=100)#metodo grid para posicionar objetos 
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion de casa:")
direccionLabel.place(x=100, y=100)#metodo grid para posicionar objetos 
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10) #padding con padx o pady 

passLabel=Label(miFrame, text="Contrasena:")
passLabel.place(x=100, y=100)#metodo grid para posicionar objetos 
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10) #padding con padx o pady 

root.mainloop()