import matplotlib.pyplot as plt
import tkinter as tk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from three_d_shapes.three_d_shape import ThreeDShape
from three_d_shapes.two_d_shape import TwoDShape
from three_d_shapes.coordinate import Coordinate, Position
from math import sin, cos, pi

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
        self.bodies.append(self.draw_tower(70))
        self.bodies.append(self.draw_turret_base(100))
        self.bodies.append(self.draw_turret_top(102.5))

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
        x2, y2, z2 = position.get_relative_coordinate()
        x = [origin_position.x, x2]
        y = [origin_position.y, y2]
        z = [origin_position.z, z2]
        self.ax.plot(x, y, z, 'red')

        # Y = green
        position = Position()
        position.update_dh(theta=90, r=20, d=0, alpha=0)
        x2, y2, z2 = position.get_relative_coordinate()
        x = [origin_position.x, x2]
        y = [origin_position.y, y2]
        z = [origin_position.z, z2]
        self.ax.plot(x, y, z, 'green')

        # Z = blue
        position = Position()
        position.update_dh(theta=0, r=0, d=20, alpha=0)
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
        for angle in range(0, 360, 10):
            x = sin((angle * (pi / 180))) * radius
            y = cos((angle * (pi / 180))) * radius
            # add a condition to make the radius smaller if x > 100
            if x > 30:
                x = 30
            base_circle.add_vertices(x, y, circle_height)

        # extrude this into a 3 dimensional object 65mm tall
        extruded_object = ThreeDShape(base_circle, 65, 'blue')
        return extruded_object

    def draw_tower(self, base_height):
        # draw a circle shape 5mm off the origin plane
        base_circle = TwoDShape()
        radius = 110 / 2  # mm
        circle_height = base_height  # mm
        last_y = 0
        last_x = 0
        for angle in range(180, 360, 10): # only draw half the circle
            x = sin((angle * (pi / 180))) * radius
            y = cos((angle * (pi / 180))) * radius
            last_y = y
            last_x = x
            base_circle.add_vertices(x, y, circle_height)

        last_x = last_x + radius
        base_circle.add_vertices(last_x, last_y, circle_height)

        last_y = last_y - 15
        base_circle.add_vertices(last_x, last_y, circle_height)
        last_x = last_x - 27.5
        base_circle.add_vertices(last_x, last_y, circle_height)
        last_y = last_y - 80
        base_circle.add_vertices(last_x, last_y, circle_height)
        last_x = last_x + 27.5
        base_circle.add_vertices(last_x, last_y, circle_height)
        last_y = last_y - 15
        base_circle.add_vertices(last_x, last_y, circle_height)

        # extrude this into a 3 dimensional object 65mm tall
        extruded_object = ThreeDShape(base_circle, 30, 'black')
        return extruded_object

    def draw_turret_base(self, height):
        # draw a circle shape 5mm off the origin plane
        base_circle = TwoDShape()
        radius = 40 / 2  # mm
        circle_height = height  # mm
        for angle in range(0, 360, 10): # only draw half the circle
            x = sin((angle * (pi / 180))) * radius
            y = cos((angle * (pi / 180))) * radius
            base_circle.add_vertices(x, y, circle_height)

        # extrude this into a 3 dimensional object 65mm tall
        extruded_object = ThreeDShape(base_circle, 2.5, 'blue')
        return extruded_object

    def draw_turret_top(self, height):
        # draw a circle shape 5mm off the origin plane
        base_circle = TwoDShape()
        radius = 40 / 2  # mm
        circle_height = height  # mm
        for angle in range(0, 180, 10): # only draw half the circle
            x = sin((angle * (pi / 180))) * radius
            y = cos((angle * (pi / 180))) * radius
            base_circle.add_vertices(x, y, circle_height)

        # extrude this into a 3 dimensional object 65mm tall
        extruded_object = ThreeDShape(base_circle, 15-2.5, 'blue')
        return extruded_object


    def update(self):
        # removes all stuff from previous plot and resets the axis
        self.reset_ax()
        self.plot_position(self.origin) # x = 'red', y = 'green', z = 'blue'
        self.bodies[0].change_origin_position(z=50)
        self.bodies[0].calculate_origin_position()
        self.plot_position(self.bodies[0].origin)

        # # set up variables and loops
        # polygons = []
        # for body in self.bodies:
        #     shape_count = 0
        #     for shape in body.shapes:
        #
        #         # adds filled polygon objects to a list
        #         vertices = shape.get_verts_to_plot()
        #         polygons.append(Poly3DCollection(vertices, color=body.colour, alpha=.5)) # alpha=.7
        #
        #         # plots outlines base shape and the extruded shape (shape[0], and shape[1])
        #         if shape_count < 2:
        #             x, y, z = shape.get_coordinates_to_plot()
        #             self.ax.plot(x, y, z, color=body.colour)
        #             shape_count += 1
        #
        # # plots all polygons in list
        # for polygon in polygons:
        #     self.ax.add_collection3d(polygon)