# Created by : Sagar Agrawal
# EPAI Session 12 : Packages

## Problem statement 

### Build a calculator package that has separate module for:

* sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e

* The modules shall include their derivatives as well

* If we do import calculator, we should be able to access all the above function (except deviratives)

* For derivates we must do: from package import derivatives. 

* Outputs are returned as well as printed using only f-string

* Write simple test cases to check the outputs of each operator and their derivative

## Modules overview : 

cos: This function returns cosine and derivative of the same, of the input number. The input is assumed to be in radians.

exp: This function returns exponential and derivative of the same, of the input number.

log: This function returns logarithm and derivative of the same, of the input number. If base is not provided, it would return log on base e.

relu: This function returns ReLU activation function and derivative of the same, output of the input number.

sigmoid: This function returns sigmoid activation function and derivative of the same, output of the input number.

sin: This function returns sine of the input number and derivative of the same. The input is assumed to be in radians.

softmax: This function returns softmax activation function and derivative of the same, output of the input array.

tan: This function returns tangent of the input number and derivative of the same. The input is assumed to be in radians.

tanh: This function returns hyperbolic tangent of the input number and derivative of the same. The input is assumed to be in radians.
