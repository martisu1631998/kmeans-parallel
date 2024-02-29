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

class rgb(Structure):
    _fields_=[("b", c_uint8), ("g", c_uint8), ("r", c_uint8)]

class Image(Structure):
    _fields_=[("length", c_uint32),
               ("width", c_uint32),
               ("height", c_uint32),
               ("header", c_uint8*54),
               ("pixels", POINTER(rgb)),
               ("fp", c_void_p)] # c_void_p acts as a placeholder because c_types doesn't have an equivalent
    

# Functions of the implementation
def read_file(name, mImage): # name can be either type Python or C string ; mImage has to be of type Image
    name = name.encode('ascii')
    p_mImage = pointer(mImage)
    lib.read_file.restype = c_int #In theory, not necessary
    out = lib.read_file(name, p_mImage)
    return int(out) #Python or C datatype?

def write_file(name, mImage, centroids, k):
    name = name.encode('ascii')
    p_mImage = pointer(mImage)
    p_centroids = pointer(centroids)
    k = c_uint8(k)
    lib.write_file.restype = c_int
    out = int(lib.write_file(name, p_mImage, p_centroids, k))

def getChecksum(centroids, k):
    p_centroids = pointer(centroids)
    k = c_uint8(k)
    lib.getChecksum.restype = c_uint32
    sum = lib.getChecksum(p_centroids, k)
    return int(sum)

def find_closest_centroid(p, centroids, num_clusters): # Maybe we don't need it
    p_p = pointer(p)
    p_centroids = pointer(centroids)
    num_clusters = c_uint8(num_clusters)
    lib.find_closest_centroid.restype = c_uint8
    closest = lib.find_closest_centroid(p_p, p_centroids, num_clusters)
    return int(closest)

def kmeans(k, centroids, num_pixels, pixels):
    k = c_uint8(k)
    p_centroids = pointer(centroids)
    num_pixels = c_uint32(num_pixels)
    p_pixels = pointer(pixels)
    lib.kmeans(k, p_centroids, num_pixels, pixels)
