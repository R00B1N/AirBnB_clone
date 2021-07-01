#!/usr/bin/python3
"""
Unittest for state
"""


from models.state import State
import pep8
import os
import unittest


class TestState(unittest.TestCase):
    """
    Unittest for the class State
    """

    def test_docstring(self):
        """Checks for docstring"""
        self.assertTrue(len(State.__doc__) > 1)
        self.assertTrue(len(State.__init__.__doc__) > 1)
        self.assertTrue(len(State.__str__.__doc__) > 1)
        self.assertTrue(len(State.save.__doc__) > 1)
        self.assertTrue(len(State.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """
        Setup test
        """
        pass

    def test_init_arg(self):
        """pass in arg to new instance"""
        b1 = State(23)
        self.assertEqual(type(b1).__name__, "State")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        b1 = State(name="California")
        self.assertEqual(type(b1).__name__, "State")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        b1 = State()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[State] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_to_dict(self):
        """Tests instances before using to_dict conversion"""
        b1 = State()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "State")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.state.State'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_to_dict(self):
        """Test instances after using to_dict conversion"""
        my_model = State()
        new_model = State()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, State)
        self.assertEqual(type(my_model).__name__, "State")
        self.assertEqual(test_dict['__class__'], "State")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_has_attribute(self):
        """Tests if the instance of BaseModel has been correctly made"""
        b1 = State()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))


if __name__ == '__main__':
    unittest.main()
