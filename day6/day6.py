class Day6Map:
    def __init__(self, lines):
        self.position = (None, None)
        self.orientation = None
        self.height = len(lines)
        self.width = len(lines[0])
        self.obstacles = []
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == '#':
                    self.obstacles.append((i, j))
                if char == "^" or char == "v" or char == "<" or char == ">":
                    self.position = (i, j)
                    self.orientation = char
        self.visited = set()

    def solve(self):
        self.visited.add(self.position)
        while(not self._is_done()):
            next_step = self._get_next_step()
            if next_step in self.obstacles:
                self._change_orientation()
            else:
                self.position = next_step
                self.visited.add(self.position)
        return len(self.visited)

    def _change_orientation(self):
        if self.orientation == "^":
            self.orientation = ">"
        elif self.orientation == ">":
            self.orientation = "v"
        elif self.orientation == "v":
            self.orientation = "<"
        elif self.orientation == "<":
            self.orientation = "^"

    def _get_next_step(self):
        next_step = (None, None)
        if self.orientation == "^":
            next_step = (self.position[0] - 1, self.position[1])
        elif self.orientation == "v":
            next_step = (self.position[0] + 1, self.position[1])
        elif self.orientation == ">":
            next_step = (self.position[0], self.position[1] + 1)
        elif self.orientation == "<":
            next_step = (self.position[0], self.position[1] - 1)
        return next_step

    def _is_done(self):
        if self.position[0] == 0 and self.orientation == "^":
            return True
        elif self.position[0] == self.height - 1 and self.orientation == "v":
            return True
        elif self.position[1] == 0 and self.orientation == "<":
            return True
        elif self.position[1] == self.width - 1 and self.orientation == ">":
            return True
        return False

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = Day6Map(lines)

print(map.solve())

