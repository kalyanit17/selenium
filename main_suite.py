import unittest
from SeleniumPythonRefactorTestCase import SearchText
from SeleniumPythonMultipleTests import HomePageTest

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

test_suite = unittest.TestSuite([search_test,home_page])

unittest.TextTestRunner(verbosity=2).run(test_suite)