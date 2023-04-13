import pytest
import importlib
import .1LinkList

module_name = '1LinkList'
module = importlib.import_module(module_name)
globals().update(vars(module))

a = GreatLinkedList
b = GreatLinkedList

def test_scenario()