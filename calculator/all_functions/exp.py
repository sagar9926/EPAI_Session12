#exp.py

import math
from .f_string import f_string

__all__ = ['f_exp']



@f_string
def f_exp(arg : float) -> 'Exponential of input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Exponential of input argument

    """
    return(math.exp(arg))

@f_string
def f_dexp(arg) -> 'Derivative of Exponential of input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Derivative of Exponential of input argument

    """

    return(math.exp(arg))
