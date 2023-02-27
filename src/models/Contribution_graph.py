import json


class contribution_graph:
    width: int
    length: int
    graph: list[list]

    def __init__(self):
        self.width = 0
        self.length = 0
        self.graph = self.init_graph(self, self.width, self.length)

    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length
        self.graph = self.init_graph(self, width, length)

    # Init the graph from file
    def __init__(self, path: str):
        self.graph = json.load(path)

    # Init the graph to default state
    def init_graph(self, width: int, length: int) -> list[list]:
        return [[0 for j in range(width)] for k in range(length)]
