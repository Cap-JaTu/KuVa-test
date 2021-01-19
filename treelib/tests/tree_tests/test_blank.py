import unittest
from treelib import Tree


class TestBlankTree(unittest.TestCase):

    def setUp(self):
        input = []
        self.test_tree = Tree(input)

    def test_tree(self):
        min, max = self.test_tree.get_depths()
        self.assertIsNone(min)
        self.assertIsNone(max)


if __name__ == '__main__':
    unittest.main()
