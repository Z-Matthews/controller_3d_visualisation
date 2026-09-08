# This is a test script to interact with an Arduino connected with usb
# via the serial interface class
# allowing the user to configure visualisation and output settings based on a generic GUI
from gui.gui_control import TKinterApp
from serial_interface_library.serial_interface import SerialInterface
from controller_interface import ControllerInterface
# import threading
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
    app.pages[2].left_axis_plot.update(
        controller.left_stick_x,
        controller.left_stick_y,
        controller.right_stick_x,
        controller.right_stick_y
    )
def plt2_animate(i):
    #controller.get_controller_inputs()
    # This is where we would animate the fucking main 3D plot
    app.pages[0].three_d_plot.update()

app.protocol("WM_DELETE_WINDOW", app.on_closing)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # detect_ports()
    # if app.current_page_index

    match app.page_dictionary[app.current_page_index][0]:
        case "Main Page" | "Main page popup": # main page
            ani1 = animation.FuncAnimation(app.pages[0].three_d_plot.fig, plt2_animate, interval=20,
                                           cache_frame_data=False)
        case "Controller page" | "Controller page popup": # connect blue tooth controller and switch initial show page to 2 to test this
            if controller.auto_connect():
                ani2 = animation.FuncAnimation(app.pages[2].left_axis_plot.fig, plt1_animate, interval=1,
                                               cache_frame_data=False)
        case _:
            print("Not currently a valid page index")  # Default case

    app.mainloop()



