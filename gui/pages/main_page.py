from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui.pages.page_object import PageObject
from gui.controls.z_button import ZButton
from plotting.two_d_gymbal_plot import Plot

class MainPage(PageObject):
    def __init__(self, master, title_text, page_index, pop_up_index):
        super().__init__(master, title_text, page_index, pop_up_index)

        self.left_axis_plot = Plot(1, "Controller - Left stick")
        canvas = FigureCanvasTkAgg(self.left_axis_plot.fig, master=self.figure_area_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side='left', fill='both', expand=False)

        # self.right_axis_plot = Plot(1, "Controller - Right stick")
        # canvas2 = FigureCanvasTkAgg(self.right_axis_plot.fig, master=self.figure_area_frame)
        # canvas2.draw()
        # canvas2.get_tk_widget().pack(side='left', fill='both', expand=False)


        self.export_csv_button = ZButton(self.footer_frame, text="Export CSV")
        self.export_csv_button.pack(side='left', fill='both', expand=True)
        self.export_png_button = ZButton(self.footer_frame, text="Export PNG")
        self.export_png_button.pack(side='left', fill='both', expand=True)
        self.export_start_button = ZButton(self.footer_frame, text="Start / stop experiment")
        self.export_start_button.pack(side='left', fill='both', expand=True)
