import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Provided data
J_values = np.array([3, 5, 7, 9, 11])
frequencies = np.array([345795.9899, 576267.9305, 806651.806, 1036912.393, 1267014.486])

# Define the model function for the transition frequency
def transition_frequency(J, B, D):
    return 2 * B * J - 4 * D * J**3

# Fit the model to the data
params, covariance = curve_fit(transition_frequency, J_values, frequencies)

# Extract fitted parameters
B, D = params

# Generate fitted frequencies for plotting
fitted_frequencies = transition_frequency(J_values, B, D)

# Plot the data and the fit
plt.scatter(J_values, frequencies, label="Measured Frequencies", color="blue")
plt.plot(J_values, fitted_frequencies, label=f"Fitted Model\nB = {B:.4f} MHz, D = {D:.4f} MHz", color="red")
plt.xlabel("J (Rotational Quantum Number)")
plt.ylabel("Frequency (MHz)")
plt.title("Fit of Transition Frequency Data for CO Molecule")
plt.legend()
plt.grid(True)
plt.show()

B, D
