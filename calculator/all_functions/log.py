#log.py

import math
from .f_string import f_string

__all__ = ['f_log']



@f_string
def f_log(arg : float) -> 'logarithm of input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    logarithm of input argument

    """
    return(math.log(arg))

@f_string
def f_dlog(arg) -> 'Derivative of logarithm of input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Derivative of logarithm of input argument

    """

    return(1/arg)
