# -*- coding: utf-8 -*-
import MySQLdb
from GestorUsuarios import GestorUsuarios
class GestorEmpresas:
#PRogramar funcion para añadir empresa
    @classmethod
    def registrarEmpresa(self, nombre, ciudad):
        base_datos = MySQLdb.connect(host="localhost", user="root", db="CALIFICACIONES_DB"); #La conexión está clara.
        consulta="INSERT INTO EMPRESAS (Nombre, Ciudad) values("+"'"+nombre+"', "+"'"+ciudad+"');"
        cursor = base_datos.cursor()
        cursor.execute(consulta);
        base_datos.commit()
        cursor.close()
        base_datos.close()

#Funcion para listar todas las empresas y calificaciones

    @classmethod
    def listarEmpresasCalificaciones(self):
        base_datos = MySQLdb.connect(host="localhost", user="root", db="CALIFICACIONES_DB"); #La conexión está clara.
        consulta = "SELECT Nombre,Ciudad from EMPRESAS;"
        cursor = base_datos.cursor()
        cursor.execute(consulta)
        respuesta=" <table border='1'>\n\t"
        respuesta=respuesta + " <tr> <td> Nombre de Empresa</td> <td> Ciudad de Empresa</td></tr>\n"
        for (Nombre, Ciudad) in cursor:
            respuesta = respuesta + "<tr>\n\t"
            respuesta = respuesta + "<td>"+ Nombre + "</td>\n"
            respuesta = respuesta + "<td>"+ Ciudad + "</td>\n"
            respuesta = respuesta + "</tr>\n"
        respuesta = respuesta + "</table>"
        cursor.close()
        base_datos.close()
        return respuesta

#Funcion que obtiene solo el nombre
    @classmethod
    def obtenerEmpresas(self):
        base_datos = MySQLdb.connect(host="localhost", user="root", db="CALIFICACIONES_DB");
        consulta = "SELECT Nombre, Codigo_empresa from EMPRESAS;"
        cursor = base_datos.cursor()
        cursor.execute(consulta)
        empresas = []
        for (Nombre,Codigo_empresa) in cursor:
            empresas.append({Nombre,Codigo_empresa})
        cursor.close()
        base_datos.close()
        print empresas
        return empresas
#Funcion para calificar una empresa
    @classmethod
    def calificarEmpresa(self, codigo_usuario, codigo_empresa, nota):
        #Abrimos conexion
        base_datos = MySQLdb.connect(host="localhost", user="root", db="CALIFICACIONES_DB");
        #Buscamos el ID de la empresa
        consulta = "INSERT INTO CALIFICA(codigo_usuario, codigo_empresa, Nota) VALUES (" + codigo_usuario + "," + codigo_empresa + "," + nota + ");"
        cursor = base_datos.cursor()
        cursor.execute(consulta)
        cursor.close()
        base_datos.close()
