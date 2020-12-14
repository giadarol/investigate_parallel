from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([
        "myfunc.pyx",
        "myfuncpara.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp']),
)
