import copy

import matplotlib.pyplot as plt
import tkinter as tk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from three_d_shapes.three_d_shape import ThreeDShape
from three_d_shapes.two_d_shape import TwoDShape
from three_d_shapes.coordinate import Coordinate, Position
from math import sin, cos, pi, sqrt, degrees
import numpy as np


class Plot3D:
    def __init__(self, title, screen_width, screen_height):
        self.fig = None
        self.ax = None

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title
        self.view_size = 200
        self.initialise_3d_plot()

        self.bodies = []
        self.bodies.append(self.draw_base())
        # self.bodies.append(self.draw_tower(70))
        # self.bodies.append(self.draw_turret_base(100))
        # self.bodies.append(self.draw_turret_top(102.5))

        self.origin = Position()

    def initialise_3d_plot(self, view_size=200):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')
        dpi = 100
        w = int((self.screen_width / 40)*39) / dpi
        h = int(self.screen_height * 0.75) / dpi
        self.fig.set_size_inches(w, h)

        # set up the axis
        self.view_size = view_size
        self.reset_ax()

    def plot_position(self, origin_position):
        # X = red
        position = Position()
        position.update_dh(theta=0, r=20, d=0, alpha=0)
        position.calculate_resultant_homogen(origin_position.resultant_homogen)
        x2, y2, z2 = position.get_relative_coordinate()
        x = [origin_position.x, x2]
        y = [origin_position.y, y2]
        z = [origin_position.z, z2]
        self.ax.plot(x, y, z, 'red')

        # Y = green
        position = Position()
        position.update_dh(theta=90, r=20, d=0, alpha=0)
        position.calculate_resultant_homogen(origin_position.resultant_homogen)
        x2, y2, z2 = position.get_relative_coordinate()
        x = [origin_position.x, x2]
        y = [origin_position.y, y2]
        z = [origin_position.z, z2]
        self.ax.plot(x, y, z, 'green')

        # Z = blue
        position = Position()
        position.update_dh(theta=0, r=0, d=20, alpha=0)
        position.calculate_resultant_homogen(origin_position.resultant_homogen)
        x2, y2, z2 = position.get_relative_coordinate()
        x = [origin_position.x, x2]
        y = [origin_position.y, y2]
        z = [origin_position.z, z2]
        self.ax.plot(x, y, z, 'blue')

    def reset_ax(self):
        self.ax.clear() # clear old setup

        # set up the axis
        self.ax.set_xlim([-1*self.view_size, self.view_size])
        self.ax.set_ylim([-1*self.view_size, self.view_size])
        self.ax.set_zlim([0, self.view_size*2])
        self.ax.set_aspect('equal')

        self.ax.set_xlabel("x (mm)")
        self.ax.set_ylabel("y (mm)")
        self.ax.set_zlabel("z (mm)")

        self.ax.grid()

    def draw_base(self):
        # draw a circle shape 5mm off the origin plane
        base_circle = TwoDShape()
        radius = 150/2 # mm
        circle_height = 5 # mm
        sagitta = 41.25 # mm
        chord_length = 2 * sqrt((2*radius*sagitta)-(sagitta**2))
        half_chord = chord_length/2
        angle = degrees(sin(half_chord/radius))
        print("angle = ", angle)
        point = Position()
        point.update_dh(theta=angle, r=radius, d=0, alpha=0)
        base_circle.add_vertices(copy.deepcopy(point))
        angle_increment = (360 - (2*angle)) / 20 # where 20 is the number of increments
        index = 0
        total_angle = 0
        while total_angle < 360 - angle:
            index += 1
            total_angle = angle + (angle_increment * index)
            point.update_dh(theta=total_angle, r=radius, d=0, alpha=0)
            base_circle.add_vertices(copy.deepcopy(point))
        total_angle = 360 - angle
        point.update_dh(theta=total_angle, r=radius, d=0, alpha=0)
        base_circle.add_vertices(copy.deepcopy(point))

        # turn the whole shape ccw 90 degrees
        for vertex in base_circle.vertices:
            vertex.update_dh_mods(theta_mod=vertex.theta[1]+90)

        # extrude this into a 3 dimensional object 65mm tall
        extruded_object = ThreeDShape(base_circle, 65, 'blue')
        extruded_object.change_origin_position(z=5)
        return extruded_object

    # def draw_tower(self, base_height):
    #     # draw a circle shape 5mm off the origin plane
    #     base_circle = TwoDShape()
    #     radius = 110 / 2  # mm
    #     circle_height = base_height  # mm
    #     last_y = 0
    #     last_x = 0
    #     for angle in range(180, 360, 10): # only draw half the circle
    #         x = sin((angle * (pi / 180))) * radius
    #         y = cos((angle * (pi / 180))) * radius
    #         last_y = y
    #         last_x = x
    #         base_circle.add_vertices(x, y, circle_height)
    #
    #     last_x = last_x + radius
    #     base_circle.add_vertices(last_x, last_y, circle_height)
    #
    #     last_y = last_y - 15
    #     base_circle.add_vertices(last_x, last_y, circle_height)
    #     last_x = last_x - 27.5
    #     base_circle.add_vertices(last_x, last_y, circle_height)
    #     last_y = last_y - 80
    #     base_circle.add_vertices(last_x, last_y, circle_height)
    #     last_x = last_x + 27.5
    #     base_circle.add_vertices(last_x, last_y, circle_height)
    #     last_y = last_y - 15
    #     base_circle.add_vertices(last_x, last_y, circle_height)
    #
    #     # extrude this into a 3 dimensional object 65mm tall
    #     extruded_object = ThreeDShape(base_circle, 30, 'black')
    #     return extruded_object
    #
    # def draw_turret_base(self, height):
    #     # draw a circle shape 5mm off the origin plane
    #     base_circle = TwoDShape()
    #     radius = 40 / 2  # mm
    #     circle_height = height  # mm
    #     for angle in range(0, 360, 10): # only draw half the circle
    #         x = sin((angle * (pi / 180))) * radius
    #         y = cos((angle * (pi / 180))) * radius
    #         base_circle.add_vertices(x, y, circle_height)
    #
    #     # extrude this into a 3 dimensional object 65mm tall
    #     extruded_object = ThreeDShape(base_circle, 2.5, 'blue')
    #     return extruded_object
    #
    # def draw_turret_top(self, height):
    #     # draw a circle shape 5mm off the origin plane
    #     base_circle = TwoDShape()
    #     radius = 40 / 2  # mm
    #     circle_height = height  # mm
    #     for angle in range(0, 180, 10): # only draw half the circle
    #         x = sin((angle * (pi / 180))) * radius
    #         y = cos((angle * (pi / 180))) * radius
    #         base_circle.add_vertices(x, y, circle_height)
    #
    #     # extrude this into a 3 dimensional object 65mm tall
    #     extruded_object = ThreeDShape(base_circle, 15-2.5, 'blue')
    #     return extruded_object


    def update(self):
        # removes all stuff from previous plot and resets the axis
        self.reset_ax()
        self.origin.resultant_homogen = self.origin.homogeneous_transformation
        self.plot_position(self.origin) # x = 'red', y = 'green', z = 'blue'

        # set up variables and loops
        polygons = []
        for body in self.bodies:

            # plot origin
            body.calculate_origin_position()
            self.plot_position(body.origin)

            shape_count = 0
            for shape in body.shapes:

                # adds filled polygon objects to a list
                vertices = shape.get_verts_to_plot()
                polygons.append(Poly3DCollection(vertices, color=body.colour, alpha=.5)) # alpha=.7

                # plots outlines base shape and the extruded shape (shape[0], and shape[1])
                if shape_count < 2:
                    x, y, z = shape.get_coordinates_to_plot()
                    self.ax.plot(x, y, z, color=body.colour)
                    shape_count += 1

            # this loop generates the sides of each body by making rectangles between each set
            # of four vertexes made by the base shape and extruded shape
            for vertex in range(len(body.shapes[0].vertices)):
                x = []
                y = []
                z = []

                if vertex < len(body.shapes[0].vertices) - 1:
                    x.append(body.shapes[0].vertices[vertex].x)
                    y.append(body.shapes[0].vertices[vertex].y)
                    z.append(body.shapes[0].vertices[vertex].z)

                    x.append(body.shapes[0].vertices[vertex + 1].x)
                    y.append(body.shapes[0].vertices[vertex + 1].y)
                    z.append(body.shapes[0].vertices[vertex + 1].z)

                    x.append(body.shapes[1].vertices[vertex + 1].x)
                    y.append(body.shapes[1].vertices[vertex + 1].y)
                    z.append(body.shapes[1].vertices[vertex + 1].z)

                    x.append(body.shapes[1].vertices[vertex].x)
                    y.append(body.shapes[1].vertices[vertex].y)
                    z.append(body.shapes[1].vertices[vertex].z)

                else:
                    x.append(body.shapes[0].vertices[vertex].x)
                    y.append(body.shapes[0].vertices[vertex].y)
                    z.append(body.shapes[0].vertices[vertex].z)

                    x.append(body.shapes[0].vertices[0].x)
                    y.append(body.shapes[0].vertices[0].y)
                    z.append(body.shapes[0].vertices[0].z)

                    x.append(body.shapes[1].vertices[0].x)
                    y.append(body.shapes[1].vertices[0].y)
                    z.append(body.shapes[1].vertices[0].z)

                    x.append(body.shapes[1].vertices[vertex].x)
                    y.append(body.shapes[1].vertices[vertex].y)
                    z.append(body.shapes[1].vertices[vertex].z)

                # jam them in a numpy list adding the first again to close the loop / polygon
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                z = np.append(z, z[0])

                verts = []
                verts.append(list(zip(x, y, z)))
                verts = np.array(verts)

                polygons.append(Poly3DCollection(verts, color=self.bodies[0].colour, alpha=.5))  # alpha=.7

        # plots all polygons in list
        for polygon in polygons:
            self.ax.add_collection3d(polygon)