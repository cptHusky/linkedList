import pytest
import importlib

module_name = '1LinkList'
module = importlib.import_module(module_name)
globals().update(vars(module))
