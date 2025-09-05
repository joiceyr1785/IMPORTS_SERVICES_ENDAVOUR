from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pyodbc

class UbicacionTK:

    def __init__(self, app):
        self.app = app
        self.app.title("UBICACIÓN")
        self.app.geometry("640x480")



    # CONECTAMOS A LA BBDD IMPORTS_SERVICES_ENDAVOUR
        self.db = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=USUARIO-MKQRT2U;"
            "DATABASE=IMPORTS_SERVICES_ENDAVOUR;"
            "Trusted_Connection=yes;"
        )

        self.cursor = self.db.cursor()

        frame = LabelFrame(self.app, text='Nueva Ubicacion')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        lb_distrito = Label(frame, text='Distrito : ')
        lb_distrito.grid(row=1, column=0)
        self.txt_distrito = Entry(frame)
        self.txt_distrito.grid(row=1, column=1)

        # Grilla de ubicacion
        self.tree = Treeview(self.app)
        self.tree['columns'] = ('Distrito', 'Provincia')

        self.tree.column('#0', width=80, stretch=NO)
        self.tree.column('Distrito', width=150)
        self.tree.column('Provincia', width=150)

        self.tree.heading('#0', text='ID_UBICACION')
        self.tree.heading('Distrito', text='Distrito')
        self.tree.heading('Provincia', text='Provincia')

        self.tree.grid(row=5, column=0, padx=20, pady=20)
        self.cargar_ubicacion()

    def cargar_ubicacion(self):
        #limpiar el treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # cargar ubicacion
        self.cursor.execute("Select id_ubicacion, distrito, provincia from Dim_Ubicacion")
        for row in self.cursor.fetchall():
            self.tree.insert('', END, text=row[0], values=(row[1:]))


if __name__ == "__main__":
    app = Tk()
    app_ubicacion = UbicacionTK(app)
    app.mainloop()