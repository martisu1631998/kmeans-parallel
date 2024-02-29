from ctypes import *

lib_path = '/home/alumnos/ppia/ppia-12/Escritorio/prac1/kmeanslib.so'
lib = CDLL(lib_path)

# Check that it's working
say_hello = lib.say_hello
say_hello(b"Martisu")

# Structure translations
class Cluster(Structure): 
    _fields_=[("num_puntos", c_uint32),
              ("r", c_uint8),
              ("g", c_uint8),
              ("b", c_uint8),
              ("media_r", c_uint32),
              ("media_g", c_uint32),
              ("media_b", c_uint32)]

class Pixel(Structure): # rgb
    _fields_=[("b", c_uint8), ("g", c_uint8), ("r", c_uint8)]

class Image(Structure):
    _fields_=[("length", c_uint32),
               ("width", c_uint32),
               ("height", c_uint32),
               ("header", c_uint8*54),
               ("pixels", POINTER(Pixel)),
               ("fp", c_void_p)] # c_void_p acts as a placeholder because c_types doesn't have an equivalent
    

