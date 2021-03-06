import unittest
from treelib import Tree


class TestTree1(unittest.TestCase):

    def setUp(self):
        input = [1, [5, 0, 2], 0, [7, [2, [0], 3]], [[0]]]
        self.test_tree = Tree(input)

    def test_tree(self):
        min, max = self.test_tree.get_depths()
        self.assertEqual(min, 1)
        self.assertEqual(max, 4)


if __name__ == '__main__':
    unittest.main()
