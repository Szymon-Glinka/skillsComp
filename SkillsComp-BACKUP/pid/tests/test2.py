# Zeigler-Nichols method for PID tuning
def zeigler_nichols_method(Ku, Tu):
    Kp = 0.6 * Ku
    Ki = 1.2 * Ku / Tu
    Kd = 0.075 * Ku * Tu
    return Kp, Ki, Kd

# Example usage
Ku = 2.5  # Ultimate gain
Tu = 3.0  # Ultimate period
Kp, Ki, Kd = zeigler_nichols_method(Ku, Tu)

print("Tuned PID parameters:")
print("Kp =", Kp)
print("Ki =", Ki)
print("Kd =", Kd)
