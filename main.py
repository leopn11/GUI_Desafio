
import tkinter
from tkinter import ttk
window = tkinter.Tk()

def salir(event):
    print("No pudiste responder")
    window.quit()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=6)

parametro_label = ttk.Label(window, text=" - Responde si es TRUE O FALSE")
parametro_label.grid(column=0, row=0, sticky=tkinter.W, pady=7, padx=7 )

pregunta_label = ttk.Label(window, text=" 1. ¿El posicionamiento grid es el mas utilizado para generar GUI?")
pregunta_label.grid(column=0, row=2, sticky=tkinter.W, pady=7, padx=7 )

r1 = ttk.Radiobutton(window, text="TRUE", value=1)
r2 = ttk.Radiobutton(window, text="FALSE", value=2)

r1.grid(column=0, row=3, padx=6, pady=6, sticky=tkinter.W)
r2.grid(column=0, row=4, padx=6, pady=6, sticky=tkinter.W)

opcion_label = ttk.Label(window, text="Si no sabes la repuesta puedes salir ")
opcion_label.grid(column=0, row=5, sticky=tkinter.W, pady=7, padx=7 )

rSalir = ttk.Radiobutton(window, text="Salir!!!", value=6)
rSalir.grid(column=0, row=6, padx=6, pady=6, sticky=tkinter.W,)
rSalir.bind('<Button-1>', salir)

window.mainloop()