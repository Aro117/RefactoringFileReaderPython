import unittest
from validator import Validator





suite = unittest.TestLoader().loadTestsFromTestCase(RefactorTests)
unittest.TextTestRunner(verbosity=1).run(suite)
