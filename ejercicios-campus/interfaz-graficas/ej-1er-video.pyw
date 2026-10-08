from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas") #Cambia el nombre del titulo de la ventana

#raiz.resizable(1,0) #Permite o no el modificar el ancho o alto de la ventana, con valores booleanos,(1 o 0) indica si se puede o no.

#raiz.iconbitmap("rutaAIcono") #cambia el icono de la ventana, con formato .ico

#raiz.geometry("650x350") # Le indica por defecto el tama;ao de ancho y alto de la ventana

raiz.config(bg="blue") #le podemos cambiar el estilo de la ventana. por ej el bg de background con color en ingles.

miFrame=Frame()

miFrame.pack(side="right", anchor="s") #el anchor para agregar una direccion de pegado
#miFrame.pack(fill="x") #Lo rellena a lo largo del eje x, lo mismo para y agregando ,expand="True"(ensancha el frame), both para ambas direcciones

miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove") #parametros: groove, sunken

miFrame.config(cursor="hand2") #cambia el icono del cursor al posicionarse sobre el frame






raiz.mainloop()
