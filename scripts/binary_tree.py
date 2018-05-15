
class BinaryTree(object):
    #TODO: docstring
    def __init__(self, name):
        """ create a binary node """
        self._key = name
        self._left_child = None
        self._right_child = None
    
    @property
    def right_child(self):
        #TODO: docstring
        return self._right_child
    
    @property
    def left_child(self):
        #TODO: docstring
        return self._left_child
        
    @property
    def key(self):
        #TODO: docstring
        return self._key
    
    @left_child.setter
    def left_child(self, new_node):
        #TODO: docstring
        if self._left_child:
            t = BinaryTree(new_node)
            t._left_child = self._left_child
            self._left_child = t
        else:
            self._left_child = BinaryTree(new_node)
    
    @right_child.setter
    def right_child(self, new_node):
        #TODO: docstring
        if self.right_child:
            t = BinaryTree(new_node)
            t._right_child = self._right_child
            self._right_child = t
        else:
            self._right_child = BinaryTree(new_node)
    
    @key.setter   
    #TODO: docstring
    def key(self, key):
        self._key = key

def in_order_traversal(tree, func=print):
    #TODO: docstring
    if tree:
        in_order_traversal(tree.left_child)
        print(tree.key)
        in_order_traversal(tree.right_child)

def pre_order_traversal(tree, func=print):
    #TODO: docstring
    if tree:
        print(tree.key)
        in_order_traversal(tree.left_child)
        in_order_traversal(tree.right_child)

def post_order_traversal(tree, func=print):
    #TODO: docstring
    if tree:
        in_order_traversal(tree.left_child)
        in_order_traversal(tree.right_child)
        print(tree.key)

def binary_tree_bfs(tree, func=print):
    #TODO: docstring
    from collections import deque
    if tree.key is None:
        raise TypeError('root is None')
    queue = deque()
    queue.append(tree.key)
    while queue:
        node = queue.popleft()
        func(node)
        if node.left_child is not None:
            queue.append(node.left_child)
        if node.right_child is not None:
            queue.append(node.right_child)