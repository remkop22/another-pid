
class PID:

    def __init__(self, Kp, Ki, Kd, time_interval, set_point):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.time_interval = time_interval
        self.set_point = set_point

        self.accumalative_error = 0
        self.previous_error = 0

    def error(self, process_value):
        return self.set_point - process_value

    def proportional(self, process_value):
        return self.error(process_value) * self.Kp

    def integral(self, process_value):
        self.accumalative_error += self.error(process_value) * self.time_interval
        return self.accumalative_error * self.Ki

    def derivative(self, process_value):
        derr = (self.error(process_value) - self.previous_error) / self.time_interval
        self.previous_error = self.error(process_value)
        return derr * self.Kd

    def next_value(self, process_value):
        p = self.proportional(process_value)
        i = self.integral(process_value)
        d = self.derivative(process_value)
        return p + i + d
