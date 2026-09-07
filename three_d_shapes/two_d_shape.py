import copy
import numpy as np
from three_d_shapes.coordinate import Coordinate

class TwoDShape:
    def __init__(self):
        self.vertices = []

    def add_vertices(self, x, y, z):
        coordinate = Coordinate(x, y, z)
        self.vertices.append(coordinate)

    def get_coordinates_to_plot(self):
        # generate lists of x, y, and z coordinates
        x = []
        y = []
        z = []
        for vertices in self.vertices:
            x.append(vertices.x)
            y.append(vertices.y)
            z.append(vertices.z)

        # jam them in a numpy list adding the first again to close the loop / polygon
        x.append(copy.deepcopy(x[0]))
        y.append(copy.deepcopy(y[0]))
        z.append(copy.deepcopy(z[0]))

        return x, y, z

    def get_verts_to_plot(self):
        # generate lists of x, y, and z coordinates
        x = []
        y = []
        z = []
        for vertices in self.vertices:
            x.append(vertices.x)
            y.append(vertices.y)
            z.append(vertices.z)

        # jam them in a numpy list adding the first again to close the loop / polygon
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        z = np.append(z, z[0])

        verts = []
        verts.append(list(zip(x, y, z)))
        verts = np.array(verts)

        return verts