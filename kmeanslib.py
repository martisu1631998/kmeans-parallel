from ctypes import *

lib_path = '/home/alumnos/ppia/ppia-12/Escritorio/prac1/kmeanslib.so'
lib = CDLL(lib_path)

# Check that it's working
say_hello = lib.say_hello
say_hello(b"Martisu")

class Cluster(Structure): 
    _fields_=[("num_puntos", c_uint32),
              ("r", c_uint8),
              ("g", c_uint8),
              ("b", c_uint8),
              ("media_r", c_uint32),
              ("media_g", c_uint32),
              ("media_b", c_uint32)]
    
    