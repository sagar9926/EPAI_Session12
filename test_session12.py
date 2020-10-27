import inspect
import math
import os
import re

import pytest

import calculator
from calculator import derivatives

def test_readme_exists():
    assert os.path.isfile("README.md"), "Put a README file, man!!"


def test_readme_contents():
    readme_words = [word for line in open("README.md", "r") for word in line]
    assert len(readme_words) >= 500, "Say more in the README. please....."


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.rea_d()
    f.close()
    assert content.count("#") >= 10

def test_sin():

    assert calculator.f_sin(math.pi/ 2) == f'Result of function sin({math.pi/2}) = {math.sin(math.pi/2)}'


def test_cos():
    assert calculator.f_cos(math.pi/ 2) == f'Result of function cos({math.pi/2}) = {math.cos(math.pi /2)}'


def test_tan():
    assert calculator.f_tan(math.pi/ 4) == f'Result of function tan({math.pi/4}) = {math.tan(math.pi / 4)}'

 

def test_tanh():
    assert calculator.f_tanh(math.pi/ 4) == f'Result of function tanh({math.pi/4}) = {math.tanh(math.pi / 4)}'

def test_log():
    assert calculator.f_log(1) == f'Result of function log({1}) = {math.log(1)}'


def test_exp():
    assert calculator.f_exp(1) == f'Result of function exp({1}) = {math.exp(1)}'


def test_sigmoid():
    assert calculator.f_sigmoid(2) == f'Result of function sigmoid({2}) = {1 / (1 + math.exp(-2))}'
"""

def test_relu():
    assert max(0, -10) == calculator.relu(-10)


def test_sin_d():

    assert math.cos(3.14 // 2) == derivatives.sin_d(3.14 // 2)


def test_cos_d():
    assert -math.sin(3.14 // 2) == derivatives.cos_d(3.14 // 2)


def test_tan_d():
    assert 1-math.tan(3.14 // 2)**2 == derivatives.tan_d(3.14 // 2)


def test_tanh_d():
    assert 1-(math.tanh(3.14 // 2)**2) == derivatives.tanh_d(3.14 // 2)


def test_log_d():
    assert 1 == derivatives.log_d(1)


def test_exp_d():
    assert math.exp(10) == derivatives.exp_d(10)


def test_sigmoid_d():
    x=10
    assert calculator.sigmoid(x)*(1-calculator.sigmoid(x)) == derivatives.sigmoid_d(x)


def test_relu_d():
    assert 0 == derivatives.relu_d(-10)
    assert 1 == derivatives.relu_d(10000)

"""
