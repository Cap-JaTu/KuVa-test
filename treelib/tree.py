from anytree import Node, AnyNode, RenderTree, AsciiStyle, LevelOrderGroupIter


class Tree:

    def __init__(self, tree_in: list) -> None:
        self.tree = None
        self._process_tree(tree_in)

    def _process_tree(self, tree_in: list) -> None:
        if not tree_in:
            self.tree = None
            return

        self.tree = AnyNode(id=None)
        stack_level = {
            'idx': 0,
            'list': tree_in,
            'parent': self.tree
        }
        stack = [stack_level]
        while stack:
            enum_data = stack[0]
            idx = enum_data['idx']
            enumerable = enum_data['list']
            parent_node = enum_data['parent']
            if idx >= len(enumerable):
                stack.pop(0)
                continue

            part = enumerable[idx]
            stack[0]['idx'] += 1

            if isinstance(part, int):
                AnyNode(id=part, parent=parent_node)
            elif isinstance(part, list):
                blank_node = AnyNode(id=None, parent=parent_node)
                stack_level = {
                    'idx': 0,
                    'list': part,
                    'parent': blank_node
                }
                stack.insert(0, stack_level)
            else:
                raise ValueError("Don't know what to do with a: %s" % type(part))

    def get_depths(self) -> tuple:
        if not self.tree:
            return None, None

        level = 0
        min = None
        max = None
        for children in LevelOrderGroupIter(self.tree):
            nodes_at_this_level = [node.id for node in children]
            if 0 in nodes_at_this_level:
                if not min or min > level:
                    min = level
                if not max or max < level:
                    max = level
            level += 1

        return min, max
