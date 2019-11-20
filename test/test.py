import unittest

class WelcomeTest(unittest.TestCase):

    # positive scenario...
    def test_welcome_success(self):
        self.assertEqual('dannel', 'dannel')
    
    # negative scenario...
    def test_welcome_failure(self):
        self.assertEqual('dannel', 'joel')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output = 'test-reports')
    unittest.main(testRunner = runner)
    unittest.main()