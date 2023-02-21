import numpy as np

# Creating a dictionary with the keys 'mean', 'variance', 'standard deviation', 'max', 'min', and
# 'sum'. The values are lists containing the mean, variance, standard deviation, max, min, and sum of
# the matrix along axis 0, axis 1, and flattened.

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(list).reshape(3,3)
        calculations = {
            'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
            'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
            'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
            'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
            'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
            'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
        }
        return calculations
