#sin.py

import math
from .f_string import f_string

__all__ = ['f_sin']



@f_string
def f_sin(arg : float) -> 'Sin of input argument':
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Sin of input argument

    """
    return(math.sin(arg))

@f_string
def f_dsin(arg : float) -> 'Derivative of Sin of input argument' :
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Derivative of Sin of input argument

    """

    return(math.cos(arg))
