from setuptools import setup

setup(name='appEjercicioIV',
      version='0.1',
      description='Una aplicacion web de prueba para calificar empresas',
      url='https://github.com/JA-Gonz/appEjercicioIV',
      author='JA-Gonz',
      author_email='jagoncccc@gmail.com',
      license='MIT',
      packages=['appEjercicioIV'],
      install_requires=[
          'mysql-python',
          'jinja2',
          'webapp2',
          'Paste',
          'webob'
      ],
      zip_safe=False)
