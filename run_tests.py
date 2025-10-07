import pytest
import sys

def main():
    """
    Main function to run the test suite for the TutorX application.
    This function uses pytest to discover and run all tests in the 'tests/' directory.
    """
    sys.exit(pytest.main(["tests/"]))

if __name__ == "__main__":
    main()