import matplotlib.pyplot as plt
import tkinter as tk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from three_d_shapes.three_d_shape import ThreeDShape
from three_d_shapes.two_d_shape import TwoDShape
from three_d_shapes.coordinate import Coordinate
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

    def plot_points(self, plot, x, y):
        self.ax[plot].scatter(x, y)

    def reset_ax(self):
        self.ax.clear() # clear old setup

        # set up the axis
        self.ax.set_xlim([-1*self.view_size, self.view_size])
        self.ax.set_ylim([-1*self.view_size, self.view_size])
        self.ax.set_zlim([0, self.view_size*2])
        self.ax.set_aspect('equal')
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
            if x > 50:
                x = 50
            base_circle.add_vertices(x, y, circle_height)

        # extrude this into a 3 dimensional object 65mm tall
        extruded_object = ThreeDShape(base_circle, 65)

        # return the generated object
        return extruded_object

    def update(self):
        # removes all stuff from previous plot and resets the axis
        self.reset_ax()

        # set up variables and loops
        shape_count = 0
        polygons = []
        for body in self.bodies:
            for shape in body.shapes:

                # adds filled polygon objects to a list
                vertices = shape.get_verts_to_plot()
                polygons.append(Poly3DCollection(vertices, alpha=.7))

                # plots outlines base shape and the extruded shape (shape[0], and shape[1])
                if shape_count < 2:
                    x, y, z = shape.get_coordinates_to_plot()
                    self.ax.plot(x, y, z, color='blue')
                    shape_count += 1

        # plots all polygons in list
        for polygon in polygons:
            self.ax.add_collection3d(polygon)