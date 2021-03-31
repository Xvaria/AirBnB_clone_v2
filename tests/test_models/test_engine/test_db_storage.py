#!/usr/bin/python3
""" Module for testing DBstorage """
from unittest import TestCase, mock
import os

class test_DBStorage(TestCase):
    """  """
    @mock.patch.dict(os.environ, {
        "HBNB_ENV": "test",
        "HBNB_MYSQL_USER": "hbnb_test",
        "HBNB_MYSQL_PWD": "hbnb_test_pwd",
        "HBNB_MYSQL_HOST": "localhost",
        "HBNB_MYSQL_DB": "hbnb_test_db",
        "HBNB_TYPE_STORAGE": "db",
    })
    def test_00(self):
        pass
