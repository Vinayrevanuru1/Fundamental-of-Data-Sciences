from cmath import log
import numpy as np
import pandas as pd
import sys
import util
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Check the command line
if len(sys.argv) != 2:
    print(f"{sys.argv[0]} <xlsx>")
    exit(1)

# Learning rate
t = 0.001

# Limit interations
max_steps = 1000

# Get the arg and read in the spreadsheet
infilename = sys.argv[1]
X, Y, labels = util.read_excel_data(infilename)
n, d = X.shape
print(f"Read {n} rows, {d - 1} features from '{infilename}'.")

# Get the mean and standard deviation for each column
## Your code here
means = np.mean(X, axis=0)
stds = np.std(X, axis=0)

X_copy = X.copy()

Xp = np.ones((n, d))

for i in range(1, d):
    for j in range(n):
        Xp[j][i] = (X.iloc[j, i] - means[i]) / stds[i]


# First guess for B is "all coefficents are zero"
B = np.zeros(d)
print(f"{B} =B")
# Create a numpy array to record avg error for each step
errors = np.zeros(max_steps)
## Your code here
print(Xp,"Xp",B,"B")

for i in range(1000):

    # Compute the gradient
    grd = Xp @ B
    # Compute the error
    error = grd - Y
    # Update B
    B = B - t * (Xp.T @ error)

    # Record the error
    errors[i] = np.mean(error**2) / 2
     # Note the current B

    if errors[i]>errors[i-1] and i>1:
        break
    

while errors[-1] == 0:
    errors = errors[:-1]


print(f"Took {i} iterations to converge")


# "Unstandardize" the coefficients

B[0] = B[0] - np.sum(B[1:] * means[1:] / stds[1:])
for i in range(1, d):
    B[i] = B[i] / stds[i]

print("means",means[1:],"stds",stds[1:])
# Show the result
print(util.format_prediction(B, labels))

# Get the R2 score
R2 = util.score(B, X, Y)
print(f"R2 = {R2:f}")

# Draw a graph
fig1 = plt.figure(1, (4.5, 4.5))
plt.plot(errors)  ## Your code ehre
plt.xscale("log")
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.yscale("log")
fig1.savefig("err.png")
