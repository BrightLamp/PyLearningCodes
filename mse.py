import numpy as np
from sklearn import linear_model

np.random.seed(123)
np.set_printoptions(suppress=True, linewidth=120)

X = np.random.random([10, 5]).astype(np.float)
y = np.random.random(10).astype(np.float)

# sklearn
linear = linear_model.LinearRegression()
linear.fit(X, y)

# Pure Python
X = np.hstack([np.ones([10, 1]), X])

IX = np.linalg.inv(np.matmul(X.T, X))
XIX = np.matmul(X, IX)
w = np.matmul(y, XIX)

print("----- Code Output -----")
print("sklearn coef", linear.coef_)
print("sklearn intercept", linear.intercept_)

print("numpy coef", w[1:])
print("numpy intercept", w[0])

"""
----- Code Output -----
sklearn coef [ 0.49571807 -0.4013861   0.67121452 -0.4458699  -0.68057386]
sklearn intercept 0.767935574124093
numpy coef [ 0.49571807 -0.4013861   0.67121452 -0.4458699  -0.68057386]
numpy intercept 0.7679355741241028
"""
