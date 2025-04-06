# python -m pytest ----> to run the pytest 

from calculator import add

import pytest

def test_add():
    assert add(2,3) == 5