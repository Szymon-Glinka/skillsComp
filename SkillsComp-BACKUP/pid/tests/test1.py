import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

time = 0
integral = 0
previousTime = -1e-6
previousError = 0

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def calculate(self, setpoint, process_variable):
        error = setpoint - process_variable

        # Proportional term
        proportional = self.Kp * error

        # Integral term
        self.integral += error
        integral = self.Ki * self.integral

        # Derivative term
        derivative = self.Kd * (error - self.last_error)
        self.last_error = error

        # Calculate the control signal
        control_signal = proportional + integral + derivative

        return control_signal

def system(t, temp, Tq):
    epsilon = 1
    tau = 4
    Tf = 300
    Q = 2
    dTdt = 1/[(tau*(1+epsilon)) * (Tf-temp) + Q/(1+epsilon)*(Tq-temp)]
    return dTdt

# number of steps
num_of_steps = 300
previousTime = 0
initialValue = 20
delta_T = 0.1
list_of_resoultValues = [initialValue]
time_list = [previousTime]


list_of_manipulatedVariables = []
setpoint = 310
integral = 0

pid = PIDController(21, 0.0, 0.0)

for i in range(1, num_of_steps):
    time = i * delta_T
    time_span = np.linspace(previousTime, time, 10)
    time_list.append(time)

    manipulatedVariable = pid.calculate(setpoint, list_of_resoultValues[-1]),
    resoultValues = odeint(system, list_of_resoultValues[-1], time_span, args = manipulatedVariable, tfirst=True)


    list_of_resoultValues.append(resoultValues[-1][0])
    list_of_manipulatedVariables.append(manipulatedVariable[0])

    previousTime = time

plt.plot(time_list, list_of_resoultValues)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()