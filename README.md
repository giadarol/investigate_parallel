# investigate_parallel

## Dask

Dask could be an interesing option: https://docs.dask.org/en/latest/

## Context manager in pyhedtail

An (obsolete) example can be found here:

https://github.com/PyCOMPLETE/PyHEADTAIL-playground/blob/master/howto_notebooks/PyHEADTAIL_on_GPU_Tutorial.ipynb

One can get an idea of how it works directly from the [source of the context manager][https://github.com/PyCOMPLETE/PyHEADTAIL/blob/58028e2ec4c304f9b698de06926376e4793c0669/PyHEADTAIL/general/contextmanager.py#L142]

## nogil in cython

**Does not seem to be an option**

It seems that python code cannot be executed in a prange:

https://ipython-books.github.io/57-releasing-the-gil-to-take-advantage-of-multi-core-processors-with-cython-and-openmp/

some info on parallelism in cython:

https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html

some extra info:

https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html
