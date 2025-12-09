class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: "Node | None" = None
        self.right: "Node | None" = None


def insert(root: Node | None, key: int) -> Node:
    """Insert key into BST and return (possibly new) root."""
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    # duplicates are ignored
    return root


def find_min(root: Node | None) -> int | None:
    """Return minimum key in BST, or None if tree is empty."""
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.key


def find_max(root: Node | None) -> int | None:
    """Return maximum key in BST, or None if tree is empty."""
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right
    return current.key


def sum_tree(root: Node | None) -> int:
    """Return sum of all keys in BST."""
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)


if __name__ == "__main__":
    values = [5, 15, 25, 3, 12, 18, 30]
    root = None
    for v in values:
        root = insert(root, v)

    print("Minimum:", find_min(root))
    print("Maximum:", find_max(root))
    print("Sum:", sum_tree(root))
