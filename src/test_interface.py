import platform
import pytest
import ecos
import numpy as np
import scipy.sparse as sp

# global data structures for problem
c = np.array([-1.])
h = np.array([4., -0.])
G = (sp.csc_matrix([1., -1.]).T).tocsc()
A = sp.csc_matrix([1.])
b = np.array([3.])
dims = {'q': [], 'l': 2}

def check_solution(solution, expected):
    np.testing.assert_almost_equal(solution, expected, decimal=5)

@pytest.mark.parametrize("inputs,expected", [
    ((c, G, h, dims, {'feastol': 2e-8, 'reltol': 2e-8, 'abstol': 2e-8, 'verbose': True}), 4),
    ((c, G, h, dims, A, b, {'feastol': 2e-8, 'reltol': 2e-8, 'abstol': 2e-8, 'verbose': True}), 3),
    ((c, G, h, {'q': [2], 'l': 0}, {'feastol': 2e-8, 'reltol': 2e-8, 'abstol': 2e-8, 'verbose': True}), 2)
])
def test_problems(inputs, expected):
    sol = ecos.solve(*inputs[:-1], **inputs[-1])
    check_solution(sol['x'][0], expected)

if platform.python_version_tuple() < ('3','0','0'):
    @pytest.mark.parametrize("new_dims,expected", [
        ({'q': [], 'l': 2}, 4),
        ({'q': [], 'l': 2}, 3),
        ({'q': [2], 'l': 0}, 2)
    ])
    def test_problems_with_longs(new_dims, expected):
        myopts = {'feastol': 2e-8, 'reltol': 2e-8, 'abstol': 2e-8}
        sol = ecos.solve(c, G, h, new_dims, **myopts)
        check_solution(sol['x'][0], expected)

@pytest.mark.parametrize("error_type,keyword,value", [
    (TypeError, 'verbose', 0),
    (ValueError, 'feastol', 0),
    (ValueError, 'abstol', 0),
    (ValueError, 'reltol', 0),
    (ValueError, 'feastol_inacc', 0),
    (ValueError, 'abstol_inacc', 0),
    (ValueError, 'reltol_inacc', 0),
    (ValueError, 'max_iters', -1),
    (TypeError, 'max_iters', 1.1),
])
def test_failures(error_type, keyword, value):
    with pytest.raises(error_type):
        ecos.solve(c, G, h, dims, **{keyword: value})
