# -*- coding: utf-8 -*-
import jsonpickle

class Libro(object):
    nombre=""
    numero_paginas=0
    url=""
    def __init__(self, nombre,np,link):
        self.nombre =nombre
        self.numero_paginas=np
        self.url=link


class Prueba(object):
    vector_clase={}
    def __init__(self, vector):
        self.vector_clase = vector
    @classmethod
    def get(self):
        lista = (1,2,3)
        lista2 = (4,4,4)
        devolver = [lista, lista2]
        return devolver


class ObjetoJSON(object):
    #p = Prueba()
    #sl = Libro()

    def __init__(self, prueba,libro):
        self.p = Prueba(prueba.vector_clase)
        self.l = Libro(libro.nombre,libro.numero_paginas,libro.url)


class JSON(object):
    @classmethod
    def guardar(self):
        archivo = open('json.json','w')
        objeto_prueba = Prueba((1,2,3,4))
        objeto_libro = Libro('Nombre del libro',500,'www.get.com')
        objeto_json = ObjetoJSON(objeto_prueba,objeto_libro)
        #json_obj = jsonpickle.encode(Prueba.get())
        json_obj = jsonpickle.encode(objeto_json)
        # LA opcion unpicklable=False hace que en el JSON no aparezca py/object como nombre de atributo
        archivo.write(json_obj)
        #libro = {}
        #libro['pagina1'] = 'Esta es la pag 1'
        #libro ['DOcumentacion'] = 'Documentacion'
        #libro ['ALLA VA UN VECTOR'] = [2,3,3,1,5,9.0]
        #libro_json = jsonpickle.encode(libro, keys = True)
        #archivo.write(libro_json)
        archivo.close()

        print "GUARDADO"
        objeto = jsonpickle.decode(json_obj)
        print objeto.p.vector_clase

    @classmethod
    def leer(self):
        archivo = open('json.json','rb')
        objetos_json = archivo.read()
        #objetos_json.replace( '\x00', '' )
        #leer = repr(objetos_json)
        #print leer
        objeto = jsonpickle.decode(objetos_json)
        print objeto
        l = objeto.l
        print objeto.l.nombre
        archivo.close()


def main():
    JSON.guardar()
    JSON.leer()

if __name__ == '__main__':
    main()
