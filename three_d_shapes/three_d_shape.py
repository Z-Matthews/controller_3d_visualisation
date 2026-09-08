import copy
from three_d_shapes.coordinate import Coordinate, Position
from three_d_shapes.two_d_shape import TwoDShape

class ThreeDShape:
    def __init__(self, shape, height, colour):
        self.positionTracking = []

        # x displacement -----> change r value to x displacement
        self.positionTracking.append(Position())

        # y displacement -----> change r to value of y displacement
        self.positionTracking.append(Position())
        self.positionTracking[1].update_dh_mods(theta_mod=90)

        # z displacement -----> change d to value of z displacement
        self.positionTracking.append(Position())
        self.positionTracking[2].update_dh_mods(theta_mod=-90, d_mod=5)

        # yaw (angle around z axis) -----> change theta to value of angle around z in degrees (positive is counter-clockwise)
        self.positionTracking.append(Position())

        # pitch (angle around y axis)
        self.positionTracking.append(Position())
        self.positionTracking[4].update_dh_mods(theta_mod=90)

        # roll (angle around x axis)
        self.positionTracking.append(Position())
        self.positionTracking[5].update_dh_mods(theta_mod=-90)

        self.origin = Position()
        self.shapes = []
        self.base_shape = shape
        self.shapes.append(shape)
        self.colour = colour

        self.height = height
        self.extrude_base_shape()

    def change_origin_position(self, x=None, y=None, z=None, yaw=None, pitch=None, roll=None):
        # x displacement -----> change r value to x displacement
        if x is not None:
            self.positionTracking[0].update_dh(r=x)

        # y displacement -----> change r to value of y displacement
        if y is not None:
            self.positionTracking[1].update_dh(r=y)

        # z displacement -----> change d to value of z displacement
        if z is not None:
            self.positionTracking[2].update_dh(d=z)

        # yaw (angle around z axis) -----> change theta to value of angle around z in degrees (positive is counter-clockwise)
        if yaw is not None:
            self.positionTracking[3].update_dh(theta=(-1*yaw))

        # pitch (angle around y axis)
        if pitch is not None:
            self.positionTracking[4].update_dh(alpha=(-1*pitch))

        # roll (angle around x axis)
        if roll is not None:
            self.positionTracking[5].update_dh(alpha=(-1*roll))

        self.calculate_origin_position()

    def calculate_origin_position(self):
        # we need to multiply each joint nodes origin by the previous to get the resultant homogen
        for index in range(len(self.positionTracking)):
            if index > 0:
                self.positionTracking[index].calculate_resultant_homogen(self.positionTracking[index -1].resultant_homogen)
            else:
                self.positionTracking[index].resultant_homogen = self.positionTracking[index].homogeneous_transformation
            # print(f'homogen_{index}')
            # print(self.positionTracking[index].resultant_homogen)

        self.origin = self.positionTracking[len(self.positionTracking)-1]

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