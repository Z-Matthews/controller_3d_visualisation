# This is a test script to interact with an Arduino connected with usb
# via the serial interface class
# allowing the user to configure visualisation and output settings based on a generic GUI
from gui.gui_control import TKinterApp
from serial_interface_library.serial_interface import SerialInterface
from controller_interface import ControllerInterface
import threading
import matplotlib.animation as animation

controller = ControllerInterface()
SI = SerialInterface()
app = TKinterApp()

def detect_ports():
    # this function detects available ports and then prints them to the terminal
    SI.find_devices()
    print(SI)

def plt1_animate(i):
    controller.get_controller_inputs()
    app.pages[0].left_axis_plot.update(controller.left_stick_x, controller.left_stick_y,controller.right_stick_x, controller.right_stick_y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    detect_ports()
    if controller.auto_connect():
        ani1 = animation.FuncAnimation(app.pages[0].left_axis_plot.fig, plt1_animate, interval=10, cache_frame_data=False)
    app.mainloop()



