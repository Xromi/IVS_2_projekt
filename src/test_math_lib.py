import ctypes
import sys
import os

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Error: Expecting one command line argument.")
        sys.exit()
    
    # Load the shared library into ctypes 
    lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), sys.argv[1]))
    try:
        c_lib = ctypes.CDLL(lib_path)
    except OSError:
        print("Unable to load library")
        sys.exit()
    
    # Testing
    print("Testing...")

    """
    # create named function pointers and set argument and return value types
    print_hello = c_lib.print_hello
    print_hello.argtypes = None
    print_hello.restype = None

    my_sqrt = c_lib.my_sqrt
    my_sqrt.argtypes = [ctypes.c_double]
    my_sqrt.restype = ctypes.c_double

    # call C functions
    print_hello()
    print(my_sqrt(14))
    """
