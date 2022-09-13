import pandas as pd
import numpy as np

# Read in the excel file
# Returns:
#   X: first column is 1s, the rest are from the spreadsheet
#   Y: The last column from the spreadsheet
#   labels: The list of headers for the columns of X from the spreadsheet
def read_excel_data(infilename):

    data = pd.read_excel(infilename)
    Y = data["price"]
    X = data
    X["property_id"] = 1
    X.rename(columns={"property_id": "x0"}, inplace=True)
    X.drop("price", inplace=True, axis=1)
    labels = list(X.columns)
    return X, Y, labels


# Make it pretty
def format_prediction(B, labels):
    ## Your code here
    pred_string = f"price = ${B[0]:,.2f} + "
    for i in range(1, len(B)):
        pred_string += f"(${B[i]:,.2f} x {labels[i]}) + "
    pred_string = pred_string[:-3]
    return pred_string


# Return the R2 score for coefficients B
# Given inputs X and outputs Y
def score(B, X, Y):
    ## Your code here
    n, d = X.shape
    Xp = np.ones((n, d))
    for i in range(1, d):
        for j in range(n):
            Xp[j][i] = X.iloc[j, i]
    Yhat = Xp @ B
    Ybar = np.mean(Y)
    ssreg = np.sum((Yhat - Ybar) ** 2)
    sstot = np.sum((Y - Ybar) ** 2)
    return ssreg / sstot
