import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Plot:
    def __init__(self, plot_type, title):
        self.fig = plt.figure()
        self.ax = None

        self.title = title
        self.type = plot_type
        if self.type == 1:
            self.initialise_2d_plot()
        if self.type == 2:
            self.initialise_3d_plot()


    def initialise_2d_plot(self):
        self.ax.set(xlabel='x axis', ylabel='y axis',
               title=self.title)

    def initialise_3d_plot(self):
        self.ax = self.fig.add_subplot(projection='3d')

    def plot_points(self,x,y):
        self.ax.plot(x, y)