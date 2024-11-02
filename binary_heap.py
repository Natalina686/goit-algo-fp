import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуємо значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def insert_into_heap(root, key):
    #  Вставляємо новий ключ у купу та зберігаємо властивості купи.

    new_node = Node(key)
    if root is None:
        return new_node
    
    #  Використовуємо чергу для знаходження правильного місця для нового вузла.
    queue = [root]
    while queue:
        current = queue.pop(0)
        
        if current.left is None:
            current.left = new_node
            return root
        else:
            queue.append(current.left)
        
        if current.right is None:
            current.right = new_node
            return root
        else:
            queue.append(current.right)

def build_heap(values):
    # Будуємо бінарну купу з масиву значень..
    root = None
    for value in values:
        root = insert_into_heap(root, value)
    
    return root

# Приклад
heap_values = [10, 20, 30, 40, 50]
heap_root = build_heap(heap_values)

# Відображення купи
draw_tree(heap_root)