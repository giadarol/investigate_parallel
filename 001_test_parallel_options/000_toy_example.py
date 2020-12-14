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

@numba.njit(parallel=True)
def rotate_numba_para(x, xp):

    N_part = len(x)

    for ii in numba.prange(N_part):

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
    
@numba.njit(parallel=True)
def rotate_particles_vect_numba(x, xp):

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

tests = [
    {'name': 'python_naive', 'function': rotate_particles},
    {'name': 'python_np_vect', 'function': rotate_particles_vect},
    {'name': 'cython_naive', 'function': rc.rotate_particles},
    {'name': 'cython_optimized', 'function': rc.rotate_particles_opt},
    {'name': 'fortran_f2py', 'function': rf.rotate_fortran},
    {'name': 'numba_ser_loop', 'function': rotate_numba},
    {'name': 'cython_paral', 'function': rcp.rotate_particles_par},
    {'name': 'numba_par_loop', 'function': rotate_numba_para},
    {'name': 'numba_par_vect', 'function': rotate_particles_vect_numba},
    ]

N_part = 10000000
x, xp = generate_particles(N_part)
import timeit

for tt in tests:
    name = tt['name']
    fun = tt['function']
    def thistest():
        fun(x,xp)
    exectime = timeit.timeit(
            stmt = 'thistest()',
            setup = 'from __main__ import thistest', number=2)

    print(f'Exec. time {name}:\t {exectime:.2f} s')

