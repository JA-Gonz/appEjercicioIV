# -*- coding: utf-8 -*-
import MySQLdb
#from GestorEmpresas import GestorEmpresas
class GestorUsuarios:

    # Metodo para registrar usuario
    @classmethod
    def registrarUsuario(self, nombre, ciudad):
        base_datos = MySQLdb.connect(host="localhost", user="root", db="CALIFICACIONES_DB"); #La conexión está clara.
        consulta="INSERT INTO USUARIOS (Nombre, Ciudad) values("+"'"+nombre+"', "+"'"+ciudad+"');"
        cursor = base_datos.cursor()
        cursor.execute(consulta);
        base_datos.commit()
        cursor.close()
        base_datos.close()

    # Método para listar todos los usuarios
    @classmethod
    def obtenerUsuarios(self):
        base_datos = MySQLdb.connect(host="localhost", user="root", db="CALIFICACIONES_DB");
        consulta = "SELECT Codigo_usuario, NOMBRE from USUARIOS;"
        cursor = base_datos.cursor()
        cursor.execute(consulta)
        usuarios = []
        for Codigo_usuario, Nombre in cursor:
            usuarios.append({Codigo_usuario,Nombre})
        cursor.close()
        base_datos.close()
        print usuarios
        return usuarios
