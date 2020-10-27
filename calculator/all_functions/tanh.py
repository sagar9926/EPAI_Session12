#tanh.py

import math
from .f_string import f_string

__all__ = ['f_tanh']



@f_string
def f_tanh(arg : float) -> 'Hyperbolic Tangent of input argument':
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Hyperbolic Tangent of input argument

    """
    return(math.tanh(arg))

@f_string
def f_dtanh(arg : float) -> 'Derivative of Hyperbolic Tangent of input argument' :
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Derivative of Tangent of input argument

    """

    return(1 - (math.tanh(arg) ** 2))
