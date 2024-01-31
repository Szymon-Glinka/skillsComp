import numpy as np
import time
from scipy.integrate import odeint


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        '''This class contains the PID controller's algorithm, the system that the PID controller is controlling and zeigler nichols tuning system'''
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def calculate(self, setpoint, process_variable):
        '''This function is the PID controller's algorithm. It takes in the setpoint and the process variable and returns the control signal'''
        
        error = setpoint - process_variable                      #Calculating the error

        #--- Calculating the proportional trerm ---
        proportional = self.Kp * error

        #--- Calculating the integral term ---
        self.integral += error
        integral = self.Ki * self.integral
        
        #--- Calculating the derivative term ---
        derivative = self.Kd * (error - self.last_error)
        self.last_error = error


        control_signal = proportional + integral + derivative    #calculating the control signal

        return control_signal
    
    def zeigler_nichols_tuning(process_func, initial_output, step_size=0.01, max_output=1.0):
        # Initialize tuning parameters
        ku = 0
        tu = 0
        kp = 0
        ki = 0
        kd = 0

        # Step 1: Find ultimate gain and ultimate period
        output = initial_output
        while output < max_output:
            output = process_func(output)
            time.sleep(step_size)
            ku = max(ku, output)

        tu = step_size * (ku - initial_output)

        # Step 2: Calculate PID parameters
        kp = 0.6 * ku
        ki = 2 * kp / tu
        kd = kp * tu / 8

        return kp, ki, kd

    def system(self, none1, none2, MV):
        '''This function is the system that the PID controller is controlling. It takes in the manipulated variable(MV) and returns the deretive of the result variable(X)'''

        #--- system ---
        dXdt =  (MV * 2) + (MV * 3) / 4 
        
        return dXdt


def simulation():
    '''This function simulates a PID controller and returns a list of the result values and a list of the manipulated variables'''

    #--- Declaring lists ---
    list_of_resultValues = [initialValue]
    time_list = [previousTime]
    list_of_manipulatedVariables = []

    #--- Declaring "changable" variables ---
    delta_T = 0.1                 #Time step
    previousTime = 0
    num_of_steps = 300
    initialValue = 0
    setpoint = 100                #Simulations setpoint/goal

    #--- creating a PID object ---
    pid = PIDController(0.8, 0.1, 0.1) 

    #--- Simulation ---
    for i in range(1, num_of_steps):
        #--- operations on time ---
        time = i * delta_T                                 #Calculating the time
        time_span = np.linspace(previousTime, time, 10)    #Creating a list of time values
        time_list.append(time)                             
        previousTime = time                               
        
        #--- Getting manipulatedVariuable(MV) from pid and calculating deretive of it to get result variable ---
        manipulatedVariable = pid.calculate(setpoint, list_of_resultValues[-1]),
        resultValues = odeint(pid.system, list_of_resultValues[-1], time_span, args = manipulatedVariable, tfirst=True)

        #--- Appending the result and manipulated variable to their lists ---
        list_of_resultValues.append(resultValues[-1][0])
        list_of_manipulatedVariables.append(manipulatedVariable[0])
        