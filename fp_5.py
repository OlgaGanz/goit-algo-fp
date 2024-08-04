import uuid
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors:dict, name = "Graph"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node) for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(name)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def insert_nodes(root, key):
    if not root:
        return Node(key)
    queue = [root]
    while queue:
        temp = queue.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    return root

def build_heap_tree(heap_list):
    root = Node(heap_list[0])
    for key in heap_list[1:]:
        root = insert_nodes(root, key)
    return root


def generate_color(step, total_steps):
    base_color = [0, 100, 50]
    new_color = []

    darken_factor = np.interp(step, [0, total_steps], [0, 200])

    for col in base_color:
        new_color.append(np.interp(col + darken_factor, [0, 255], [0, 1]))

    return new_color


def dfs_visualize(root, total_steps):
    visited = []
    stack = [root]
    colors = {}
    step = 0

    if root is None:
        return []

    while stack:
        current = stack.pop()
        visited.append(current.val)
        current.color = generate_color(step, total_steps)
        colors[current.id] = current.color
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        step += 1
    title = "DFS: " + str(visited)

    return colors, title


def bfs_visualize(root, total_steps=1):
    visited = []
    queue = deque([root])
    colors = {}
    step = 0

    if root is None:
        return
    
    while queue:
        node = queue.popleft()
        visited.append(node.val)
        node.color = generate_color(step, total_steps)
        colors[node.id] = node.color

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
        step += 1

    title = "BFS: " + str(visited)

    return colors, title


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    # heap_list = [1, 3, 5, 7, 9, 2]
    heapq.heapify(heap_list)
    # Побудова дерева з купи
    print(heap_list)
    heap_tree_root = build_heap_tree(heap_list)

    # Обрахунок кількості кроків (вузлів)
    total_steps = count_nodes(heap_tree_root)

    # DFS візуалізація
    dfs_colors, title = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors, title)

    # BFS візуалізація
    bfs_colors, title = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors, title)
