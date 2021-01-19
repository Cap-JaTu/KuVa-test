import unittest
from treelib import Tree


class TestTree1(unittest.TestCase):

    def setUp(self):
        input = [[1, 0, 0, 0]]
        self.test_tree = Tree(input)

    def test_tree(self):
        min, max = self.test_tree.get_depths()
        self.assertEqual(min, 2)
        self.assertEqual(max, 2)


if __name__ == '__main__':
    unittest.main()
