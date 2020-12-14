import numpy as np
from math import sin, cos
import numba


def generate_particles(N_part):
    x = np.random.randn(N_part)
    xp = np.random.randn(N_part)
    return x, xp


def rotate_particles(x, xp):

    N_part = len(x)

    for ii in range(N_part):
        
        theta = np.pi/3. + 0.01*x[ii]
        costh = cos(theta)
        sinth = sin(theta)
        
        x_new = x[ii]*costh + xp[ii]*sinth
        xp_new = -xp[ii]*sinth + x[ii]*costh

        x[ii] = x_new
        xp[ii] = xp_new

@numba.njit
def rotate_numba(x, xp):

    N_part = len(x)

    for ii in range(N_part):
        
        theta = np.pi/3. + 0.01*x[ii]
        costh = cos(theta)
        sinth = sin(theta)
        
        x_new = x[ii]*costh + xp[ii]*sinth
        xp_new = -xp[ii]*sinth + x[ii]*costh

        x[ii] = x_new
        xp[ii] = xp_new

def rotate_particles_vect(x, xp):
    
    theta = np.pi/3. + 0.01*x
    costh = np.cos(theta)
    sinth = np.sin(theta)
    
    x_new = x*costh + xp*sinth
    xp_new = -xp*sinth + x*costh

    x[:] = x_new
    xp[:] = xp_new
    
    
import myfunc as rc
import myfuncpara as rcp
import rotate_fortran as rf

N_part = 10000000
x, xp = generate_particles(N_part)
#@profile
def doit():
    rotate_particles(x, xp)

def doit_vect():
    rotate_particles_vect(x, xp)
    
def doit_cython():
    rc.rotate_particles(x, xp)
    
def doit_cython_opt():
    rc.rotate_particles_opt(x, xp)

def doit_cython_para():
    rcp.rotate_particles_par(x, xp)

def doit_fortran():
    rf.rotate_fortran(x, xp)

def doit_numba():
    rotate_numba(x, xp)



import timeit

#exectime = timeit.timeit(stmt = 'doit()',  setup = 'from __main__ import doit', number=2)
#print('Exec. time: %.2f s'%exectime)
#
exectime = timeit.timeit(stmt = 'doit_vect()',  setup = 'from __main__ import doit_vect', number=2)
print('Exec. time vect: %.2f s'%exectime)

#exectime = timeit.timeit(stmt = 'doit_cython()',  setup = 'from __main__ import doit_cython', number=2)
#print('Exec. time cython: %.2f s'%exectime)

exectime = timeit.timeit(stmt = 'doit_cython_opt()',  setup = 'from __main__ import doit_cython_opt', number=2)
print('Exec. time cython opt: %.2f s'%exectime)

exectime = timeit.timeit(stmt = 'doit_cython_para()',  setup = 'from __main__ import doit_cython_para', number=2)
print('Exec. time cython para: %.2f s'%exectime)

exectime = timeit.timeit(stmt = 'doit_fortran()',  setup = 'from __main__ import doit_fortran', number=2)
print('Exec. fortran: %.2f s'%exectime)

exectime = timeit.timeit(stmt = 'doit_numba()',  setup = 'from __main__ import doit_numba', number=2)
print('Exec. numba: %.2f s'%exectime)

# to profile:
# kernprof --view -l 000_profile_example.py



