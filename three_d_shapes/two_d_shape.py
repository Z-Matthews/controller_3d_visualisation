import copy
import numpy as np
from three_d_shapes.coordinate import Coordinate, Position

class TwoDShape:
    def __init__(self):
        self.vertices = []
        self.origin = Position()

    def add_vertices(self, position):
        # position = Position()
        self.vertices.append(position)

    def update_origin_position(self, origin):
        self.origin = copy.deepcopy(origin)

    def get_coordinates_to_plot(self):
        # generate lists of x, y, and z coordinates
        x = []
        y = []
        z = []
        for vertices in self.vertices:
            vertices.calculate_resultant_homogen(self.origin.resultant_homogen)
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
            #self.origin.calculate_resultant_homogen(self.origin.resultant_homogen)
            vertices.calculate_resultant_homogen(self.origin.resultant_homogen)
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