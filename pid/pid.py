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

    def system(self, none1, none2, MV):
        '''This function is the system that the PID controller is controlling. It takes in the manipulated variable(MV) and returns the deretive of the result variable(X)'''

        #--- system ---
        dXdt =  (MV * 2) + (MV * 3) / 4 
        
        return dXdt


def simulation(kp, ki, kd, deltaT, steps, initVal, setPoint, autoTuning):
    '''This function simulates a PID controller and returns a list of the result values and a list of the manipulated variables'''
    #--- Declaring "changable" variables ---
    delta_T = deltaT               #Time step
    previousTime = 0
    num_of_steps = steps
    initialValue = initVal
    setpoint = setPoint            #Simulations setpoint/goal

    #--- Declaring lists ---
    list_of_resultValues = [initialValue]
    time_list = [previousTime]
    list_of_manipulatedVariables = []

    #--- creating a PID object with or without zeigler-nichols autotuning---
    if autoTuning == False:
        pid = PIDController(kp, ki, kd) 
    elif autoTuning == True:
        pid = PIDController(2.39, 0.05, 0.0125) #variables from zeigler-nichols tuning

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

    return list_of_resultValues, time_list
        