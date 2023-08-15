import unittest

# Import your test modules
from test.test_car import TestCalliope, TestGlissade, TestPalindrome, TestRorschach, TestThovex, TestCapuletEngine, TestSternmanEngine, TestWilloughbyEngine, TestSpindlerBattery, TestNubbinBattery, TestCarriganTire, TestOctoprimeTire
# Add similar imports for other test modules

def run_tests():
    # Create a test suite by loading test cases from the imported test modules
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalliope)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGlissade))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPalindrome))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRorschach))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestThovex))

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCapuletEngine))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSternmanEngine))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWilloughbyEngine))

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSpindlerBattery))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestNubbinBattery))

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCarriganTire))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOctoprimeTire))
    # Add similar lines to load test cases from other modules

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the tests
    result = runner.run(suite)

    # Check the result and return appropriate exit code
    if result.wasSuccessful():
        return 0  # All tests passed
    else:
        return 1  # Some tests failed

if __name__ == '__main__':
    exit_code = run_tests()
    exit(exit_code)
