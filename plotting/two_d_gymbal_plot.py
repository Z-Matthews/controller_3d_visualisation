import matplotlib.pyplot as plt

class Plot:
    def __init__(self, plot_type, title):
        self.fig = None
        self.ax = None

        self.title = title
        self.type = plot_type
        if self.type == 1:
            self.initialise_2d_plot()
        if self.type == 2:
            self.initialise_3d_plot()


    def initialise_2d_plot(self):
        self.fig, self.ax = plt.subplots(1, 2)

    def initialise_3d_plot(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')

    def plot_points(self,x,y):
        self.ax.plot(x, y)

    def update(self, x1, y1, x2, y2):
        for ax in self.ax:
            ax.clear() # clear old setup

            # set up the axis
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            ax.set_xlabel('X (mm)')
            ax.set_ylabel('Y (mm)')
            ax.set_aspect('equal')
            ax.grid()

        # plot stick positions
        circle = plt.Circle((x1, y1), 0.25, alpha = 0.5)
        circle2 = plt.Circle((x1, y1), 0.2, alpha=0.5)
        self.ax[0].add_patch(circle)
        self.ax[0].add_patch(circle2)

        # plot stick positions
        circle3 = plt.Circle((x2, y2), 0.25, alpha = 0.5)
        circle4 = plt.Circle((x2, y2), 0.2, alpha=0.5)
        self.ax[1].add_patch(circle3)
        self.ax[1].add_patch(circle4)