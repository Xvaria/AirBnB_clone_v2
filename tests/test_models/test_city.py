#!/usr/bin/python3
""" test description for function """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ test description for function """

    def __init__(self, *args, **kwargs):
        """ test description for function """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    # def test_state_id(self):
    #     """ test description for function """
    #     new = self.value()
    #     print(new)
    #     self.assertEqual(type(new.state_id), str)

    # def test_name(self):
    #     """ test description for function """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)

if __name__ == "__main__":
    unittest.main()
