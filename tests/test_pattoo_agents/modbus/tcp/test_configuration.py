#!/usr/bin/env python3
"""Test the class_oid module."""

import sys
import unittest
import os

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(
            os.path.abspath(os.path.join(
                os.path.abspath(os.path.join(
                        EXEC_DIR,
                        os.pardir)), os.pardir)), os.pardir)), os.pardir))

if EXEC_DIR.endswith(
        '/pattoo-agents/tests/test_pattoo_agents/modbus/tcp') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the \
"pattoo-agents/tests/test_pattoo_agents/modbus/tcp" directory. Please fix.''')
    sys.exit(2)

# Pattoo imports
from pattoo_agents.agents.modbus.tcp import configuration
from pattoo_agents.agents.modbus.variables import (
    InputRegisterVariable, HoldingRegisterVariable, RegisterVariable,
    DeviceRegisterVariables)
from tests.libraries.configuration import UnittestConfig


class TestConfigModbusTCP(unittest.TestCase):
    """Checks all ConfigModbusTCP methods."""

    ##########################################################################
    # Initialize variable class
    ##########################################################################
    config = configuration.ConfigModbusTCP()

    def test___init__(self):
        """Testing function __init__."""
        pass

    def test_registervariables(self):
        """Testing method / function registervariables."""
        # Initialize variables
        expected_ip_device = 'unittest.modbus.tcp.device.net'
        register_variables = []

        # Test
        result = self.config.registervariables()
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 2)
        for drv in result:
            self.assertTrue(isinstance(drv, DeviceRegisterVariables))
            self.assertTrue(drv.active)
            self.assertEqual(drv.device, expected_ip_device)
            for _rv in drv.data:
                self.assertTrue(isinstance(_rv, RegisterVariable))
                self.assertTrue(_rv.active)
            register_variables.extend(drv.data)

        # Evaluate each RegisterVariable
        self.assertEqual(len(register_variables), 4)
        for index, _rv in enumerate(register_variables):
            if index == 0:
                self.assertEqual(_rv.address, 387)
                self.assertEqual(_rv.count, 1)
                self.assertEqual(_rv.unit, None)
                self.assertTrue(isinstance(_rv, InputRegisterVariable))
            elif index == 1:
                self.assertEqual(_rv.address, 388)
                self.assertEqual(_rv.count, 1)
                self.assertEqual(_rv.unit, None)
                self.assertTrue(isinstance(_rv, InputRegisterVariable))
            elif index == 2:
                self.assertEqual(_rv.address, 123)
                self.assertEqual(_rv.count, 1)
                self.assertEqual(_rv.unit, None)
                self.assertTrue(isinstance(_rv, HoldingRegisterVariable))
            else:
                self.assertEqual(_rv.address, 456)
                self.assertEqual(_rv.count, 1)
                self.assertEqual(_rv.unit, None)
                self.assertTrue(isinstance(_rv, HoldingRegisterVariable))

    def test__create_drv(self):
        """Testing method / function _create_drv."""
        # Tested by test_registervariables
        pass


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
