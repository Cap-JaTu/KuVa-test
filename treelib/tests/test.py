import unittest
import treelib.tests.tree_tests as Tests


def suite():
    test_cases = [
        Tests.TestBlankTree,
        Tests.TestNoZerosTree,
        Tests.TestTree1,
    ]
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
