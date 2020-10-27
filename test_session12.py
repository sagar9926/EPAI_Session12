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
    assert len(readme_words) >= 100, "Say more in the README. please....."


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
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

def test_relu():
    assert calculator.f_relu(-100) == f'Result of function relu({-100}) = {max(0, -10)}'


def test_dsin():
    assert derivatives.f_dsin(math.pi/ 2) == f'Result of function dsin({math.pi/2}) = {math.cos(math.pi/2)}'


def test_dcos():
    assert derivatives.f_dcos(math.pi/ 2) == f'Result of function dcos({math.pi/2}) = {-math.sin(math.pi /2)}'


def test_dtan():
    assert derivatives.f_dtan(math.pi/ 4) == f'Result of function dtan({math.pi/4}) = {(1 + math.tan(math.pi / 4)**2)}'

def test_dtanh():
    assert derivatives.f_dtanh(math.pi/ 4) == f'Result of function dtanh({math.pi/4}) = {1-(math.tanh(math.pi / 4)**2)}'

  
def test_dlog():
    assert derivatives.f_dlog(1) == f'Result of function dlog({1}) = {1.0}'


def test_dexp():
    assert derivatives.f_dexp(10) == f'Result of function dexp({10}) = {math.exp(10)}'


def test_drelu():
    derivatives.f_drelu(-10) == f'Result of function drelu({-10}) = {0}'
    derivatives.f_drelu(10) == f'Result of function drelu({10}) = {1}'
   
