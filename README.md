# investigate_parallel

## Context manager in pyhedtail

An (obsolete) example can be found here:

https://github.com/PyCOMPLETE/PyHEADTAIL-playground/blob/master/howto_notebooks/PyHEADTAIL_on_GPU_Tutorial.ipynb

## nogil in cython

**Does not seem to be an option**

It seems that python code cannot be executed in a prange:

https://ipython-books.github.io/57-releasing-the-gil-to-take-advantage-of-multi-core-processors-with-cython-and-openmp/

some info on parallelism in cython:

https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html

some extra info:

https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html
