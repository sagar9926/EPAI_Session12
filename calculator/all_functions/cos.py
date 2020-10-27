#cos.py

import math
from .f_string import f_string

__all__ = ['f_cos']



@f_string
def f_cos(arg : float) -> 'Cosine of input argument':
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Cosine of input argument

    """
    return(math.cos(arg))

@f_string
def f_dcos(arg : float) -> 'Derivative of Cosine of input argument' :
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Derivative of Cosine of input argument

    """

    return(-math.sin(arg))

