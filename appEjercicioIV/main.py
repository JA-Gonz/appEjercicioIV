# -*- coding: utf-8 -*-

import datetime
import jinja2
import os
import webapp2
import cgi
from GestorEmpresas import GestorEmpresas
from GestorUsuarios import GestorUsuarios
import re

plantilla_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))



#Ventana principal: tendrá 4 botones para acceder a las distintas opciones
class PaginaPrincipal (webapp2.RequestHandler):

	def get(self):
		plantilla=plantilla_env.get_template('plantilla/paginaprincipal.html')
		self.response.out.write(plantilla.render())
#Pagina de Crear empresa. Tendrá un campo de texto para el nombre de la empresa y un botón de enviar. La empresa quedará grabada.
class PaginaCrearEmpresa (webapp2.RequestHandler):
    def get(self):

        plantilla=plantilla_env.get_template('plantilla/crearempresa.html')
        self.response.out.write(plantilla.render())


    def post(self):

        if not(self.request.get('nombreEmpresa') and self.request.get('ciudadEmpresa')):
            plantilla=plantilla_env.get_template('plantilla/crearempresa.html')
            self.response.out.write(plantilla.render())
        else:
            #Grabamos los datos en la base de datos.
            GestorEmpresas.registrarEmpresa(self.request.get('nombreEmpresa'), self.request.get('ciudadEmpresa'))
            plantilla=plantilla_env.get_template('plantilla/paginaprincipal.html')
            self.response.out.write(plantilla.render())

#Listar calificaciones. Listará el nombre de empresas y las calificaciones que ha tenido.
class PaginaListarCalificaciones(webapp2.RequestHandler):

        def get(self):
            respuesta = GestorEmpresas.listarEmpresasCalificaciones()
            templateVars = {"empresas" : respuesta}
            plantilla=plantilla_env.get_template('plantilla/listarempresas.html')

            self.response.out.write(plantilla.render(templateVars))


#Crear un usuario
class PaginaCrearUsuario(webapp2.RequestHandler):

        def get(self):
            plantilla=plantilla_env.get_template('plantilla/crearusuario.html')
            self.response.out.write(plantilla.render())

        def post(self):

            if not(self.request.get('nombreUsuario') and self.request.get('ciudadUsuario')):
                    plantilla=plantilla_env.get_template('plantilla/crearusuario.html')
                    self.response.out.write(plantilla.render())
            else:
                    #Grabamos los datos en la base de datos.
                    GestorUsuarios.registrarUsuario(self.request.get('nombreUsuario'), self.request.get('ciudadUsuario'))
                    plantilla=plantilla_env.get_template('plantilla/paginaprincipal.html')
                    self.response.out.write(plantilla.render())

#Crear calificacion. Será una pagina con un desplegable con todas las empresas guardadas, otro desplegable de 1 a 10 para la nota, y
# un campo de texto para introudicr el nombre de usuario (no se manejarán sesiones).
class PaginaCalificarEmpresa(webapp2.RequestHandler):

    def get(self):
        usuarios = GestorUsuarios.obtenerUsuarios()
        patron = '[a-zA-Z0-9]'
        respuesta = "<select name='seleccion_usuario'>\n"
        for (codigo_usuario, usuario) in usuarios:
            respuesta = respuesta + "<option value=" + str(codigo_usuario) + ">" + ''.join(re.findall(patron, str(usuario))) + "</option>\n"
        respuesta = respuesta + "</select>\n"

        empresas =  GestorEmpresas.obtenerEmpresas()
        respuesta = respuesta + "<select name='seleccion_empresa'>\n"
        for codigo_empresa, empresa in empresas:
            respuesta = respuesta + "<option value=" + str(codigo_empresa) + ">" + ''.join(re.findall(patron, str(empresa))) + "</option>\n"
        respuesta = respuesta + "</select>\n"

        templateVars = {"listas": respuesta}
        plantilla = plantilla_env.get_template('plantilla/calificarempresa.html')
        self.response.out.write(plantilla.render(templateVars))

    def post(self):
        if not(self.request.get('seleccion_usuario'), self.request.get('seleccion_empresa'),self.request.get('seleccion_nota') ):
            usuarios = GestorUsuarios.obtenerUsuarios()
            patron = '[a-zA-Z0-9]'
            respuesta = "<select>\n"
            for usuario in usuarios:
                respuesta = respuesta + "<option value=" + ''.join(re.findall(patron, str(usuario))) + ">" + ''.join(re.findall(patron, str(usuario))) + "</option>\n"
                respuesta = respuesta + "</select>\n"

            empresas =  GestorEmpresas.obtenerEmpresas()
            respuesta = respuesta + "<select>\n"
            for empresa in empresas:
                respuesta = respuesta + "<option value=" + ''.join(re.findall(patron, str(empresa)))  + ">" + ''.join(re.findall(patron, str(empresa))) + "</option>\n"
            respuesta = respuesta + "</select>\n"
            templateVars = {"listas": respuesta}
            plantilla = plantilla_env.get_template('plantilla/calificarempresa.html')
            self.response.out.write(plantilla.render(templateVars))
        else:
            #Grabamos los datos en la base de datos.
            print self.request.get('seleccion_usuario')
            print self.request.get('seleccion_nota')
            print self.request.get('seleccion_empresa')
            GestorEmpresas.calificarEmpresa(self.request.get('seleccion_usuario'), self.request.get('seleccion_empresa'),self.request.get('seleccion_nota'))
            plantilla=plantilla_env.get_template('plantilla/paginaprincipal.html')
            self.response.out.write(plantilla.render())


#Borrar una calificación. Lo mismo que la de Crear calificacion, pero con solo dos desplegables.
class PaginaBorrarCalificacion(webapp2.RequestHandler):
    def get(self):
        respuesta = GestorEmpresas.obtenerEmpresasCalificar()
        templateVars = {"formBorrar" : respuesta}
        plantilla=plantilla_env.get_template('plantilla/borrarEmpresa.html')
        self.response.out.write(plantilla.render(templateVars))

    def post(self):
        if not(self.request.get('nombreUsuario'), self.request.get('nombreEmpresa')):
            respuesta = GestorEmpresas.obtenerEmpresasCalificar()
            templateVars = {"formBorrar" : respuesta}
            plantilla=plantilla_env.get_template('plantilla/borrarEmpresa.html')
            self.response.out.write(plantilla.render(templateVars))
        else:
            #Grabamos los datos en la base de datos.
            GestorEmpresas.borrarCalificacion(self.request.get('nombreEmpresa'),self.request.get('nombreUsuario'))
            plantilla=plantilla_env.get_template('plantilla/paginaprincipal.html')
            self.response.out.write(plantilla.render())

# Ranking de empresa. Las empresas serán ordenadas de mayor a menor, haciendo una media de todas sus calificaciones.



class PaginaPruebaVariable(webapp2.RequestHandler):
    def get(self,parametro):
        self.response.write( 'Parametro recibido: %s' % parametro)

class PaginaModificacion(webapp2.RequestHandler):
    def get(self):
        self.response.write('Modificacion para CI')

aplicacion = webapp2.WSGIApplication([
                                      ('/',PaginaPrincipal),
                                      ('/crearempresa',PaginaCrearEmpresa),
                                      ('/listarempresas', PaginaListarCalificaciones),
                                      ('/calificarempresa', PaginaCalificarEmpresa),
                                      ('/crearusuario',PaginaCrearUsuario),
                                      (r'/prueba/(\w*)', PaginaPruebaVariable),
                                      ('/modificacion',PaginaModificacion)
					], debug=True)




def main():
    from paste import httpserver
    httpserver.serve(aplicacion, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
