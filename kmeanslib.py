from ctypes import *
lib_path = '/home/alumnos/ppia/ppia-12/Escritorio/prac1/kmeanslib.so'
lib = CDLL(lib_path)

# Check that it's working
say_hello = lib.say_hello
say_hello(b"Martisu")

class cluster(): #??
    pass