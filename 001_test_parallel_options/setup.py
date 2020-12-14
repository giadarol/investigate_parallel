from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([
        Extension('myfuncpara',
            ["myfuncpara.pyx"],
            extra_compile_args=['-fopenmp'],
            extra_link_args=['-fopenmp']),
        Extension('myfunc',
            ["myfunc.pyx"])
        ]),
)
