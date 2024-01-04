class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error_sum = 0
        self.last_error = 0

    def compute(self, setpoint, process_variable):
        error = setpoint - process_variable

        # Proportional term
        p = self.kp * error

        # Integral term
        self.error_sum += error
        i = self.ki * self.error_sum

        # Derivative term
        d = self.kd * (error - self.last_error)
        self.last_error = error

        # Compute the control signal
        control_signal = p + i + d

        return control_signal
