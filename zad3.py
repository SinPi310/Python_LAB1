class Node:
    def __init__(self, value=None):
        self.value = value
        self.edges = []

class Tree:
    #konstruktor, do utworzenia korzenia drzewa
    def __init__(self, root_value=None):
        self.root = Node(root_value)

    #tworzenie nowego węzła do drzewa
    def add_node(self, parent, value):
        new_node = Node(value)
        parent.edges.append(new_node)
        return new_node

    #rekurencyjne przeszukiwanie drzewa
    def traverse(self, node, visit_func, depth=0):
        if node is not None:
            visit_func(node, depth)
            for edge in node.edges:
                self.traverse(edge, visit_func, depth + 1)

    #wbudowana metoda służąca do czytelnej reprezentacji
    def __str__(self):
        tree_str = []
        self.traverse(self.root, lambda node, depth: tree_str.append("  " * depth + str(node.value)))
        return "\n".join(tree_str)

# Przykład użycia:
if __name__ == "__main__":

    my_tree = Tree("A")
    b_node = my_tree.add_node(my_tree.root, "B")
    c_node = my_tree.add_node(my_tree.root, "C")
    my_tree.add_node(b_node, "D")
    my_tree.add_node(b_node, "E")
    #my_tree.add_node(c_node, "F")

    f_node = my_tree.add_node(c_node, "F")
    my_tree.add_node(f_node, "G")
    my_tree.add_node(f_node, "H")


    # Sprawdzenie, gdzie jest korzeń drzewa:
    root_node = my_tree.root
    root_value = root_node.value

    print("Drzewo:")
    print(my_tree)


    print("Korzeń drzewa:", root_value)