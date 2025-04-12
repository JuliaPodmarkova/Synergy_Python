import random
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def bfs(self):
        if not self.root:
            return []
        queue = deque([self.root])
        result = []
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def dfs_preorder(self):
        return self._dfs_preorder_recursively(self.root)

    def _dfs_preorder_recursively(self, node):
        if node:
            return [node.value] + self._dfs_preorder_recursively(node.left) + self._dfs_preorder_recursively(node.right)
        return []

    def dfs_inorder(self):
        return self._dfs_inorder_recursively(self.root)

    def _dfs_inorder_recursively(self, node):
        if node:
            return self._dfs_inorder_recursively(node.left) + [node.value] + self._dfs_inorder_recursively(node.right)
        return []

    def dfs_postorder(self):
        return self._dfs_postorder_recursively(self.root)

    def _dfs_postorder_recursively(self, node):
        if node:
            return self._dfs_postorder_recursively(node.left) + self._dfs_postorder_recursively(node.right) + [node.value]
        return []

class AVLTree(BinaryTree):
    def insert(self, key):
        self.root = self._insert_balanced(self.root, key)

    def _insert_balanced(self, node, key):
        if not node:
            return Node(key)
        if key < node.value:
            node.left = self._insert_balanced(node.left, key)
        else:
            node.right = self._insert_balanced(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return self.rebalance(node)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rebalance(self, node):
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y


if __name__ == "__main__":
    numbers = random.sample(range(1, 100), 10)  # Генерируем 10 случайных чисел
    print("Сгенерированные числа для заполнения узлов дерева:", numbers)

    # Тестирование BinaryTree
    print("\nТестирование BinaryTree:")
    bt = BinaryTree()
    for num in numbers:
        bt.insert(num)

    print("Обход по ширине: ", bt.bfs())
    print("Обход по длине, прямой подход: ", bt.dfs_preorder())
    print("Обход по длине, симметричный подход: ", bt.dfs_inorder())
    print("Обход по длине, обратный подход: ", bt.dfs_postorder())

    print("\nТестирование AVLTree:")
    avl_tree = AVLTree()
    for num in numbers:
        avl_tree.insert(num)

    print("Обход по ширине: ", avl_tree.bfs())
    print("Обход по длине, прямой подход: ", avl_tree.dfs_preorder())
    print("Обход по длине, симметричный подход: ", avl_tree.dfs_inorder())
    print("Обход по длине, обратный подход: ", avl_tree.dfs_postorder())