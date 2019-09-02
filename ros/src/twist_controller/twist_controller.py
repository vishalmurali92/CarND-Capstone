
GAS_DENSITY = 2.858
ONE_MPH = 0.44704


class Controller(object):
    def __init__(self,vehicle_mass,fuel_capacity,brake_deadband,decel_limit,
        accel_limit,wheel_radius,wheel_base,steer_ratio,max_lat_accel,max_steer_angle):

        self.yaw_controller = YawController(wheel_base,steer_ratio,0.1,max_lat_accel,max_steer_angle)
        

    def control(self, *args, **kwargs):
        # TODO: Change the arg, kwarg list to suit your needs
        # Return throttle, brake, steer
        return 1., 0., 0.
