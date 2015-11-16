import webapp2
import __main__
import sure
import pasarelatest
#import unittest

class TestStringMethods():
        def test_listarempresas(self):
            # Build a request object passing the URI path to be tested.
            # You can also pass headers, query arguments etc.
            request = webapp2.Request.blank('/listarempresas')
            # Get a response for that request.
            response = request.get_response(pasarelatest.aplicacion())

            # Let's check if the response is correct.
            # self.assertEqual(response.status_int, 200)
            #self.assertTrue('<td>' in response.body)
            (response.body).should.contain('<td>')

        def test_calificarempresa(self):
            # Build a request object passing the URI path to be tested.
            # You can also pass headers, query arguments etc.
            request = webapp2.Request.blank('/calificarempresa')
            # Get a response for that request.
            response = request.get_response(pasarelatest.aplicacion())

            # Let's check if the response is correct.
            # self.assertEqual(response.status_int, 200)
            #self.assertTrue('<td>' in response.body)
            (response.body).should.contain('<select name=')
        def test_crearempresa(self):
            # Build a request object passing the URI path to be tested.
            # You can also pass headers, query arguments etc.
            request = webapp2.Request.blank('/crearempresa')
            # Get a response for that request.
            response = request.get_response(pasarelatest.aplicacion())

            # Let's check if the response is correct.
            # self.assertEqual(response.status_int, 200)
            #self.assertTrue('<input name="nombreEmpresa" type="text" placeholder="Nombre Empresa">' in response.body)
            (response.body).should.contain('<input name="nombreEmpresa" type="text" placeholder="Nombre Empresa">')
        def test_crearusuario(self):
            # Build a request object passing the URI path to be tested.
            # You can also pass headers, query arguments etc.
            request = webapp2.Request.blank('/crearusuario')
            # Get a response for that request.
            response = request.get_response(pasarelatest.aplicacion())

            # Let's check if the response is correct.
            # self.assertEqual(response.status_int, 200)
            #self.assertTrue('<input name="nombreUsuario" type="text" placeholder="Nombre Usuario">' in response.body)
            (response.body).should.contain('<input name="nombreUsuario" type="text" placeholder="Nombre Usuario">')
        def test_paginaprincipal(self):
            # Build a request object passing the URI path to be tested.
            # You can also pass headers, query arguments etc.
            request = webapp2.Request.blank('/')
            # Get a response for that request.
            response = request.get_response(pasarelatest.aplicacion())

            # Let's check if the response is correct.
            # self.assertEqual(response.status_int, 200)
            #self.assertTrue('<a class="uk-button-danger" href="crearempresa"> Crear Empresa </a>' in response.body)
            (response.body).should.contain('<a class="uk-button-danger" href="crearempresa"> Crear Empresa </a>')

        def test_prueba(self):
            # Build a request object passing the URI path to be tested.
            # You can also pass headers, query arguments etc.
            request = webapp2.Request.blank('/prueba')
            # Get a response for that request.
            response = request.get_response(pasarelatest.aplicacion())

            # Let's check if the response is correct.
            # self.assertEqual(response.status_int, 200)
            #self.assertTrue('<a class="uk-button-danger" href="crearempresa"> Crear Empresa </a>' in response.body)
            (response.body).should.contain('Parametro')

            def test_prueba(self):
                # Build a request object passing the URI path to be tested.
                # You can also pass headers, query arguments etc.
                request = webapp2.Request.blank('/prueba/valor_prueba')
                # Get a response for that request.
                response = request.get_response(pasarelatest.aplicacion())

                # Let's check if the response is correct.
                # self.assertEqual(response.status_int, 200)
                #self.assertTrue('<a class="uk-button-danger" href="crearempresa"> Crear Empresa </a>' in response.body)
                (response.body).should.contain('valor_prueba')
