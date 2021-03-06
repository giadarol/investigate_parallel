from math import pi

cimport cython

from cython.parallel import prange
cdef extern from "math.h" nogil:
		double sin(double x)
		double cos(double x)

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def rotate_particles_par(double[:] x, double[:] xp):

	cdef int N_part = len(x)
	cdef int ii
	cdef double theta, sinth, costh
	cdef double x_new, xp_new
	cdef double cpi = pi

	#for ii in prange(N_part, nogil=True):
	for ii in prange(N_part, nogil=True, num_threads=4):
	#for ii in range(N_part):
		
		theta = cpi/3. + 0.01*x[ii]
		costh = cos(theta)
		sinth = sin(theta)
		
		x_new = x[ii]*costh + xp[ii]*sinth
		xp_new = -xp[ii]*sinth + x[ii]*costh

		x[ii] = x_new
		xp[ii] = xp_new
