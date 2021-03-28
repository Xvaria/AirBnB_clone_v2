#!/usr/bin/python3
"""This module tests console.py file.
Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_console.py"
"""

from console import HBNBCommand
import unittest
from unittest.mock import create_autospec, patch
import sys
from io import StringIO
import os
import pep8

classes = ["BaseModel", "User", "State", "City",
           "Amenity", "Place", "Review"]


class TestConsole(unittest.TestCase):
    ''' TestCase class for storing the unittests of the console. '''
    @classmethod
    def teardown(cls):
        ''' Removes the file.json on each test. '''
        try:
            os.remove("file.json")
        except:
            pass

    def setUp(self):
        ''' Sets up the mock stdin and stderr. '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create_session(self, server=None):
        ''' Creates the cmd session. '''
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_create(self):
        ''' Tests for the create command. '''
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('create'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
