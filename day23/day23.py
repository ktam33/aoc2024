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


connected_comps = set()
for a in comps:
    for b in a.connected:
        for c in b.connected:
            if a in b.connected and a in c.connected:
                connected_comps.add(tuple(sorted((a.label, b.label, c.label))))

answer = 0
for x in connected_comps:
    if x[0][0] == 't' or x[1][0] == 't' or x[2][0] == 't':
        answer += 1
print(answer)

