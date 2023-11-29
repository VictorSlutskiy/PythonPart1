import numpy as np

Y = np.random.uniform(13.5, 18.6, (12, 1))
X1 = np.ones((12, 1))
X2 = np.random.randint(25, 25 + 12, (12, 1))
X3 = np.random.randint(60, 82, (12, 1))
X = np.concatenate((np.concatenate((X1, X2), axis=1), X3), axis=1)
A = (np.linalg.inv(np.transpose(X).dot(X))).dot(np.transpose(X).dot(Y))
Y_n = A[0] + A[1] * X2 + A[2] * X3
print(Y)
print(Y_n)
