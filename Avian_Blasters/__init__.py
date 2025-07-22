import logging


logging.basicConfig(level=logging.DEBUG)
<<<<<<< HEAD:my_project/__init__.py
logger = logging.getLogger('Avian-Blasters')

# this is the initial module of your app
# this is executed whenever some client-code is calling `import Avian-Blasters` or `from Avian-Blasters import ...`
=======
logger = logging.getLogger('Avian_Blasters')

# this is the initial module of your app
# this is executed whenever some client-code is calling `import Avian_Blasters` or `from Avian_Blasters import ...`
>>>>>>> main:Avian_Blasters/__init__.py
# put your main classes here, eg:
class MyClass:
    def my_method(self):
        return "Hello World"


# let this be the last line of this file
<<<<<<< HEAD:my_project/__init__.py
logger.info("Avian-Blasters loaded")
=======
logger.info("Avian_Blasters loaded")
>>>>>>> main:Avian_Blasters/__init__.py
