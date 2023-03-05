import json

from .Cell import Cell
from typing import List


class Contribution_Graph:
    width: int
    height: int
    graph: List[List[Cell]]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.graph = self.create_graph(width, height)

    # Init the graph from file
    @classmethod
    def from_string(cls, path: str):
        temp_graph = json.load(path)
        width = len(temp_graph)
        obj = cls(width, len(temp_graph[1]) if width > 0 else 0)
        obj.set_graph(temp_graph)
        return obj

    # Init the graph to default state
    def create_graph(self, width: int, height: int) -> list[list]:
        return [[0 for j in range(width)] for k in range(height)]

    def write(self, path: str):
        with open(path, 'w') as file:
            json.dump(self.graph, file, indent=2)

    def set_graph(self, graph: List[List[Cell]]):
        self.graph = graph

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
