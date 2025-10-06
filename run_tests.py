"""
TutorX-MCP Test Runner

This script discovers and runs all tests in the 'tests/' directory.
"""
import unittest
import os

def run_tests():
    """
    Discovers and runs all tests in the 'tests' directory.
    """
    # Define the directory where the tests are located
    test_dir = 'tests'

    # Discover all test cases in the specified directory
    loader = unittest.TestLoader()
    suite = loader.discover(test_dir)

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the test suite
    print(f"Running tests from '{os.path.abspath(test_dir)}'...")
    result = runner.run(suite)

    # Exit with a non-zero status code if any tests failed
    if not result.wasSuccessful():
        exit(1)

if __name__ == "__main__":
    run_tests()