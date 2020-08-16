#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector
import sys


def add(arg1, arg2 , connect):
#Guardar los registros en una base de datos del tipo MySQL mediante una función que se encuentre en un módulo aparte
        micursor = connect.cursor()
        sql = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
        datos = (arg1, arg2)
        micursor.execute(sql, datos)
        connect.commit()
        count=micursor.rowcount
        return count
