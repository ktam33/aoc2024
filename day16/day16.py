with open('test_input.txt', 'r') as file:
    lines = [line.strip() for line in file]



nodes = set()
start = None
current_dir = '>'

class Node:
    def __init__(self, pos, label):
        self.pos = pos
        self.label = label

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.pos == other.pos and self.label == other.label

    def __hash__(self):
        return hash(self.pos)

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        nodes.add(Node((i, j), char))

