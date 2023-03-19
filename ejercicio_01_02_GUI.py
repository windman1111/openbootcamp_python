import customtkinter as ctk

root = ctk.CTk()
root.title("Ejercicio 01_GUI")
root.geometry("300x200")

ctk.CTkLabel(root, text="Selecciona tu color preferido").pack()
def resetear():
    opcion.set("")

opcion = ctk.StringVar()
def actualiza_radio(valor):
    ctk.CTkLabel(root, text=valor).pack()

ctk.CTkRadioButton(root, text="rojo", variable=opcion, value="rojo").pack()
ctk.CTkRadioButton(root, text="azul", variable=opcion, value="azul").pack()
ctk.CTkRadioButton(root, text="verde", variable=opcion, value="verde").pack()
ctk.CTkRadioButton(root, text="amarillo", variable=opcion, value="amarillo").pack()

ctk.CTkLabel(root, text=opcion.get()).pack()

boton_envia = ctk.CTkButton(root, 
        text="Enviar",
        command=lambda: actualiza_radio(opcion.get())).pack()
boton_reset = ctk.CTkButton(root, 
        text="Reset",
        command=lambda: resetear).pack()

root.mainloop()
