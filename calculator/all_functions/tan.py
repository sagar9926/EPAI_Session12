#tan.py

import math
from .f_string import f_string

__all__ = ['f_tan']



@f_string
def f_tan(arg : float) -> 'Tangent of input argument':
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Tangent of input argument

    """
    return(math.tan(arg))

@f_string
def f_dtan(arg : float) -> 'Derivative of Tangent of input argument' :
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Derivative of Tangent of input argument

    """

    return(1 + math.tan(arg)**2)
