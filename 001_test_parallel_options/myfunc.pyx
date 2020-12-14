
#from math import sin, cos, pi
cdef extern from "math.h" nogil:
		double sin(double x)
		double cos(double x)
from math import pi

def rotate_particles(x, xp):

	N_part = len(x)

	for ii in range(N_part):
		
		theta = pi/3. + 0.01*x[ii]
		costh = cos(theta)
		sinth = sin(theta)
		
		x_new = x[ii]*costh + xp[ii]*sinth
		xp_new = -xp[ii]*sinth + x[ii]*costh

		x[ii] = x_new
		xp[ii] = xp_new

def rotate_particles_opt(double[:] x, double[:] xp):

	cdef int N_part = len(x)
	cdef int ii
	cdef double theta, sinth, costh
	cdef double x_new, xp_new
	cdef double cpi = pi

	for ii in range(N_part):
		
		theta = cpi/3. + 0.01*x[ii]
		costh = cos(theta)
		sinth = sin(theta)
		
		x_new = x[ii]*costh + xp[ii]*sinth
		xp_new = -xp[ii]*sinth + x[ii]*costh

		x[ii] = x_new
		xp[ii] = xp_new

