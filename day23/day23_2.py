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
    
def find_longest_cycle(start, current, length, path, visited, cycle_length, longest_cycle):
    unvisited = current.connected.difference(visited)
    path.append(current)
    visited.append(current)
    if len(unvisited) == 0:
        return (cycle_length, longest_cycle)
    else:
        potential_cycles = []
        if start in unvisited:
            cycle_length = length + 1
            longest_cycle = path.copy().append(start)
        for comp in unvisited:
            if comp != start:
                path_copy = path.copy()
                path_copy.append(comp)
                visited_copy = visited.copy()
                visited_copy.append(comp)
                potential_cycles.append(find_longest_cycle(start, comp, length + 1, path_copy, visited_copy, cycle_length, longest_cycle))
        max_length = 0
        max_cycle_path = None
        for cycle in potential_cycles:
            if cycle[0] is not None and cycle[0] > max_length:
                max_length = cycle[0]
                max_cycle_path = cycle[1]
        return (max_length, max_cycle_path)



with open('test_input.txt', 'r') as file:
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


current = comps[Comp('ka')]
asdf = find_longest_cycle(current, current, 0, [], [], None, None)
pass
