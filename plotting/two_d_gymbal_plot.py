import matplotlib.pyplot as plt
import tkinter as tk

class Plot:
    def __init__(self, plot_type, title, screen_width, screen_height):
        self.fig = None
        self.ax = None

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title
        self.type = plot_type
        if self.type == 1:
            self.initialise_2d_plot()
        if self.type == 2:
            self.initialise_3d_plot()


    def initialise_2d_plot(self):
        self.fig, self.ax = plt.subplots(1, 2)
        print(f'Figure width {int((self.screen_width / 40)*39)}px')
        print(f'Figure height {int(self.screen_height * 0.75)}px')
        dpi = 100
        w = int((self.screen_width / 40)*39) / dpi
        h = int(self.screen_height * 0.75)/ dpi
        self.fig.set_size_inches(w, h)

        for ax in self.ax:
            ax.clear() # clear old setup

            # set up the axis
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            ax.set_aspect('equal')
            ax.grid()

    def initialise_3d_plot(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')

    def plot_points(self, plot, x, y):
        self.ax[plot].scatter(x, y)

    def update(self, x1, y1, x2, y2):
        for ax in self.ax:
            ax.clear() # clear old setup

            # set up the axis
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            ax.set_aspect('equal')
            ax.grid()

        # plot stick positions
        circle = plt.Circle((x1, y1), 0.25, alpha = 0.5)
        self.ax[0].add_patch(circle)
        # self.plot_points(0, x1, y1)

        # plot stick positions
        circle3 = plt.Circle((x2, y2), 0.25, alpha = 0.5)
        self.ax[1].add_patch(circle3)
        # self.plot_points(1, x2, y2)