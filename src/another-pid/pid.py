
class PID:

    def __init__(self, Kp, Ki, Kd, time_interval, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.time_interval = time_interval
        self.setpoint = setpoint

        self.accumalative_error = 0
        self.previous_error = 0

    def error(self, process_value):
        return self.setpoint - process_value

    def proportional(self, process_value):
        return self.error(process_value) * self.Kp

    def integral(self, process_value):
        self.accumalative_error += self.error(process_value) * self.time_interval
        return self.accumalative_error * self.Ki

    def derivative(self, process_value):
        derr = (self.error(process_value) - self.previous_error) / self.time_interval
        self.previous_error = self.error(process_value)
        return derr

    def next_value(self, process_value):
        return self.proportional(process_value) + self.integral(process_value) + self.derivative(process_value)
