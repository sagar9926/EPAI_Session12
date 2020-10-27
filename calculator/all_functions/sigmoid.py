#sigmoid.py

import math
from .f_string import f_string

__all__ = ['f_sigmoid']



@f_string
def f_sigmoid(arg : float) -> 'Applies sigmoid on input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Applies sigmoid on input argument

    """
    return(1/(1 +math.exp(-1*arg)))

@f_string
def f_dsigmoid(arg) -> 'Derivative of Sigmoid of input argument':
    """
    Parameters
    ----------
    arg : float

    Returns
    -------
    Derivative of Sigmoid of input argument

    """
    sig = f_sigmoid(arg)
    return(sig*(1 - sig))
