from tqdm import tqdm
class Comp: 
    def __init__(self, label):
        self.label = label
        self.connected = set()

    def __hash__(self):
        return hash(self.label)
    
    def __eq__(self, other):
        if not isinstance(other, Comp):
            return False
        return self.label == other.label
    
    def __repr__(self):
        return self.label
    
def find_largest_network(comp, network, visited):
    visited = visited.copy()
    visited.add(comp)
    if all([c in comp.connected for c in network]): 
        network = network.copy()
        network.add(comp)
    unvisited = comp.connected.difference(visited)
    if len(unvisited) == 0:
        return (network, visited)
    
    max_network = None
    max_length = 0
    for next in unvisited:
        result = find_largest_network(next, network, visited)
        visited.update(result[1])
        if len(result[0]) > max_length:
            max_network = result[0]
            max_length = len(result[0])
    return (max_network, visited)

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
comps = {}
for line in lines:
    a = Comp(line[0:2])
    if a in comps:
        a = comps[a]
    else:
        comps[a] = a
    b = Comp(line[3:5])
    if b in comps:
        b = comps[b]
    else:
        comps[b] = b
    a.connected.add(b)
    b.connected.add(a)

max_network = None
max_length = 0
for comp in tqdm(comps):
    result = find_largest_network(comp, set([comp]), set([comp]))
    if len(result[0]) > max_length:
        max_length = len(result[0])
        max_network = result[0]
print(','.join(sorted([c.label for c in max_network])))
