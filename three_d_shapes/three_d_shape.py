import copy
from three_d_shapes.coordinate import Coordinate
from three_d_shapes.two_d_shape import TwoDShape

class ThreeDShape:
    def __init__(self, shape, height):
        self.shapes = []
        self.base_shape = shape
        self.shapes.append(shape)

        self.height = height
        self.extrude_base_shape()


    def extrude_base_shape(self):
        new_shape = copy.deepcopy(self.base_shape)
        self.shapes.append(new_shape)
        for vertices_index in range(len(self.base_shape.vertices)):
            self.shapes[1].vertices[vertices_index].z = self.base_shape.vertices[vertices_index].z + self.height

        for vertices_index in range(len(self.base_shape.vertices)):
            self.shapes.append(TwoDShape())
            current_shape_index = len(self.shapes) - 1

            if vertices_index < len(self.base_shape.vertices) - 1:
                x, y, z = self.base_shape.vertices[vertices_index].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)
                x, y, z = self.base_shape.vertices[vertices_index + 1].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)
                x, y, z = self.shapes[1].vertices[vertices_index + 1].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)
                x, y, z = self.shapes[1].vertices[vertices_index].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)

            else:
                x, y, z = self.base_shape.vertices[vertices_index].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)
                x, y, z = self.base_shape.vertices[0].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)
                x, y, z = self.shapes[1].vertices[0].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)
                x, y, z = self.shapes[1].vertices[vertices_index].get()
                self.shapes[current_shape_index].add_vertices(x, y, z)