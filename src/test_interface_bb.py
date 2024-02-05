import ecos
import numpy as np
import scipy.sparse as sp

c = np.array([-1., -1.])
h = np.array([ 4., 12., 0., 0.])
bool_idx = [1]
G = sp.csc_matrix((
    np.array([2.0, 3.0, -1.0, 1.0, 4.0, -1.0]),
	np.array([0, 1, 2, 0, 1, 3]),
	np.array([0, 3, 6]),
))

dims = dict()
dims['l'] = 4

sol = ecos.solve(c, G, h, dims, verbose=False, mi_verbose=False, int_vars_idx=bool_idx)

c = np.array([-1., -1.])
h = np.array([ 4., 12., 0., 0.])
bool_idx = []
G = sp.csc_matrix((
    np.array([2.0, 3.0, -1.0, 1.0, 4.0, -1.0]),
	np.array([0, 1, 2, 0, 1, 3]),
	np.array([0, 3, 6]),
))

dims = dict()
dims['l'] = 4

sol = ecos.solve(c, G, h, dims, verbose=False, mi_verbose=False, int_vars_idx=bool_idx)

c = np.array([-1., -1.1])
h = np.array([ 4., 12., 0., 0.])
bool_idx = [1,0]
G = sp.csc_matrix((
    np.array([2.0, 3.0, -1.0, 1.0, 4.0, -1.0]),
	np.array([0, 1, 2, 0, 1, 3]),
	np.array([0, 3, 6]),
))

dims = dict()
dims['l'] = 4

sol = ecos.solve(c, G, h, dims, verbose=False, mi_verbose=False, int_vars_idx=bool_idx)


c = np.array([-1., -1.5])
h = np.array([ 4., 12., 0. , 0.])
bool_idx = [1]
G = sp.csc_matrix((
    np.array([2.0, 3.0, -1.0, 1.0, 4.0, -1.0]),
    np.array([0, 1, 2, 0, 1, 3]),
    np.array([0, 3, 6]),
))

dims = dict()
dims['l'] = 4

sol = ecos.solve(c, G, h, dims, verbose=False, mi_verbose=True, bool_vars_idx=bool_idx)