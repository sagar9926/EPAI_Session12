#softmax.py

import math
from .f_string import f_string

__all__ = ['f_softmax']



@f_string
def f_softmax(*args) -> 'Hyperbolic Tangent of input argument':
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Hyperbolic Tangent of input argument

    """
    print(args)
    softmax = lambda x : math.exp(x)/sum((math.exp(arg) for arg in args))
    result = [softmax(x) for x in args]
    return(result)

@f_string
def f_dsoftmax(*args : float) -> 'Derivative of Hyperbolic Tangent of input argument' :
    """
    Parameters
    ----------
    arg : Radian angle value in float

    Returns
    -------
    Derivative of Tangent of input argument

    """
    softmax = f_softmax(*args)
    d_softmax = [x*(1-x) for x in softmax]
    return(d_softmax)
