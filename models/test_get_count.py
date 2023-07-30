#!/usr/bin/python3
"""
Test for the get() and count() methods
"""
import unittest
from models import storage
from models.state import State

class TestGetCountMethods(unittest.TestCase):
    """
    Test cases for get() and count() methods
    """

    def setUp(self):
        """Set up the test environment"""
        storage.reload()

    def test_get(self):
        """
        Test the get() method.

        Create a new state, get it by its ID,
        and check if the retrieved state is the same as the original state.
        """
        # Create a new state
        new_state = State(name="California")
        new_state.save()

        # Get the state by its ID
        state_id = new_state.id
        state = storage.get(State, state_id)

        # Check if the retrieved state is the same as the original state
        self.assertEqual(state, new_state)

    def test_count(self):
        """
        Test the count() method.

        Count the number of states before adding a new state,
        create a new state, count the number of states after adding the new state,
        and check if the count increased by 1.
        """
        # Count the number of states before adding a new state
        count_before = storage.count(State)

        # Create a new state
        new_state = State(name="Florida")
        new_state.save()

        # Count the number of states after adding the new state
        count_after = storage.count(State)

        # Check if the count increased by 1
        self.assertEqual(count_after, count_before + 1)

if __name__ == '__main__':
    unittest.main()

