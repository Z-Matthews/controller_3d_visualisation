import pygame

class ControllerInterface:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        #print(pygame.version.SDL)

        self.controller = None
        self.num_buttons = 0
        self.num_axes = 0
        self.num_hats = 0
        self.num_balls = 0

        self.pressed_buttons = []

        self.left_stick_x = 0
        self.left_stick_y = 0
        self.right_stick_x = 0
        self.right_stick_y = 0

        self.hat_x = 0
        self.hat_y = 0

    def get_controller_inputs(self):
        pygame.event.pump()
        # Read first axis (left stick vertical/horizontal)
        self.pressed_buttons = []
        for i in range(self.num_buttons):
            if self.controller.get_button(i) > 0:
                self.pressed_buttons.append(i)

        self.left_stick_x = self.controller.get_axis(0)    #get_axis(0)  # negative is left
        self.left_stick_y = self.controller.get_axis(1)  # negative is up
        self.right_stick_x = self.controller.get_axis(3)  # negative is left
        self.right_stick_y = self.controller.get_axis(4)  # negative is up

        for i in range(self.num_hats):
            self.hat_x, self.hat_y = self.controller.get_hat(i)

        # string = f'Lx: {self.left_stick_x}, '
        # string += f'Ly: {self.left_stick_y}, '
        # string += f'Rx: {self.right_stick_x}, '
        # string += f'Ry: {self.right_stick_y}'
        # print(string)
        #
        # if len(self.pressed_buttons) > 0:
        #     button_string = "Buttons pressed: "
        #     for button in self.pressed_buttons:
        #         button_string += check_button_index(button)
        #         button_string += ", "
        #     print(button_string)
        #
        # print(f'x = {self.hat_x}, y = {self.hat_y}')


    def auto_connect(self):
        # Check if a controller is connected
        if pygame.joystick.get_count() > 0:
            self.controller = pygame.joystick.Joystick(0)
            print(f"Connected: {self.controller.get_name()}")

            # just normal buttons
            self.num_buttons = self.controller.get_numbuttons()
            print(f'number of buttons on controller: {self.num_buttons}')

            # this is like joystick axes
            self.num_axes = self.controller.get_numaxes()
            print(f'number of axes on controller: {self.num_axes}')

            # i think this is the d pad type things with axes that act like a digital joystick
            # with values output like -1, 0 , or 1
            self.num_hats = self.controller.get_numhats()
            print(f'number of hats on controller: {self.num_hats}')

            # no idea what this is, but we don't have any
            self.num_balls = self.controller.get_numballs()
            print(f'number of balls on controller: {self.num_balls}')

            return True
        else:
            print("No controller found.")
            return False

def check_button_index(index):
    match index:
        case 0:
            return "circle"
        case 1:
            return "x"
        case 2:
            return "P1"
        case 3:
            return "triangle"
        case 4:
            return "square"
        case 5:
            return "P2"
        case 6:
            return "L1"
        case 7:
            return "R1"
        case 8:
            return "L2"
        case 9:
            return "R2"
        case 10:
            return "select"
        case 11:
            return "start"
        case 12:
            return "steam"
        case 13:
            return "LJ1"
        case 14:
            return "RJ1"
        case 15:
            return "new"

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Button not found"