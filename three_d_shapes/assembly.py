import copy
from three_d_shapes.coordinate import Coordinate, Position
from three_d_shapes.two_d_shape import TwoDShape
from three_d_shapes.three_d_shape import ThreeDShape

class Joint:
    def __init__(self, index_of_ground_object, index_of_moving_object, types):
        self.position = 0
        self.types = types
        self.index_of_ground_object = index_of_ground_object
        self.index_of_moving_object = index_of_moving_object

        # dictate in which dof the moving object can move relative to the ground object
        # how?

    def check_dof_allowed(self, type):
        # check if movement in that dof is allowed
        allowed = False
        for allowed_type in self.types:
            if allowed_type == type:
                allowed = True

        # return type
        match type:
            case 0:
                return f'Translation in x: {self.position}mm, allowed = {allowed}'
            case 1:
                return f'Translation in y: {self.position}mm, allowed = {allowed}'
            case 2:
                return f'Translation in z: {self.position}mm, allowed = {allowed}'
            case 3:
                return f'Yaw / Rotation around z: {self.position}degrees, allowed = {allowed}'
            case 4:
                return f'Pitch / Rotation around y: {self.position}degrees, allowed = {allowed}'
            case 5:
                return f'Roll / Rotation around x: {self.position}degrees, allowed = {allowed}'

            case _:
                return "Movement type / degree of freedom not recognised"

    def change_position(self, dof_str, new_position):
        if new_position != self.position:
            self.position = new_position
            match dof_str:
                case "x":
                    return self.check_dof_allowed(0)
                case "y":
                    return self.check_dof_allowed(1)
                case "z":
                    return self.check_dof_allowed(2)
                case "yaw":
                    return self.check_dof_allowed(3)
                case "pitch":
                    return self.check_dof_allowed(4)
                case "roll":
                    return self.check_dof_allowed(5)

                # If an exact match is not confirmed, this last case will be used if provided
                case _:
                    return "Movement type / degree of freedom not recognised"
        return "No change in position"


class Assembly:
    def __init__(self):
        # place to store list of three-dimensional shapes
        self.bodies = []
        self.joints = []

    # dof_indexes is a list of indexes of the six degrees of freedoms which are allowed by that joint
    #     0: Translation in x: mm
    #     1: Translation in y: mm
    #     2: Translation in z: mm
    #     3: Yaw / Rotation around z: degrees
    #     4: Pitch / Rotation around y: degrees
    #     5: Roll / Rotation around x: degrees
    def add_body(self, body, dof_indexes):
        self.bodies.append(body)
        index_of_moving_object = len(self.bodies) - 1
        if index_of_moving_object < 1:
            index_of_ground_object = None
        else:
            index_of_ground_object = index_of_moving_object - 1
        self.joints.append(Joint(index_of_ground_object, index_of_moving_object, dof_indexes))

    def update_positions(self, dof_strs, joint_positions):
        for index in range(len(self.joints)):
            self.joints[index].change_position(dof_strs[index], joint_positions[index])