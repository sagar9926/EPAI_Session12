#relu.py

import math
from .f_string import f_string

__all__ = ['f_relu']



@f_string
def f_relu(arg : float) -> 'Applies RELU on input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Applies RELU on input argument

    """
    return(max(0,arg))

@f_string
def f_drelu(arg) -> 'Derivative of RELU of input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Derivative of RELU of input argument

    """

    return(1 if arg > 0  else 0)

