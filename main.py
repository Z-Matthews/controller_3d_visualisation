# This is a test script to interact with an Arduino connected with usb
# via the serial interface class
# allowing the user to configure visualisation and output settings based on a generic GUI
from gui.gui_control import TKinterApp
from serial_interface_library.serial_interface import SerialInterface
from controller_interface import ControllerInterface
import threading

controller = ControllerInterface()
SI = SerialInterface()
app = TKinterApp()

def detect_ports():
    # this function detects available ports and then prints them to the terminal
    SI.find_devices()
    print(SI)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    detect_ports()
    if controller.auto_connect():
        thread_1 = threading.Thread(target=controller.get_controller_inputs())
        #ani1 = animation.FuncAnimation(fig, plt1_animate, interval=100, cache_frame_data=False)
        #ani2 = animation.FuncAnimation(fig, plt2_animate, interval=100, cache_frame_data=False)
        thread_1.start()
        #plt.show()
    app.mainloop()



