import pytest

# This file can be used for utility functions that are shared across multiple tests.
# For example, you might have helper functions to create mock data, set up a
# test environment, or connect to a test database.

def setup_test_environment():
    """
    An example of a setup function that could be used in a fixture.
    """
    return {"status": "ready"}

def test_utility_functions():
    """
    A simple test to ensure the utility functions in this file are working.
    """
    env = setup_test_environment()
    assert env["status"] == "ready"