import unittest
from treelib import Tree


class TestNoZerosTree(unittest.TestCase):

    def setUp(self):
        input = [1, 2, [3, [4]], [5]]
        self.test_tree = Tree(input)

    def test_tree(self):
        min, max = self.test_tree.get_depths()
        self.assertIsNone(min)
        self.assertIsNone(max)


if __name__ == '__main__':
    unittest.main()
