import os
import sys
import pytest

import numpy as np
from h5py import File

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))
import h5nav.cli as cli


def setup_module():
    """Create dummy hdf5 file to navigate"""
    with File("dummy.h5", 'w') as dum:
        dum.create_group("Group1")
        dum.create_group(" Group2")
        dum["Group1"].create_group("Subgroup1")
        dum["Group1/field1"] = "information"
        dum[" Group2"]["field1"] = np.zeros(10)
        dum["Group1/Subgroup1/field1"] = np.arange(100)
        dum["Group1/Subgroup1/ field2"] = 2 * np.arange(100)


def teardown_module():
    """Destroy dummy hdf5 file"""
    os.remove("dummy.h5")


@pytest.fixture(scope="function")
def interp():
    interpreter = cli.H5NavCmd()
    interpreter.do_open("dummy.h5")
    return interpreter
