#!/usr/bin/env python
# coding: utf-8

# In[19]:


from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from sklearn import tree
import random
import mysql.connector
import validations
import saveRecords
import sklearn
import sys



#Función botón ALTA
def add_record ():
    
    titulo = val1.get().capitalize()
    descripcion = val2.get().capitalize()
    
    mi_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="Nivel_Intermedio")
    if titulo != "" and descripcion != "" and validations.validar(titulo) == 0:
        count=saveRecords.add(titulo, descripcion, mi_db)
    
        e1.delete(0, "end")
        e2.delete(0, "end")     
        obtener_reg()
        messagebox.showinfo(message="Alta registrada exitosamente", title="Alta de registro")
    else:
        messagebox.showerror(message="Se deben ingresar todos los campos y Titulo debe ser alfanumerico", title="Error al procesar ALTA")
        e1.select_range(0, "end")
        e2.select_range(0, "end")
        e1.delete(0, "end")
        e2.delete(0, "end")

ID=0
def delete_reg():
    
    mi_db = mysql.connector.connect(host="localhost", user="root", passwd="")
    micursor = mi_db.cursor()
    micursor.execute("USE Nivel_Intermedio")
    item = tree.focus()
    print(tree.focus()) #id para el arbolm identificas el registro
    dic=tree.item(item)
    print(tree.item(item)) #los parametros del arbol
    print(dic['values']) #columnas del arbol
    j=dic['values']
    x=j[0]
    print(x)
    tree.delete(item)
    sql="DELETE FROM producto WHERE producto.id=%i" %x
    micursor.execute(sql)
    mi_db.commit()

	
    
def crear_entry (valor, ancho, fila, columna = 1):
    entrada= Entry(root, textvariable = valor , width=25)
    entrada.grid(padx=65, row=fila)
    return entrada
    
def create_db():
    try:
        mi_db= mysql.connector.connect(host="localhost", user="root", passwd="")
        micursor = mi_db.cursor()
        micursor.execute("CREATE DATABASE Nivel_Intermedio")
        mi_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="Nivel_Intermedio")
        micursor = mi_db.cursor()
        micursor.execute("CREATE TABLE producto(id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
        messagebox.showinfo(message="Base de Datos creada exitosamente", title="Alta de DB")
        
    except:
        print('La base de datos que intenta crear ya existe')
        messagebox.showerror(message="La BD ya existe", title="Error al crear la Base de Datos")
    

root = Tk()
root.title("Unidad 1 - Nivel Intermedio")
root.geometry('500x360')
cabecera=Label(root, text="Ingrese sus datos", font=('calibri', 12), background="violet" , foreground="white")
cabecera.grid(padx=0, pady=5, row=0, column=0, columnspan=6, sticky=W+S+N+E)

cabecera2= Label(root, text="Mostrar los registros existentes", background="lightgrey", foreground="black", width=50)
cabecera2.grid(row=3, column=0, columnspan=5, sticky=W+E)

bgcolours= ["orange", "blue", "wheat"]

id=0

title = Label(root, text="Título")
title.grid(padx=0, pady=0, row=1, column=0,sticky=W)
descrip = Label(root, text="Descripción")
descrip.grid( padx=0,pady=0, row=2, column=0,sticky=W)


val1, val2 = StringVar(), StringVar()

e1=crear_entry(val1, 25, 1)
e2=crear_entry(val2, 25, 2)


tree = ttk.Treeview(root, columns=(0,1,2), show="headings", height="5", selectmode ="browse")
tree.grid(column=0, row=7, columnspan=3)
tree.column(0, width=150, minwidth=150, stretch=YES)
tree.column(1, width=150, minwidth=150, stretch=YES)
tree.column(2, width=150, minwidth=150, stretch=YES)
tree.heading(0, text="ID")
tree.heading(1, text="Titulo")
tree.heading(2, text="Descripcion")

def obtener_reg():
    try:
        mi_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="Nivel_Intermedio")
        micursor = mi_db.cursor()
        sql = "SELECT * FROM producto"
        micursor.execute(sql)
        base = micursor.fetchall()
        tree.delete(*tree.get_children())
        for row in base:
            tree.insert("", "end", values=(row[0], row[1], row[2])) 
        return
    except:
        return None
    
obtener_reg() 

Button(root, text="Alta", width=4 , command = add_record).grid(row=1, column=2)
#Button(root, text="Sorpresa", width=12 , command = surprise).grid(padx=20, pady=0, row=4, column=2, columnspan=1, sticky=W)
Button(root, text="Crear BD", command=create_db).grid(row=8, column=0)
Button(root, text="Borrar", command=delete_reg).grid(row=2, column=2)
barra = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
barra.grid(row=4, column=3, rowspan=1, sticky=NSEW)
tree.configure(yscrollcommand=barra.set)
tree.grid(row=4, column=0, columnspan=3, rowspan=1, sticky=NSEW)




root.mainloop()


# In[ ]:




