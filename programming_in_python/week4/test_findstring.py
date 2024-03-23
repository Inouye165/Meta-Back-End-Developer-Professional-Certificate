from curses.ascii import isdigit
import imp
import pytest
import find_string

def test_ispresent():
    assert find_string.ispresent("Al")
    
def test_nodigit():
    find_string.nodigit("N7")