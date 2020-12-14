
from math import sin, cos, pi
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

	N_part = len(x)
	cdef double theta, sinth, costh

	for ii in range(N_part):
		
		theta = pi/3. + 0.01*x[ii]
		costh = cos(theta)
		sinth = sin(theta)
		
		x_new = x[ii]*costh + xp[ii]*sinth
		xp_new = -xp[ii]*sinth + x[ii]*costh

		x[ii] = x_new
		xp[ii] = xp_new

