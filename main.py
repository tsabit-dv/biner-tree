class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = Node(value)

    def insert_right(self, value):
        self.right = Node(value)

    def display_tree(self, prefix="", is_left=True):
        result = ""
        if self.right is not None:
            result += self.right.display_tree(prefix + ("│   " if is_left else "    "), False)
        result += prefix + ("└── " if is_left else "┌── ") + str(self.value) + "\n"
        if self.left is not None:
            result += self.left.display_tree(prefix + ("    " if is_left else "│   "), True)
        return result

def build_binary_tree(value):
    if value <= 0:
        return None
    node = Node(value)
    node.insert_left(value // 2)
    node.insert_right(value // 2)
    node.left = build_binary_tree(value // 2)
    node.right = build_binary_tree(value // 2)
    return node

# Membuat akar Biner
root = build_binary_tree(1024)
print(root.display_tree())
